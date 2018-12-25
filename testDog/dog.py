#coding:utf-8
class Dog(object):
    """一次模拟小狗的尝试"""
    def __init__(self, name, age):
        """初始化属性name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟蹲下"""
        print(self.name.title() + " is now sitting.")
    
    def rollOver(self):
        """模拟打滚"""
        print(self.name.title() + " rolled over!")