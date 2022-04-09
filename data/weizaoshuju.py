#!/usr/bin/python3
# -*- coding:utf-8 -*-

from faker import Faker
import pandas as pd
import csv
import os
from tqdm import tqdm
import argparse

fake = Faker("zh_CN")


def args_parse():
    parse = argparse.ArgumentParser(description="参数")
    parse.add_argument("--count", "-c", default=1000, help="数据总数")
    parse.add_argument("--save_filename",
                       "-s",
                       default="./default_data.csv",
                       help="数据保存路径")
    parse.add_argument("--interval",
                       "-i",
                       default=100,
                       help="分批次保存, 减小内存开销,和IO次数做平衡")
    parse.add_argument("--header", "-header", help="数据表头")
    args, _ = parse.parse_known_args()
    return args


class Falsification_Of_Personal_Data():
    """
    伪造个人数据信息。 数据包含 job, company, ssn, residence, current_location, blood_group,
    website, username, name, sex, address, mail, birthdate.
    count: 是生成数据的总条数。
    """

    def __init__(self,
                 count=1000,
                 save_filename='./default_data.csv',
                 interval=100,
                 header=None):
        self.count = count
        self.save_filename = save_filename
        self.interval = interval
        self.data_list = []
        default_header = [
            'id', 'username', 'name', 'sex', 'address', 'mail', 'birthdate',
            'ssn', 'job', 'company', 'residence', 'current_location',
            'blood_group', 'website'
        ]
        self.header = default_header if header is None else header
        self.run()

    def run(self):
        for i in tqdm(range(1, self.count + 1)):
            userinfo = fake.profile()
            userinfo.update({"id": i})  # 增加 ID 字段
            self.data_list.append(userinfo)

            if len(self.data_list) % self.interval == 0:
                data_obj = pd.DataFrame(self.data_list)
                # 如果文件不存在，创建新文件并写入表头
                if not os.path.exists(self.save_filename):
                    data_obj.to_csv(self.save_filename,
                                    mode='w',
                                    index=False,
                                    header=True)
                    self.data_list.clear()  # 情况列表
                # 文件存在，检查下表头是否存在或者一致
                try:
                    # 读取已经存在文件的表头
                    datas = pd.read_csv(self.save_filename)
                    header0 = list(datas.columns)
                    # 表头一样的话，就不再写入表头
                    if sorted(self.header) == sorted(header0):
                        data_obj.to_csv(self.save_filename,
                                        mode='a',
                                        index=False,
                                        header=False)
                        self.data_list.clear()
                except pd.errors.EmptyDataError as e:
                    print(f"{self.save_filename} 是空文件，没有发现表头。")
                    # 重新写入表头
                    data_obj.to_csv(self.save_filename,
                                    mode='a',
                                    index=False,
                                    header=True)
                    self.data_list.clear()

        data_obj = pd.DataFrame(self.data_list)
        data_obj.to_csv(self.save_filename,
                        mode='a',
                        index=False,
                        header=False)


def dict_write_csv(data_dicts: list):
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


def main():
    args = args_parse()
    count = args.count
    save_filename = args.save_filename
    interval = args.interval
    header = args.header

    Falsification_Of_Personal_Data(count, save_filename, interval, header)


if __name__ == "__main__":
    main()
