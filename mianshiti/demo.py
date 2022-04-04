#!/usr/bin/python3
# Author: king
# Date: 2022-04-04 17:42:12
# Last Modified by:   King
# Last Modified time: 2022-04-04 17:42:12

list_demo = [1, 4, 6, 11, 54, 78, 3, 1, 257, 9]


def replace_value(list_args):
    new_list = []
    for i in list_args:
        if i < 10:
            new_list.append(10)
        else:
            new_list.append(i)
    print('==', new_list)


def main1():
    print(list_demo)
    replace_value(list_demo)


def main():
    """2个字段合并，如果有相同字段，该值相加
    """
    a = {"age": 10, "name": "wang", "source": 60, "kehu": "yuwen"}
    b = {
        "age": 10,
        "name": "zhang",
        "source": 60,
        "kehu": "shuxue",
        "category": "tiyu"
    }

    def dict_add(a, b):
        for k, v in b.items():
            if k in a.keys():
                a[k] += v
                print(k, a[k])
            a[k] = v
        print(a)

    dict_add(a, b)


def main2():
    """
    输入重复次数，返回该数组中的元素
    """

    def query_index(n, lista):
        new_dict = {i: lista.count(i) for i in lista}
        print(new_dict)
        for k, v in new_dict.items():
            if v == n:
                print(f"出现{n}次的元素: {k}")

    a_list = [1, 2, 3, 5, "a", "a"]
    print(a_list.count('a'))
    query_index(2, a_list)


def main3():
    """现在给定非负整数数组，你最初位于数组第一位，数组中的元素代表在该位置可以跳跃的最大长度，判断你是否可以
    到达最后一个位置。示例
    [2,3,1,1,4] 可以从第0个元素跳1步到第一个元素，再从第1个元素跳3步到最后一个元素，返回True
    [3,2,1,0,4] 无论如何选取路线，总会跳到第3个元素0的位置，该元素最大跳跃距离0，无法到达最后一个位置，返回False
    对于单元素数组，如[0], 返回True
    不考虑空数组
    Returns:
        _type_: _description_
    """
    a = [2, 3, 1, 1, 4, 3]
    # a = [3, 2, 1, 0, 4]
    b = a[1:]
    index = 1  # a 的索引
    value = 0
    while 1:
        value = a[index]
        setup = value  # 这是为了避免混淆  更换下变量
        index += setup
        print(f"a当前的索引值是: {index}, 值是: {value}")
        if setup == 0:
            print(f"False {index} index is 0")
            return False
        if index + 1 == len(a):
            print("True")
            return True
        elif index + 1 > len(a):
            print(f"False {index} 超过index")
            return False


if __name__ == '__main__':
    main3()
