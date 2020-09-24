"""
    學生訊息邏輯管理
"""

class StudentManagerController:
    """
        學生管理器，負責功能邏輯處裡
    """

    # 類變量id，表示學生學號初始值
    __init_id = 1000

    def __init__(self):
        self.__student_list = []

    @property
    def student_list(self):
        """
            學生列表，儲存學生對像
        :return:
        """
        return self.__student_list

    def __generate_id(self):
        """
            新增一個學號
        :return: 新學號
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def add_student(self, stu_info):
        """
            添加一個新學生
        :param stu_info: 沒有編號的學生訊息
        """
        stu_info.id = self.__generate_id()
        self.__student_list.append(stu_info)

    def remove_student(self, id):
        """
            根據編號刪除學生資訊
        :param id: 編號
        :return:
        """
        for item in self.__student_list:
            if item.id == id:
                self.__student_list.remove(item)
                return True  # 表示刪除成功
        return False  # 表示刪除失敗

    def update_student(self, stu_info):
        """
            根據stu_info.id修改學生其他訊息
        :param stu_info: 學生對像
        :return: 是否修改成功
        """
        for item in self.__student_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.atk = stu_info.age
                item.score = stu_info.score
                return True # 表示修改成功
        return False # 表示修改失敗

    def order_by_score(self):
        """
            根據成績，對self.__student_list進行升序排列
        """
        for r in range(len(self.__student_list) - 1):
            for c in range(r + 1, len(self.__student_list)):
                if self.__student_list[r].score > self.__student_list[c].score:
                    self.__student_list[r], self.__student_list[c] = self.__student_list[c], self.__student_list[r]

    def order_by_id(self):
        """
            根據學號，對self.__student_list進行升序排列
        """
        for r in range(len(self.__student_list) - 1):
            for c in range(r + 1, len(self.__student_list)):
                if self.__student_list[r].id > self.__student_list[c].id:
                    self.__student_list[r], self.__student_list[c] = self.__student_list[c], self.__student_list[r]