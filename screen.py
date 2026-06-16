import os
import shutil
import pyfiglet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Home_screen():
    clear_screen()
    terminal_width = shutil.get_terminal_size().columns
    full_border = "=" * terminal_width
    ascii_banner = pyfiglet.figlet_format(" ACS 69 ", font="slant")
    print()
    print(full_border.center(terminal_width))
    for line in ascii_banner.splitlines():
        print(line.center(terminal_width))
    print(" " * 2 + " Applied Computer Science ".center(terminal_width))
    print(full_border.center(terminal_width))
    print()

def Mission1_screen():
    clear_screen()
    terminal_width = shutil.get_terminal_size().columns
    full_border = "=" * terminal_width
    ascii_banner = pyfiglet.figlet_format(" MISSION 1 ", font="slant")
    print()
    print(full_border.center(terminal_width))
    for line in ascii_banner.splitlines():
        print(line.center(terminal_width))
    print(" " * 15 +"ภารกิจที่ 1: ถอดรหัสลับ".center(terminal_width))
    print(full_border.center(terminal_width))
    print()

def Mission2_screen():
        clear_screen()
        terminal_width = shutil.get_terminal_size().columns
        full_border = "=" * terminal_width
        ascii_banner = pyfiglet.figlet_format(" MISSION 2 ", font="slant")
        print()
        print(full_border.center(terminal_width))
        for line in ascii_banner.splitlines():
            print(line.center(terminal_width))
        print(" " * 9 +"ภารกิจที่ 2 : หา OUTPUT ให้หน่อย 😩".center(terminal_width))
        print(full_border.center(terminal_width))
        print()
