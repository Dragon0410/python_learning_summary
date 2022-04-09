#!/usr/bin/python3
# -*- coding:utf-8 -*-

from re import L


class Animal:

    def feature(self):
        print("大多数动物能自发且独立地移动")


class Human(Animal):

    def feature1(self):
        print("人类是一种有思考能力与情感的高级动物")


class Fish(Animal):

    def feature2(self):
        print("水生脊椎动物的总称")


class Mermaid(Human, Fish):

    def feature3(self):
        print("又称人鱼，传说中的生物，同时具备人及鱼的部分特征")


# alice = Mermaid()
# alice.feature()
# alice.feature1()
# alice.feature2()
# alice.feature3()


class Normal():

    def subsidy(self, income):
        self.money = income
        if self.money >= 50000:
            print("小康家庭补助金额:")
        return 5000


class Poor(Normal):

    def subsidy(self, income):
        self.money = income
        if self.money < 30000:
            print("中低收入家庭补助金额:")
            return 10000


student1 = Normal()
print(student1.subsidy(780000), '元')

student2 = Poor()
print(student2.subsidy(25000), "元")
