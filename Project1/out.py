import numpy as np
import random
import time
import copy

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
d_row = [-1, 1, 0, 0, -1, -1, 1, 1]
d_col = [0, 0, -1, 1, -1, 1, 1, -1]
INFINITY = 210000000
SOSO = 0
MAX_depth = 2
weight = [[-800, 260, -50, -30, -30, -50, 260, -800],
          [260, 100, -10, -5, -5, -10, 100, 260],
          [-50, -10, -5, 3, 3, -5, -10, -50],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-50, -10, -5, 3, 3, -5, -10, -50],
          [260, 100, -10, -5, -5, -10, 100, 260],
          [-800, 260, -50, -30, -30, -50, 260, -800]]

# def search(row, col, chessboard, current_color):
#     flag = False
#     for i in range(8):
#         r = row + d_row[i]
#         c = col + d_col[i]
#         if 8 > r >= 0 and 8 > c >= 0:
#             if chessboard[r][c] == -current_color:
#                 flag = nextSearch(r, c, i, chessboard, current_color)
#         if flag:
#             return True
#     return False
#
# def nextSearch(r, c, i, chessboard, current_color):
#     if 8 > r + d_row[i] >= 0 and 8 > c + d_col[i] >= 0:
#         r = r + d_row[i]
#         c = c + d_col[i]
#         if chessboard[r][c] == -current_color:
#             return nextSearch(r, c, i, chessboard, current_color)
#         elif chessboard[r][c] == current_color:
#             return True
#         else:
#             return False
#
# # 找到当前所有合法位置
# def find_valid_position(chessboard, color):
#     candidate_list = []
#     idx_none = np.where(chessboard == COLOR_NONE)
#     idx_none = list(zip(idx_none[0], idx_none[1]))
#     for pos_none in idx_none:
#         if search(pos_none[0], pos_none[1], chessboard, color):
#             candidate_list.append(pos_none)
#     return candidate_list


def find_actions(chessboard, player):
    actions = []
    my_positions = np.where(chessboard == player)
    # print(len(my_positions))
    my_positions = list(zip(my_positions[0], my_positions[1]))
    # print(len(my_positions))
    for i in range(len(my_positions)):
        flag_nextpos = False
        for j in range(8):
            cur = my_positions[i]
            flag = False
            while 8 > cur[0] + d_row[j] >= 0 and 8 > cur[1] + d_col[j] >= 0:
                cur = (cur[0] + d_row[j], cur[1] + d_col[j])
                if chessboard[cur[0]][cur[1]] == player:
                    break
                elif chessboard[cur[0]][cur[1]] == COLOR_NONE:
                    if flag:
                        actions.append(cur)
                        flag_nextpos = True
                    break
                else:
                    flag = True
            if flag_nextpos:
                 break
    return actions
#
# def find_actions(chessboard, player):
#     actions = []
#     my_positions = np.where(chessboard == COLOR_NONE)
#     # print(len(my_positions))
#     my_positions = list(zip(my_positions[0], my_positions[1]))
#     # print(len(my_positions))
#     for i in range(len(my_positions)):
#         # print(my_positions[i])
#         flag_nextpos = False
#         for j in range(8):
#             cur_r = my_positions[i][0]
#             cur_c = my_positions[i][1]
#             flag = False
#             while 8 > cur_r + d_row[j] >= 0 and 8 > cur_c + d_col[j] >= 0:
#                 cur_r += d_row[j]
#                 cur_c += d_col[j]
#                 if chessboard[cur_r][cur_c] == COLOR_NONE:
#                     break
#                 elif chessboard[cur_r][cur_c] == player:
#                     if flag:
#                         actions.append(my_positions[i])
#                         flag_nextpos = True
#                     break
#                 else:
#                     flag = True
#             if flag_nextpos:
#                  break
#     return actions

