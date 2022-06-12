import pyautogui
import time
import os, sys


def show_mouse_pos():
    for i in range(10):
        mouse_pos = pyautogui.position()
        # print(f'{10-i} - {mouse_pos}', end='\r')
        print(f'{10-i} - {mouse_pos}')
        sys.stdout.flush()
        time.sleep(1)

    return mouse_pos


def main():
    print('please, move mouse to screen position where typing should occur.')
    mouse_pos = show_mouse_pos()
    print(f'mouse position recorded was {mouse_pos}')
    answer = input("enter 'Y' to confirm, 'N' to cancel: ")

    if answer.lower() == 'y':
        path = input('enter path of txt file to be typed: ')
        # path = "typing-data.txt"

        if os.path.isfile(path):
            pyautogui.click(mouse_pos)

            for line in open(path, "r"):
                pyautogui.typewrite(line)

    else:
        pass


if __name__ == '__main__':
    main()
