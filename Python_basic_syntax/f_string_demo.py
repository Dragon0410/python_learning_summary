#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 93207
# description: 
# datetime: 2022/3/25 20:21
# name: f_string_demo

def main():
    # 简单的使用
    name = "lele"
    age = 31
    address = "HeNan"

    desc = f"Hello, My name is {name}, and {age} year. from {address}"
    desc1 = "Hello, My name is {0}, and {1} year. from {2}".format(name, age, address)
    desc2 = "Hello, My name is {name}, and {age} year. from {address}".format(name=name, age=age, address=address)
    desc3 = "Hello, My name is %s, and %d year. from %s" % (name, age, address)
    print(desc)
    print(desc1)
    print(desc2)
    print(desc3)

    number = 123.456
    print(number)
    print(f"number is {number:9.2f}")
    print(f"number is {number:09.2f}")
    print(f"number is {number:8.2e}")
    print(f"number is {number:8.2%}")

    number1 = 1234567890
    print(number1)
    print(f"number1 is {number1:.2f}")
    print(f"number1 is {number1:,.2f}")

if __name__ == "__main__":
    main()
