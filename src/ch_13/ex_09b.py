# functions that prints out all of the files that have a recent modification time
import os
import time


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            full_path = os.path.join(path, name)
            if os.path.exists(full_path):
                mtime = os.path.getmtime(full_path)
                if mtime > (now - seconds):
                    print(full_path)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} dir seconds')
        raise SystemExit(1)

    modified_within(sys.argv[1], float(sys.argv[2]))
