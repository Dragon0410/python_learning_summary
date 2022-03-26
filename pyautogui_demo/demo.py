#!/usr/bin/python3
# -*- encoding:utf-8 -*-
# author: king
# file: demo.py
# datetime: 2022/03/25 22:48:11

import pyautogui

def main():
    current_screen_size = pyautogui.size()
    print(f"current_screen_size: {current_screen_size}")
    current_mouse_position = pyautogui.position()
    print(f"current_mouse_position: {current_mouse_position}")


if __name__ == '__main__':
    main()









