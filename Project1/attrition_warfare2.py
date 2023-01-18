import vs as pg
import numpy as np
import peggy
import ab1
import ab6
import ab4
import ab2
import aabb

if __name__ == "__main__":
    peggy_white = peggy.AI(8, 1, 10)
    peggy_black = peggy.AI(8, -1, 10)
    ab1_white = ab1.AI(8, 1, 10)
    ab1_black = ab1.AI(8, -1, 10)
    ab2_white = ab2.AI(8, 1, 10)
    ab2_black = ab2.AI(8, -1, 10)
    aabb_white = aabb.AI(8, 1, 10)
    aabb_black = aabb.AI(8, -1, 10)
    ab4_white = ab4.AI(8, 1, 10)
    ab4_black = ab4.AI(8, -1, 10)
    ab6_white = ab6.AI(8, 1, 10)
    ab6_black = ab6.AI(8, -1, 10)
    peggy = 0
    ab1 = 0
    ab2 = 0
    ab4 = 0
    ab6 = 0

    # for i in range(3):
    #     game1 = pg.play_game_1(peggy_black, ab2_white)
    #     print(game1)
    #     game2 = pg.play_game_2(peggy_white, ab2_black)
    #     print(game2)
    #     game1 = pg.play_game_1(ab1_black, ab2_white)
    #     print(game1)
    #     game2 = pg.play_game_2(ab1_white, ab2_black)
    #     print(game2)
    #     game1 = pg.play_game_1(ab2_black, ab4_white)
    #     print(game1)
    #     game2 = pg.play_game_2(ab2_white, ab4_black)
    #     print(game2)
    #     game1 = pg.play_game_1(ab2_black, ab6_white)
    #     print(game1)
    #     game2 = pg.play_game_2(ab2_white, ab6_black)
    #     print(game2)
    #
    #     print("Peggy win : " + str(peggy_white.win + peggy_black.win))
    #     print("ab1 win : " + str(ab1_white.win + ab1_black.win))
    #     print("ab2 win : " + str(ab2_white.win + ab2_black.win))
    #     print("ab4 win : " + str(ab4_white.win + ab4_black.win))
    #     print("ab6 win : " + str(ab6_white.win + ab6_black.win))

    for i in range(5):
        game1 = pg.play_game_1(aabb_black, ab2_white)
        print(game1)
        game2 = pg.play_game_2(aabb_white, ab2_black)
        print(game2)

    print("ab2 win : " + str(ab2_white.win + ab2_black.win))
    print("aabb win : " + str(aabb_white.win + aabb_black.win))
