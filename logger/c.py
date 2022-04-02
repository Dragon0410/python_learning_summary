#!/usr/bin/python3
# Author: king
# Date: 2022-04-02 21:26:03
# Last Modified by:   King
# Last Modified time: 2022-04-02 21:26:03

from logger.logger import Log
import a, b

log = Log(log_name='name').getlog()


def main():
    log.debug("This is c file")


if __name__ == '__main__':
    main()
