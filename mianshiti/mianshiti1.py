#!/usr/bin/python3
# Author: king
# Date: 2022-03-31 22:01:58
# Last Modified by:   mikey.zhaopeng
# Last Modified time: 2022-03-31 22:01:58

# 输入一个字符串，如果有重复的字符，就返回重复的个数，如果有2个重复值，就返回2，说明2个重复最大值。不区分大小写
# 输入一段话，重复数，如果两个相邻的单词重复，重复数+1， 连续2个或者2个以上重复，+ 1
import random


def chech_text(text):
    if len(text.lower()) == len(set(text.lower())):
        print("没有重复值")
    else:
        new_dict = {i: text.lower().count(i) for i in text.lower()}
        keys = list(new_dict.keys())
        values = list(new_dict.values())
        a = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
        print('排序:', a)
        max_value_index = values.index(max(values))
        if values.count(max(values)) == 1:
            print(f"重复值是: {keys[max_value_index]}, 重复次数是: {max(values)}")
        else:
            max_values_index = [
                index for index, value in enumerate(values)
                if value == max(values)
            ]
            chongfuzhi = [keys[i] for i in max_values_index]
            print(f"重复值是: {','.join(chongfuzhi)}, 重复次数是: {max(values)}")


def check_ci(text):
    s = 0
    lista = text.lower().split()
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            s += 1
    print(s)

def main():
    str_str_A = [chr(i) for i in range(65, 91)]
    str_str_a = [chr(i).lower() for i in range(65, 91)]
    str0 = str_str_A + str_str_a
    count_len = 100
    text = ""
    for _ in range(count_len):
        text += random.choice(str0)

    chech_text(text)


def main1():
    text = "dog dog dog cat cat"
    text1 = "dog Dog dog dog dog"
    check_ci(text)


if __name__ == '__main__':
    main1()
