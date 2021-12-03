# getting the terminal size
import os

sz = os.get_terminal_size()

if __name__ == '__main__':
    print(sz)
    print(sz.columns)
    print(sz.lines)
