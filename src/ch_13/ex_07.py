# copying or moving files and directories
import shutil

src = './src'
dst = './dst'

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy symbolic link
shutil.copy2(src, dst, follow_symlinks=False)
#
#
# def ignore_pyc_files(dirname, filenames):
#     return [name in filenames if name.endswith('.pyc')]

# Preserve symbolic link in copied directories
shutil.copytree(src, dst, symlinks=True, ignore=shutil.ignore_patterns('*~', '*.pyc'))

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

if __name__ == '__main__':
    pass
