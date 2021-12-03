# handling errors during copying
import shutil

try:
    src = './src'
    dst = './dst'
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        # src is source name
        # dst is destination name
        # msg is error message from exception
        print(dst, src, msg)  # If you supply the ignore_dangling_symlinks=True keyword argument, then copytree()
        # will ignore dangling symlinks.