def change_weight(chessboard):
    # 感觉可以再调更小一点
    global weight
    if chessboard[0][0] != 0:
        weight[0][1] = -100
        weight[1][0] = -100
        weight[1][1] = -50
    # else:
    #     weight[0][1] = 260
    #     weight[1][0] = 260
    #     weight[1][1] = 100

    if chessboard[7][0] != 0:
        weight[7][1] = -100
        weight[6][0] = -100
        weight[6][1] = -50
    # else:
    #     weight[7][1] = 260
    #     weight[6][0] = 260
    #     weight[6][1] = 100

    if chessboard[0][7] != 0:
        weight[0][6] = -100
        weight[1][7] = -100
        weight[1][6] = -50
    # else:
    #     weight[0][6] = 260
    #     weight[1][7] = 260
    #     weight[1][6] = 100

    if chessboard[7][7] != 0:
        weight[7][6] = -100
        weight[6][7] = -100
        weight[6][6] = -50
    # else:
    #     weight[7][6] = 260
    #     weight[6][7] = 260
    #     weight[6][6] = 100


def result(chessboard, move, cur_player):
    chessboard[move[0]][move[1]] = cur_player
    for i in range(8):
        cur_row = move[0] + d_row[i]
        cur_col = move[1] + d_col[i]
        flag = False
        while 0 <= cur_row < 8 and 0 <= cur_col < 8:
            if chessboard[cur_row][cur_col] == -cur_player:
                cur_row += d_row[i]
                cur_col += d_col[i]
                flag = True
            elif chessboard[cur_row][cur_col] == cur_player and flag:
                cur_row -= d_row[i]
                cur_col -= d_col[i]
                while cur_row != move[0] or cur_col != move[1]:
                    chessboard[cur_row][cur_col] = cur_player
                    cur_row -= d_row[i]
                    cur_col -= d_col[i]
                break
            else:
                break

def utility(chessboard, color):
    ret = 0
    his_valid_list = find_actions(chessboard, -color)
    if len(his_valid_list) <= 5:
        ret += 50
        for valid in his_valid_list:
            if valid == (0, 0):
                ret += 50
            elif valid == (7, 0):
                ret += 50
            elif valid == (0, 7):
                ret += 50
            elif valid == (7, 7):
                ret += 50
    elif len(his_valid_list) < 3:
        ret += 200
        for valid in his_valid_list:
            if valid == (0, 0):
                ret += 50
            elif valid == (7, 0):
                ret += 50
            elif valid == (0, 7):
                ret += 50
            elif valid == (7, 7):
                ret += 50
    cnt_white = 0
    cnt_black = 0
    for i in range(8):
        for j in range(8):
            if color == COLOR_WHITE:
                if chessboard[i][j] == COLOR_WHITE:
                    ret += weight[i][j]
                    cnt_white += 1
                elif chessboard[i][j] == COLOR_BLACK:
                    ret -= weight[i][j]
                    cnt_black += 1
            else:
                if chessboard[i][j] == COLOR_WHITE:
                    ret -= weight[i][j]
                    cnt_white += 1
                elif chessboard[i][j] == COLOR_BLACK:
                    ret += weight[i][j]
                    cnt_black += 1
    if MAX_depth == 9:
        if color == COLOR_WHITE:
            ret = cnt_black - cnt_white
        else:
            ret = cnt_white - cnt_black
    return ret, None
