"""
    學生模型類
    管理每個學生的資訊
"""

class StudentModel:
    def __init__(self,name="",age=0,score=0,id=0):
        """
            學生基本資訊
        :param name: 姓名
        :param id: 學號
        :param age: 年齡
        :param score: 成績
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score