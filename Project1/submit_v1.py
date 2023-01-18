import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
d_row = [-1, 1, 0, 0, -1, -1, 1, 1]
d_col = [0, 0, -1, 1, -1, 1, 1, -1]
INFINITY = 210000000
SOSO = 0
MAX_depth = 2
weight = [[-8000, 260, -50, -30, -30, -50, 260, -8000],
          [260, 200, -10, -5, -5, -10, 200, 260],
          [-50, -10, -5, 3, 3, -5, -10, -50],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-30, -5, 3, 1, 1, 3, -5, -30],
          [-50, -10, -5, 3, 3, -5, -10, -50],
          [260, 200, -10, -5, -5, -10, 200, 260],
          [-8000, 260, -50, -30, -30, -50, 260, -8000]]


def find_actions(chessboard, player):
    actions = []
    my_positions = np.where(chessboard == COLOR_NONE)
    my_positions = list(zip(my_positions[0], my_positions[1]))
    for i in range(len(my_positions)):
        flag_nextpos = False
        for j in range(8):
            cur_r = my_positions[i][0]
            cur_c = my_positions[i][1]
            flag = False
            while 8 > cur_r + d_row[j] >= 0 and 8 > cur_c + d_col[j] >= 0:
                cur_r += d_row[j]
                cur_c += d_col[j]
                if chessboard[cur_r][cur_c] == COLOR_NONE:
                    break
                elif chessboard[cur_r][cur_c] == player:
                    if flag:
                        actions.append(my_positions[i])
                        flag_nextpos = True
                    break
                else:
                    flag = True
            if flag_nextpos:
                break
    return actions


def change_weight(chessboard):
    # 鎰熻鍙互鍐嶈皟鏇村皬涓€鐐�
    global weight
    if chessboard[0][0] != 0:
        weight[0][1] = -100
        weight[1][0] = -100
        weight[1][1] = -50
    else:
        weight[0][1] = 260
        weight[1][0] = 260
        weight[1][1] = 200

    if chessboard[7][0] != 0:
        weight[7][1] = -100
        weight[6][0] = -100
        weight[6][1] = -50
    else:
        weight[7][1] = 260
        weight[6][0] = 260
        weight[6][1] = 200

    if chessboard[0][7] != 0:
        weight[0][6] = -100
        weight[1][7] = -100
        weight[1][6] = -50
    else:
        weight[0][6] = 260
        weight[1][7] = 260
        weight[1][6] = 200

    if chessboard[7][7] != 0:
        weight[7][6] = -100
        weight[6][7] = -100
        weight[6][6] = -50
    else:
        weight[7][6] = 260
        weight[6][7] = 260
        weight[6][6] = 200


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


def utility(chessboard, player):
    my_actions = find_actions(chessboard, player)
    opponent_actions = find_actions(chessboard, -player)
    # 濡傛灉缁撴潫锛岀洿鎺ヨ繑鍥炵粨灞€  鍙互浼樺寲 鍙嶆find action閬嶅巻鐨勬椂鍊欓『渚跨畻鍑篸iff
    if len(my_actions) == 0 and len(opponent_actions) == 0:
        diff = 0
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == player:
                    diff = diff - 1
                elif chessboard[i][j] == -player:
                    diff = diff + 1
        if diff > 0:
            return INFINITY, None  # 涓€涓€�
        elif diff < 0:
            return diff*1000, None
        else:
            return SOSO, None

    # 璇勪及鍑芥暟
    else:
        # 1.浣嶇疆鏉冮噸锛屽€艰秺澶ц秺濂�
        value = 0
        # 2.鐜版湁涓暟涔嬪樊 锛堝鏂圭殑-鎴戠殑锛�*10 鎵€浠ユ槸瓒婂ぇ瓒婂ソ
        diff_num = 0
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == player:
                    diff_num -= 1
                    value += weight[i][j]
                elif chessboard[i][j] == -player:
                    diff_num += 1
                    value -= weight[i][j]
        diff_num *= 15

        # 3.鍒ゆ柇琛屽姩鍔� 瀵规柟*5 瓒婂ぇ瓒婂ソ
        oppo_actions = len(opponent_actions) * 10

        # 4.鍒ゆ柇鑳藉惁閫艰揩瀵规柟鍗犺
        force_corner = 0
        if len(opponent_actions) <= 5:
            for valid in opponent_actions:
                if valid in [(0, 0), (7, 0), (0, 7), (7, 7)]:
                    force_corner += 100
        elif len(opponent_actions) < 3:
            for valid in opponent_actions:
                if valid in [(0, 0), (7, 0), (0, 7), (7, 7)]:
                    force_corner += 750
        if len(my_actions) <= 5:
            for valid in my_actions:
                if valid in [(0, 0), (7, 0), (0, 7), (7, 7)]:
                    force_corner -= 100
        elif len(my_actions) < 3:
            for valid in my_actions:
                if valid in [(0, 0), (7, 0), (0, 7), (7, 7)]:
                    force_corner -= 750

        idx_none = np.where(chessboard == COLOR_NONE)
        idx_len = len(list(zip(idx_none[0], idx_none[1])))

        # 灏惧眬
        if idx_len <= 10:
            w1 = 10
            w2 = 5
            w3 = 80
            w4 = 5
        # 娆″熬灞€
        elif idx_len <= 20:
            w1 = 45
            w2 = 20
            w3 = 35
            w4 = 20
        # 涓眬
        elif idx_len <= 40:
            w1 = 35
            w2 = 35
            w3 = 20
            w4 = 35
        # 寮€灞€
        else:
            w1 = 35
            w2 = 30
            w3 = 10
            w4 = 35
        # print(value)
        # print(oppo_actions)
        # print(diff_num)
        # print(force_corner)
        # print()
        # print(chessboard)
        eveal_value = w1 * value + w2 * oppo_actions + w3 * diff_num + w4 * force_corner
        return eveal_value, None