#
# def utility(chessboard, player):
#     my_actions = find_actions(chessboard, player)
#     opponent_actions = find_actions(chessboard, -player)
#     # 如果结束，直接返回结局  可以优化 反正find action遍历的时候顺便算出diff
#     if len(my_actions) == 0 and len(opponent_actions) == 0:
#         diff = 0
#         for i in range(8):
#             for j in range(8):
#                 if chessboard[i][j] == player:
#                     diff = diff + 1
#                 elif chessboard[i][j] == -player:
#                     diff = diff - 1
#         if diff > 0:
#             return INFINITY, None  # 一个值
#         elif diff < 0:
#             return -INFINITY, None
#         else:
#             return SOSO, None
#
#     # 评估函数
#     else:
#         # 1.位置权重，值越大越好
#         value = 0
#         # 2.现有个数之差 （对方的-我的）*100 所以是越大越好
#         diff_num = 0
#         for i in range(8):
#             for j in range(8):
#                 if chessboard[i][j] == player:
#                     diff_num -= 1
#                     value += weight[i][j]
#                 elif chessboard[i][j] == -player:
#                     diff_num += 1
#                     value -= weight[i][j]
#
#         # 3.判断行动力 （对方-我）*100 越大越好
#         diff_actions = (len(opponent_actions) - len(my_actions)) * 100
#
#         # 4.判断能否逼迫对方占角
#         force_corner = 0
#         if len(opponent_actions) <= 5:
#             for valid in opponent_actions:
#                 if valid in [(0, 0), (7, 0), (0, 7), (7, 7)]:
#                     force_corner += 100
#         elif len(opponent_actions) < 3:
#             for valid in opponent_actions:
#                 if valid in [(0, 0), (7, 0), (0, 7), (7, 7)]:
#                     force_corner += 250
#
#         if MAX_depth == 9:
#             return diff_num, None
#         else:
#             return value + diff_actions + diff_num + force_corner, None
#

