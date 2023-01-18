import vs as pg
import numpy as np
import peggy
# import ab1
# import ab6
# import ab4
import ab2
import submit_v2
import aabb
import ab7
import ab8
import ab9
import ab11

if __name__ == "__main__":
    ab7_white = ab7.AI(8, 1, 10)
    ab7_black = ab7.AI(8, -1, 10)
    ab2_white = ab2.AI(8, 1, 10)
    ab2_black = ab2.AI(8, -1, 10)
    ab8_white = ab8.AI(8, 1, 10)
    ab8_black = ab8.AI(8, -1, 10)
    ab9_white = ab9.AI(8, 1, 10)
    ab9_black = ab9.AI(8, -1, 10)
    ab11_white = ab11.AI(8, 1, 10)
    ab11_black = ab11.AI(8, -1, 10)
    submit_v2_white = submit_v2.AI(8, 1, 10)
    submit_v2_black = submit_v2.AI(8, -1, 10)
    aabb_white = aabb.AI(8, 1, 10)
    aabb_black = aabb.AI(8, -1, 10)
    peggy_white = peggy.AI(8, 1, 10)
    peggy_black = peggy.AI(8, -1, 10)

    ab7 = 0
    ab2 = 0
    ab8 = 0
    ab9 = 0
    v2 = 0
    aabb = 0


    # game1 = pg.play_game_1(ab8_black, ab9_black)
    # print(game1)
    # game2 = pg.play_game_2(ab8_white, ab9_black)
    # print(game2)
    # game1 = pg.play_game_1(ab11_black, ab9_black)
    # print(game1)
    # game2 = pg.play_game_2(ab11_white, ab9_black)
    # print(game2)
    #
    # game1 = pg.play_game_1(ab9_black, aabb_white)
    # print(game1)
    # game2 = pg.play_game_2(ab9_white, aabb_black)
    # print(game2)
    # game1 = pg.play_game_1(ab9_black, submit_v2_white)
    # print(game1)
    # game2 = pg.play_game_2(ab9_white, submit_v2_black)
    # print(game2)
    #
    # game1 = pg.play_game_1(ab7_black, ab9_white)
    # print(game1)
    # game2 = pg.play_game_2(ab7_white, ab9_black)
    # print(game2)
    game1 = pg.play_game_1(peggy_black, ab9_white)
    print(game1)
    game2 = pg.play_game_2(peggy_white, ab9_black)
    print(game2)

    game1 = pg.play_game_1(ab2_black, ab9_white)
    print(game1)
    game2 = pg.play_game_2(ab2_white, ab9_black)
    print(game2)

    print("ab2 win : " + str(ab2_white.win + ab2_black.win))
    print("ab7 win : " + str(ab7_white.win + ab7_black.win))
    print("ab8 win : " + str(ab8_white.win + ab8_black.win))
    print("ab9 win : " + str(ab9_white.win + ab9_black.win))
    print("aabb win : " + str(aabb_white.win + aabb_black.win))
    print("v2 win : " + str(submit_v2_white.win + submit_v2_black.win))
    print("peggy win : " + str(peggy_white.win + peggy_black.win))
    print("ab11 win : " + str(ab11_white.win + ab11_black.win))

