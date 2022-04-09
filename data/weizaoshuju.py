#!/usr/bin/python3
# -*- coding:utf-8 -*-

from faker import Faker
import pandas as pd
import csv
from tqdm import tqdm, trange

fake = Faker("zh_CN")
# info = fake.profile()
# print(info.keys())
keys = [
    'job', 'company', 'ssn', 'residence', 'current_location', 'blood_group',
    'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate'
]


def dict_write_csv(data_dicts):
    filename = "./profile_infos.csv"
    with open(filename, 'a', newline='', encoding='gbk') as ff:
        fields = [
            'id', 'username', 'name', 'sex', 'address', 'mail', 'birthdate',
            'ssn', 'job', 'company', 'residence', 'current_location',
            'blood_group', 'website'
        ]
        writer = csv.DictWriter(ff, fieldnames=fields)
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            if not list(reader):
                writer.writeheader()
            writer.writerows(data_dicts)


def pandas_write_csv(datas):
    pass


# import time

# new_list = []
# for _ in tqdm(range(1000001)):
#     time.sleep(0.005)
#     info = fake.profile()
#     info.update({"id": _})
#     new_list.append(info)
#     if _ % 1000 == 0:
#         dict_write_csv(new_list)
#         new_list.clear()

# dict_write_csv([info])

filename = "E:\giteecode\python_learning_summary\profile_infos.csv"


def aa(line):
    filename = './aaa.csv'
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(line)


with open(filename, 'r', encoding='gbk') as ff:
    all_lines = ff.readlines()
    for i in all_lines:
        aa(i)
