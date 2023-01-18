import vs as pg
import numpy as np
# import peggy
# import ab1
# import ab6
# import ab4
import ab2
import submit_v2
import aabb
import ab7
import ab8
import ab9

if __name__ == "__main__":
    # peggy_white = peggy.AI(8, 1, 10)
    # peggy_black = peggy.AI(8, -1, 10)
    # ab1_white = ab1.AI(8, 1, 10)
    # ab1_black = ab1.AI(8, -1, 10)
    # ab2_white = ab2.AI(8, 1, 10)
    # ab2_black = ab2.AI(8, -1, 10)
    # ab4_white = ab4.AI(8, 1, 10)
    # ab4_black = ab4.AI(8, -1, 10)
    # ab6_white = ab6.AI(8, 1, 10)
    # ab6_black = ab6.AI(8, -1, 10)
    # submit_v1_white = submit_v1.AI(8, 1, 10)
    # submit_v1_black = submit_v1.AI(8, -1, 10)

    ab7_white = ab7.AI(8, 1, 10)
    ab7_black = ab7.AI(8, -1, 10)
    ab2_white = ab2.AI(8, 1, 10)
    ab2_black = ab2.AI(8, -1, 10)
    ab8_white = ab8.AI(8, 1, 10)
    ab8_black = ab8.AI(8, -1, 10)
    ab9_white = ab9.AI(8, 1, 10)
    ab9_black = ab9.AI(8, -1, 10)
    submit_v2_white = submit_v2.AI(8, 1, 10)
    submit_v2_black = submit_v2.AI(8, -1, 10)
    aabb_white = aabb.AI(8, 1, 10)
    aabb_black = aabb.AI(8, -1, 10)

    ab7 = 0
    ab2 = 0
    ab8 = 0
    ab9 = 0
    v2 = 0
    aabb = 0


    # peggy = 0
    # ab1 = 0
    # ab2 = 0
    # ab4 = 0
    # ab6 = 0

    # for i in range(5):
        # game1 = pg.play_game_1(peggy_black, ab1_white)
        # print(game1)
        # game2 = pg.play_game_2(peggy_white, ab1_black)
        # print(game2)
        # game1 = pg.play_game_1(peggy_black, ab2_white)
        # print(game1)
        # game2 = pg.play_game_2(peggy_white, ab2_black)
        # print(game2)
        # game1 = pg.play_game_1(peggy_black, ab4_white)
        # print(game1)
        # game2 = pg.play_game_2(peggy_white, ab4_black)
        # print(game2)
        # game1 = pg.play_game_1(peggy_black, ab6_white)
        # print(game1)
        # game2 = pg.play_game_2(peggy_white, ab6_black)
        # print(game2)

    game1 = pg.play_game_1(ab2_black, ab7_black)
    print(game1)
    game2 = pg.play_game_2(ab2_white, ab7_black)
    print(game2)
    game1 = pg.play_game_1(ab2_black, ab8_white)
    print(game1)
    game2 = pg.play_game_2(ab2_white, ab8_black)
    print(game2)
    game1 = pg.play_game_1(ab2_black, ab9_white)
    print(game1)
    game2 = pg.play_game_2(ab2_white, ab9_black)
    print(game2)
    game1 = pg.play_game_1(ab2_black, aabb_white)
    print(game1)
    game2 = pg.play_game_2(ab2_white, aabb_black)
    print(game2)
    game1 = pg.play_game_1(ab2_black, submit_v2_white)
    print(game1)
    game2 = pg.play_game_2(ab2_white, submit_v2_black)
    print(game2)

    game1 = pg.play_game_1(aabb_black, submit_v2_white)
    print(game1)
    game2 = pg.play_game_2(aabb_white, submit_v2_black)
    print(game2)

        # game1 = pg.play_game_1(submit_v2_black, ab2_white)
        # print(game1)
        # game2 = pg.play_game_2(submit_v2_white, ab2_black)
        # print(game2)

    # game1 = pg.play_game_1(ab7_black, ab8_white)
    # print(game1)
    # game2 = pg.play_game_2(ab7_white, ab8_black)
    # print(game2)
    # game1 = pg.play_game_1(ab7_black, ab9_white)
    # print(game1)
    # game2 = pg.play_game_2(ab7_white, ab9_black)
    # print(game2)
    # game1 = pg.play_game_1(ab7_black, aabb_white)
    # print(game1)
    # game2 = pg.play_game_2(ab7_white, aabb_black)
    # print(game2)
    # game1 = pg.play_game_1(ab7_black, submit_v2_white)
    # print(game1)
    # game2 = pg.play_game_2(ab7_white, submit_v2_black)
    # print(game2)

        # game1 = pg.play_game_1(ab2_black, ab4_white)
        # print(game1)
        # game2 = pg.play_game_2(ab2_white, ab4_black)
        # print(game2)
        # game1 = pg.play_game_1(ab2_black, ab6_white)
        # print(game1)
        # game2 = pg.play_game_2(ab2_white, ab6_black)
        # print(game2)

        # game1 = pg.play_game_1(ab4_black, ab6_white)
        # print(game1)
        # game2 = pg.play_game_2(ab4_white, ab6_black)
        # print(game2)

    print("ab2 win : " + str(ab2_white.win + ab2_black.win))
    print("ab7 win : " + str(ab7_white.win + ab7_black.win))
    print("ab8 win : " + str(ab8_white.win + ab8_black.win))
    print("ab9 win : " + str(ab9_white.win + ab9_black.win))
    print("aabb win : " + str(aabb_white.win + aabb_black.win))
    print("v2 win : " + str(submit_v2_white.win + submit_v2_black.win))
