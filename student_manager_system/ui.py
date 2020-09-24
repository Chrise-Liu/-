"""
    學生資訊管理系統 界面
"""
from bll import StudentManagerController
from model import StudentModel

class StudentManagerView:
    """
    學生管理系統介面
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        """
            顯示選項
        """
        print("1)添加學生訊息")
        print("2)顯示學生訊息")
        print("3)刪除學生訊息")
        print("4)修改學生訊息")
        print("5)依照成績升序排列")

    def __select_menu(self):
        """
            選項選擇處理
        """
        item = input("請輸入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__manager.order_by_id()
            self.__output_students(self.__manager.student_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()
        else:
            print("輸入錯誤。")

    def main(self):
        """
            界面視圖入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        """
            自終端獲取學生訊息並添加學生對像
        """
        name = input("請輸入學生姓名：")
        age = int(input("請輸入學生年齡："))
        score = int(input("請輸入學生成績："))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        """
            顯示當前學生對像訊息
        :param list_output: 存儲學生對像列表
        :return: 返回學生訊息
        """
        for item in list_output:
            print("學號：%d, 學生姓名：%s, 年齡：%d, 成績：%d."%(item.id, item.name, item.age, item.score))

    def __delete_student(self):
        """
            根據學生ID刪除學生訊息
        """
        id = int(input("請輸入學生學號："))
        if self.__manager.remove_student(id):
            print("刪除成功。")
        else:
            print("刪除失敗。")

    def __modify_student(self):
        """
            根據學生ID 修改學生其餘訊息
        """
        stu = StudentModel()
        stu.id = int(input("請輸入要修改的學生學號："))
        stu.name = input("請輸入新的學生名稱：")
        stu.age = int(input("請輸入新的學生年齡："))
        stu.score = int(input("請輸入新的學生成績："))
        if self.__manager.update_student(stu):
            print("修改成功。")
        else:
            print("修改失敗。")

    def __output_student_by_score(self):
        """
            依據學生成績升序顯示學生資訊
        :return: 學生排序
        """
        self.__manager.order_by_score()
        self.__output_students(self.__manager.student_list)