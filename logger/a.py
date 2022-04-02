#!/usr/bin/python3
# Author: king
# Date: 2022-04-02 21:24:18
# Last Modified by:   King
# Last Modified time: 2022-04-02 21:24:18

from logger.logger import Log

log = Log(log_name=__name__).getlog()


def main():
    log.debug("This is a file")


if __name__ == '__main__':
    main()
