#!/usr/bin/python3
# Author: king
# Date: 2022-03-31 22:01:58
# Last Modified by:   mikey.zhaopeng
# Last Modified time: 2022-03-31 22:01:58

# 1. 输入一个字符串，如果有重复的字符，就返回最大重复的个数，如果有2个重复值，就返回2，说明2个重复最大值。不区分大小写
# 示例1:
# text = "abcd"   => 没有重复值
# text = "abdacdd" => 重复值是d 重复3次
# text = "AbsdDa"  => 重复值是a,d 重复值2

# 2. 输入一段话，重复数，如果两个相邻的单词重复，重复数+1， 连续2个或者2个以上重复，+ 1
# 示例2
# "Gog dog dog cat" => 1
# "dog Dog dog dog doG" => 1
# "dog cat mouse" => 0
# "dog dog cat cat mouse" => 2

import random


def check_text(text):
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


def check_text2(text):
    from collections import Counter
    print(text)
    if len(text.lower()) == len(set(text.lower())):
        print("没有重复值")
    else:
        new_dict = dict(Counter(text))
        # sorted_list = sorted(new_dict.items(),
        #  key=lambda k: k[1],
        #  reverse=True)
        # print("倒向排序后,变成列表:", sorted_list)
        keys = list(new_dict.keys())
        values = list(new_dict.values())
        max_values = max(values)
        if values.count(max_values) > 1:
            # 如果最大值的数量大于 1
            max_value_index_list = [
                index for index, value in enumerate(values)
                if value == max_values
            ]
            keys = [keys[index] for index in max_value_index_list]
            print(f"重复值是: {','.join(keys)}, 重复次数是: {max_values}")

        else:
            max_values_index = values.index(max_values)
            key = keys[max_values_index]
            print(f"重复值是: {key}, 重复次数是: {max_values}")


def check_text3(text):
    from collections import Counter
    print(text)
    if len(text.lower()) == len(set(text.lower())):
        print("没有重复值")
    else:
        new_dict = dict(Counter(text))
        repeat_max_value = max(new_dict.values())
        repeat_str_list = [
            k for k, v in new_dict.items() if v == repeat_max_value
        ]
        print(f"重复值是: {','.join(repeat_str_list)}, 重复次数是: {repeat_max_value}")


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
    int_str_i = [str(i) for i in range(10)]
    str0 = str_str_A + str_str_a + int_str_i
    text = "".join(random.choice(str0) for _ in range(100))
    check_text3(text)


def main1():
    text = "dog dog dog cat cat"
    text1 = "dog Dog dog dog dog"
    check_ci(text)


if __name__ == '__main__':
    main()
