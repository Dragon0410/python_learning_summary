#!/usr/bin/python3
# Author: king
# Date: 2022-04-02 18:53:55
# Last Modified by:   King
# Last Modified time: 2022-04-02 18:53:55

import logging
import datetime
import os


class Log():

    def __init__(
        self,
        log_name=None,
        log_path="",
        fmt="[%(asctime)s]-%(filename)s:%(lineno)d-%(funcName)s-[%(levelname)s]: %(message)s",
    ) -> None:
        self.logger = logging.getLogger(log_name)
        # print(logger.handlers)  # 观察多次引入的logger, 出现的handlers
        self.logger.handlers.clear()  # 如果不加这个的话,多项引入会出现重复记录log

        if not log_path:
            timestr = datetime.datetime.now().strftime("%Y%m%d")
            current_directory = os.path.abspath(__file__)
            log_path = os.path.join(current_directory, "../logs")
            if not os.path.exists(log_path):
                os.makedirs(log_path)

        self.logname = os.path.join(log_path, f"{timestr}.log")
        self.logger.setLevel("DEBUG")
        self.formatter = logging.Formatter(fmt)
        self.file_handler()
        self.stream_handler()

    def file_handler(self):
        fh = logging.FileHandler(self.logname, "a", encoding="utf-8")
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        fh.close()

    def stream_handler(self):
        ch = logging.StreamHandler()
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


def main():
    log = Log().getlog()
    text = "This is a test program"
    log.debug(text)


if __name__ == '__main__':
    main()