def alphabeta_search(chessboard, player):
    def max_value(cur_chessboard, cur_depth, alpha, beta):
        change_weight(cur_chessboard)
        if cur_depth > MAX_depth:
            return utility(cur_chessboard, player)

        v, move = -INFINITY, None
        cur_candidate_list = find_actions(cur_chessboard, player)
        if len(cur_candidate_list) == 0:
            temp_chessboard = cur_chessboard.copy()
            v2, _ = min_value(temp_chessboard, cur_depth + 1, alpha, beta)
            if v2 > v:
                v, move = v2, None
            if v >= beta:
                return v, move
            # alpha = max(alpha, v)

        for a in cur_candidate_list:
            temp_chessboard = cur_chessboard.copy()
            result(temp_chessboard, a, player)
            v2, _ = min_value(temp_chessboard, cur_depth + 1, alpha, beta)
            if v2 > v:
                v, move = v2, a
            if v >= beta:
                break
            alpha = max(alpha, v)
        return v, move

    def min_value(cur_chessboard, cur_depth, alpha, beta):
        change_weight(cur_chessboard)
        if cur_depth > MAX_depth:
            return utility(cur_chessboard, player)  # 涓嶄竴瀹氬綋鏃惰繖涓眬闈㈤鑹叉槸鎴戠殑锛�
        v, move = INFINITY, None
        cur_candidate_list = find_actions(cur_chessboard, -player)
        if len(cur_candidate_list) == 0:
            temp_chessboard = cur_chessboard.copy()
            v2, _ = max_value(temp_chessboard, cur_depth + 1, alpha, beta)
            if v2 < v:
                v, move = v2, None
            if v <= alpha:
                return v, move
            # beta = min(beta, v)

        for a in cur_candidate_list:
            temp_chessboard = cur_chessboard.copy()
            result(temp_chessboard, a, -player)
            v2, _ = max_value(temp_chessboard, cur_depth + 1, alpha, beta)
            if v2 < v:
                v, move = v2, a
            if v <= alpha:
                break
            beta = min(beta, v)
        return v, move

    return max_value(chessboard, 0, -INFINITY, INFINITY)


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
        self.win = 0

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

        # 鏇存敼鎼滅储娣卞害
        # change_max_depth(chessboard)
        idx_none = np.where(chessboard == COLOR_NONE)
        idx_none = list(zip(idx_none[0], idx_none[1]))
        global MAX_depth
        if 30 <= len(idx_none) < 40:
            MAX_depth = 2
        elif 17 <= len(idx_none) < 30:
            MAX_depth = 3
        elif 14 <= len(idx_none) < 17:
            MAX_depth = 4
        elif 11 <= len(idx_none) < 14:
            MAX_depth = 5
        # elif 11 <= len(idx_none) < 12:
        #     MAX_depth = 7
        elif 0 < len(idx_none) < 11:
            MAX_depth = 12
        else:
            MAX_depth = 3
        print(MAX_depth)
        # global MAX_depth
        # can_len = len(self.candidate_list)
        # if can_len < 3:
        #     MAX_depth = 9
        # elif can_len < 5:
        #     MAX_depth = 7
        # elif can_len < 7:
        #     MAX_depth = 3
        # else:
        #     MAX_depth = 2
        _, move = alphabeta_search(chessboard, self.color)
        if move is not None:
            self.candidate_list.remove(move)
            self.candidate_list.append(move)
        time_elapsed = time.perf_counter() - start_time
        print("ab total time is: " + str(time_elapsed) + "s")
        return self.candidate_list

    #鍙嶆€�1锛氬悆瓒婂瀛愯秺涓嶅ソ锛� 鐏汉娲昏矾 瑕佽瀵规柟琛屽姩鍔泆pup鎵嶈