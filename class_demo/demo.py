#!/usr/bin/python3
# -*- coding:utf-8 -*-

# User: king
# FileName:
# DateTime: 2022/4/7 {TIME}
# Editor: PyCharm
# Project: python_learning_summary

# # 继承是面向对象程序设计的重要概念之一。
# 通过继承，我们可以从既有的类上衍生出新的类。如果程序的需求为仅修改或删除某项功能，此时不需要将该类的成员数据及成员函数重新写一遍，只需要“继承”原先已定义好的类就可以产生新的类了。
# 继承是指将现有类的属性和行为，经过修改或重写（Override）之后，就可产生出拥有新功能的类，这样可以大幅提升程序代码的可重用性（Reusability）。
# 事实上，继承除了可重复利用之前开发过的类之外，最大的优势在于能够维持对象封装的特性。因为继承时不易改变已经设计完整的类，这样可以减少继承时类设计上的错误发生

# 单继承（Single Inheritance），即派生类直接继承单独一个基类的成员数据与成员函数。在 Python 中使用继承机制


class MobilePhone:

    def touch(self):
        print("我能提供屏幕触控操作功能")


class HTC(MobilePhone):

    def touch(self):
        MobilePhone.touch(self)
        print("我也能提供")


# ull = HTC()
# ull.touch()


class Weekday:

    def display(self, pay):
        self.price = pay
        print(f"欢迎来购物， 购买总金额: {self.price:.2f} 元")


class Holiday(Weekday):

    def display(self, pay):
        super().display(pay)
        if self.price >= 15000:
            self.price *= 0.8
        else:
            self.price
        print(f"八折 {self.price:.2f} 元")


# moday = Weekday()
# moday.display(25000)

# h = Holiday()
# h.display(18000)


class Animal():

    def __init__(self):
        print("我属于动物类")


class Human(Animal):

    def __init__(self, name):
        super().__init__()
        print(f"我{name}也属于人类")


# man = Human("黄种人")


class Tom:

    def __init__(self) -> None:
        self.height1 = 178


class Andy(Tom):

    def __init__(self) -> None:
        self.height2 = 180
        super().__init__()


class Michael(Andy):

    def __init__(self) -> None:
        self.height3 = 185
        super().__init__()

    def display(self):
        print(f"父亲Tom身高: {self.height1}")
        print(f"兄弟Andy身高: {self.height2}")
        print(f"自己Michael身高: {self.height3}")


# m1 = Michael()
# m1.display()