#没有判断是否结束，直接按utility算
def alphabeta_search(chessboard, color):
    def max_value(current_chessboard, current_candidate, depth, alpha, beta, current_color):
        change_weight(current_chessboard)
        if depth > MAX_depth:
            return utility(current_chessboard, color)  # 不一定当时这个局面颜色是我的？对于我这个局面的评估
        v, move = -INFINITY, None
        if not current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            v2, _ = min_value(temp_chessboard, find_actions(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 > v:
                v, move = v2, None
            alpha = max(alpha, v)
            if alpha >= beta:
                return v, move
        for a in current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            result(temp_chessboard, a, current_color)
            v2, _ = min_value(temp_chessboard, find_actions(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 > v:
                v, move = v2, a
            alpha = max(alpha, v)
            if alpha >= beta:
                return v, move
        return v, move

    def min_value(current_chessboard, current_candidate, depth, alpha, beta, current_color):
        change_weight(current_chessboard)
        if depth > MAX_depth:
            return utility(current_chessboard, color)
        v, move = INFINITY, None
        if not current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            v2, _ = max_value(temp_chessboard, find_actions(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 < v:
                v, move = v2, None
            beta = min(beta, v)
            if beta <= alpha:
                return v, move
        for a in current_candidate:
            temp_chessboard = copy.deepcopy(current_chessboard)
            result(temp_chessboard, a, current_color)
            v2, _ = max_value(temp_chessboard, find_actions(temp_chessboard, -current_color), depth + 1, alpha,
                              beta, -current_color)
            if v2 < v:
                v, move = v2, a
            beta = min(beta, v)
            if beta <= alpha:
                return v, move
        return v, move

    return max_value(chessboard, find_actions(chessboard, color), 0, -INFINITY, +INFINITY, color)


# def alphabeta_search(chessboard, player):
#
#     def max_value(cur_chessboard, cur_depth, alpha, beta):
#
#         change_weight(cur_chessboard)
#         if cur_depth > MAX_depth:
#             return utility(cur_chessboard, player)
#
#         v, move = -INFINITY, None
#         cur_candidate_list = find_actions(cur_chessboard, player)
#         if len(cur_candidate_list) == 0:
#             temp_chessboard = cur_chessboard.copy()
#             v2, _ = min_value(temp_chessboard, cur_depth + 1, alpha, beta)
#             if v2 > v:
#                 v, move = v2, None
#             if v >= beta:
#                 return v, move
#             # alpha = max(alpha, v)
#
#         for a in cur_candidate_list:
#             temp_chessboard = cur_chessboard.copy()
#             result(temp_chessboard, a, player)
#             v2, _ = min_value(temp_chessboard, cur_depth + 1, alpha, beta)
#             if v2 > v:
#                 v, move = v2, a
#             if v >= beta:
#                 break
#             alpha = max(alpha, v)
#         return v, move
#
#     def min_value(cur_chessboard, cur_depth, alpha, beta):
#         change_weight(cur_chessboard)
#         if cur_depth > MAX_depth:
#             return utility(cur_chessboard, player)  # 不一定当时这个局面颜色是我的？
#         v, move = INFINITY, None
#         cur_candidate_list = find_actions(cur_chessboard, -player)
#         if len(cur_candidate_list) == 0:
#             temp_chessboard = cur_chessboard.copy()
#             v2, _ = max_value(temp_chessboard, cur_depth + 1, alpha, beta)
#             if v2 < v:
#                 v, move = v2, None
#             if v <= alpha:
#                 return v, move
#             # beta = min(beta, v)
#
#         for a in cur_candidate_list:
#             temp_chessboard = cur_chessboard.copy()
#             result(temp_chessboard, a, -player)
#             v2, _ = max_value(temp_chessboard, cur_depth + 1, alpha, beta)
#             if v2 < v:
#                 v, move = v2, a
#             if v <= alpha:
#                 break
#             beta = min(beta, v)
#         return v, move
#
#     return max_value(chessboard, 0, -INFINITY, INFINITY)

# don't change the class name
class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need to add your decision to your candidate_list. The system will get the end of your candidate_list as your decision.
        self.candidate_list = []

    # The input is the current chessboard. Chessboard is a numpy array.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        start_time = time.perf_counter()
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here

        self.candidate_list = find_actions(chessboard, self.color)
        priority, max_weight = None, -INFINITY
        for positions in self.candidate_list:
            if weight[positions[0]][positions[1]] > max_weight:
                priority, max_weight = positions, weight[positions[0]][positions[1]]
        if priority is not None:
            self.candidate_list.remove(priority)
            self.candidate_list.append(priority)

        # 更改搜索深度
        # change_max_depth(chessboard)
        idx_none = np.where(chessboard == COLOR_NONE)
        idx_none = list(zip(idx_none[0], idx_none[1]))
        global MAX_depth
        if 17 <= len(idx_none) < 30:
            MAX_depth = 3
        elif 14 <= len(idx_none) < 17:
            MAX_depth = 4
        elif 12 <= len(idx_none) < 14:
            MAX_depth = 5
        elif 11 <= len(idx_none) < 12:
            MAX_depth = 7
        elif 0 < len(idx_none) < 11:
            MAX_depth = 9
        else:
            MAX_depth = 2
        _, move = alphabeta_search(chessboard, self.color)
        if move is not None:
            self.candidate_list.remove(move)
            self.candidate_list.append(move)
        time_elapsed = time.perf_counter() - start_time
        print("ab total time is: " + str(time_elapsed) + "s")
        return self.candidate_list

    # def go1(self, chessboard):
    #     # start_time = time.perf_counter()
    #     self.candidate_list.clear()
    #     self.candidate_list = find_actions(chessboard, self.color)
    #     return self.candidate_list

    # Here is the simplest sample:Random decision
    # idx = np.where(chessboard == COLOR_NONE)
    # idx = list(zip(idx[0], idx[1]))
    # ==============Find new pos========================================
    # Make sure that the position of your decision on the chess board is empty.
    # If not, the system will return error.
    # Add your decision into candidate_list, Records the chessboard
    # You need to add all the positions which are valid
    # candidate_list example: [(3,3),(4,4)]
    # You need append your decision at the end of the candidate_list,
    # candidate_list example: [(3,3),(4,4),(4,4)]
    # we will pick the last element of the candidate_list as the position you choose.
    # In above example, we will pick (4,4) as your decision.
    # If there is no valid position, you must return an empty list.

# chessboard= [[0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, -1, 0, 0, 0, 0, 0, 0],
#                  [0, 0, -1, 1, 1, 0, 0, 0],
#                  [0, 0, 0, -1, 1, 0, 0, 0],
#                  [0, 0, -1, 1, 1, 1, 0, 0],
#                  [0, -1, 0, 0, 1, 1, 1, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0]]

# ai = AI(8,1,5)
# ai.candidate_list = find_actions(chessboard)
# print(ai.candidate_list)
