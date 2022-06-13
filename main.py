"""
in order to create an executable out of this console script, do this:
1. install the pyinstaller python package:
    [cmd]: pip install pyinstaller
2. from the directory where you want the files to be create, run the following command:
    [cmd]: pyinstaller -F -n txt-to-typing-helper main.py
3. find the executable (.exe) under the /dist directory

https://pyinstaller.org/en/stable/usage.html#
"""

import pyautogui
import time
import os
import sys


def show_mouse_pos():
    for i in range(10):
        mouse_pos = pyautogui.position()
        # print(f'{10-i} - {mouse_pos}', end='\r')
        print(f'{10 - i} - {mouse_pos}')
        sys.stdout.flush()
        time.sleep(1)

    return mouse_pos


def main():
    print('Created by: ITG (CM) / 2022')
    print('Summary: This script helps type text file into remote connections where copy is not possible :)')
    print()
    print('Please, move the mouse pointer to screen position where typing should occur.')
    mouse_pos = show_mouse_pos()
    print(f'Mouse pointer position recorded was {mouse_pos}')
    answer = input("Enter 'Y' to confirm, any key to cancel: ")

    if answer.lower() == 'y':
        path = input('Enter absolute path of txt file to be typed: ')
        # path = "typing-data.txt"

        if os.path.isfile(path):
            pyautogui.click(mouse_pos)

            for line in open(path, "r"):
                pyautogui.typewrite(line)

    else:
        pass


if __name__ == '__main__':
    main()
