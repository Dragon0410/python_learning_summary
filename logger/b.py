#!/usr/bin/python3
# Author: king
# Date: 2022-04-02 21:25:08
# Last Modified by:   King
# Last Modified time: 2022-04-02 21:25:08

from logger.logger import Log
import a

log = Log(log_name='name').getlog()


def main():
    log.debug("This is b file")


if __name__ == '__main__':
    main()
