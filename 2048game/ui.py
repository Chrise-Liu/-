"""
    2048遊戲 控制介面
"""
from bll import GameCoreController
from model import DirectionModel
import os

class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self.__start()
        self.__update()

    def __start(self):
        """
            遊戲開始產生隨機兩個數字
            繪製介面
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()

    def __draw_map(self):
        """
            先清空控制台
            再列出map
        """
        # os.system("clear")
        for line in self.__controller.map:
            for i in line:
                print(i,end=" ")
            print()

    def __update(self):
        """
            循環執行:
            1. 接收玩家指令
            2. 產生兩個新數字
            3. 將改變介面繪出
            4. 判斷遊戲是否結束
        """
        while True:
            self.__move_map_for_input()
            self.__controller.generate_new_number()
            self.__draw_map()
            if self.__controller.is_game_over():
                print("遊戲結束!")
                break

    def __move_map_for_input(self):
        """
            接收玩家輸入的指令
            移動map
        """
        dir = input("請輸入方向(wsad):")
        dict_dir = {
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT,
        }
        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])