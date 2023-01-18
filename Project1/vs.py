import numpy as np
import peggy
# import out
import ab6
# import ab4
import ab2

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
win_me = 0
win_other = 0


def action(move, chessboard, current_color):
    chessboard[move[0]][move[1]] = current_color
    for i in range(8):
        r = move[0] + dr[i]
        c = move[1] + dc[i]
        flag = False
        while 8 > r >= 0 and 8 > c >= 0:
            if chessboard[r][c] == 0:
                flag = False
                break
            elif chessboard[r][c] == -current_color:
                flag = True
                r += dr[i]
                c += dc[i]
            else:
                break
        if flag and 8 > r >= 0 and 8 > c >= 0:
            r -= dr[i]
            c -= dc[i]
            while r != move[0] or c != move[1]:
                chessboard[r][c] = current_color
                r -= dr[i]
                c -= dc[i]


def play_game_1(a, b):
    chessboard = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, -1, 0, 0, 0],
                           [0, 0, 0, -1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
    # AI_my = ab2.AI(8, -1, 10)
    # AI_peggy = ab6.AI(8, 1, 10)
    cnt = 0
    black_list = a.go(chessboard)
    white_list = b.go(chessboard)
    while black_list or white_list:
        # 偶数黑旗走
        if cnt % 2 == 0:
            if not black_list:
                cnt += 1
                continue
            black_move = black_list.pop()
            action(black_move, chessboard, -1)
            print(black_move)
        # 奇数白旗走
        if cnt % 2 == 1:
            if not white_list:
                cnt += 1
                continue
            white_move = white_list.pop()
            action(white_move, chessboard, 1)
            print(white_move)
        cnt += 1
        print("Step: " + str(cnt))
        print("=========================================")
        for line in chessboard:
            string = ""
            print("-----------------------------------------")
            for chess in line:
                if chess == 1:
                    string += " ██ |"
                elif chess == -1:
                    string += " △  |"
                else:
                    string += "    |"
            print("|" + string)
        print("=========================================")
        print()
        black_list = a.go(chessboard)
        white_list = b.go(chessboard)

    white_cnt = 0
    black_cnt = 0
    for line in chessboard:
        string = ""
        print("-----------------------------------------")
        for chess in line:
            if chess == 1:
                string += " ██ |"
                white_cnt += 1
            elif chess == -1:
                string += " △  |"
                black_cnt += 1
            else:
                string += "    |"
        print("|" + string)
    print("=========================================")
    # 第一轮我是黑
    if white_cnt < black_cnt:
        global win_other
        win_other += 1
        b.win +=1
        return "My AI is black (△), the other AI is white (██)\nWhite Win!!!"
    elif white_cnt > black_cnt:
        global win_me
        win_me += 1
        a.win += 1
        return "My AI is black (△), the other AI is white (██)\nBlack Win!!!"
    else:
        return "My AI is black (△), the other AI is white (██)\nGame Draw"


def play_game_2(a, b):
    chessboard = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, -1, 0, 0, 0],
                           [0, 0, 0, -1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
    # AI_my = ab2.AI(8, 1, 10)
    # AI_peggy = ab6.AI(8, -1, 10)
    cnt = 0
    black_list = b.go(chessboard)
    white_list = a.go(chessboard)
    while black_list or white_list:
        # 偶数黑旗走
        if cnt % 2 == 0:
            if not black_list:
                cnt += 1
                continue
            black_move = black_list.pop()
            action(black_move, chessboard, -1)
            print(black_move)
        # 奇数白旗走
        if cnt % 2 == 1:
            if not white_list:
                cnt += 1
                continue
            white_move = white_list.pop()
            action(white_move, chessboard, 1)
            print(white_move)
        cnt += 1
        print("Step: " + str(cnt))
        print("=========================================")
        for line in chessboard:
            string = ""
            print("-----------------------------------------")
            for chess in line:
                if chess == 1:
                    string += " ██ |"
                elif chess == -1:
                    string += " △  |"
                else:
                    string += "    |"
            print("|" + string)
        print("=========================================")
        print()
        black_list = b.go(chessboard)
        white_list = a.go(chessboard)

    white_cnt = 0
    black_cnt = 0
    for line in chessboard:
        string = ""
        print("-----------------------------------------")
        for chess in line:
            if chess == 1:
                string += " ██ |"
                white_cnt += 1
            elif chess == -1:
                string += " △  |"
                black_cnt += 1
            else:
                string += "    |"
        print("|" + string)
    print("=========================================")
    if white_cnt < black_cnt:
        global win_me
        win_me += 1
        a.win += 1
        return "My AI is white (██), the other AI is black (△)\nWhite Win!!!"
    elif white_cnt > black_cnt:
        global win_other
        win_other += 1
        b.win += 1
        return "My AI is white (██), the other AI is black (△)\nBlack Win!!!"
    else:
        return "My AI is white (██), the other AI is black (△)\nGame Draw"


# if __name__ == "__main__":
#     for i in range(2):
#         game1 = play_game_1()
#         print(game1)
#         game2 = play_game_2()
#         print(game2)
#     print("I win: ")
#     print(win_me)
#     print("Others win:")
#     print(win_other)
