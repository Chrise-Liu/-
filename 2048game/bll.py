"""
    遊戲邏輯處理，負責處理遊戲核心算法。
"""
from model import DirectionModel
import random
from model import Location

class GameCoreController:
    """
        遊戲核心管控類
    """
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        """
        屬性管控，類外可獲取目前map的數據
        :return: self.__map
        """
        return self.__map

    def __zero_to_end(self):
        """
            將0元素移動至末尾
        """
        for i in range(-1,-len(self.__list_merge),-1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            相鄰兩相同元素相加
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge)-1):
            if self.__list_merge[i] == self.__list_merge[i+1]:
                self.__list_merge[i] += self.__list_merge[i+1]
                del self.__list_merge[i+1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            map向左移動
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            map向右移動
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __square_matrix_transpose(self):
        """
            矩陣轉置(二維)
        """
        for r in range(0,len(self.__map)):
            for c in range(r+1,len(self.__map[r])):
                self.__map[r][c],self.__map[c][r] = self.__map[c][r],self.__map[r][c]

    def __move_up(self):
        """
            map向上移動
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        """
            map向下移動
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def move(self, dir):
        """
            控制移動
        :param dir: 方向,DirectionModel類
        :return:
        """
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    def generate_new_number(self):
        """
            生成新的數字
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        """
            新數字機率:
            90% == 2
            10% == 4
        :return: 新數字
        """
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        """
            統計目前map中有多少空位(0元素)
            * 每次計算前先清空self.__list_empty_location，避免上次數據影響
        """
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r,c))

    def is_game_over(self):
        """
            判斷遊戲是否結束
            1. 判斷map是否還有空位
            2. 判斷左右或上下是否有相同數字
        :return: True表示結束 False表示沒結束
        """
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map)-1):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False
        return True



