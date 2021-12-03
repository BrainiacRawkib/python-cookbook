# Creating and unpacking archives
import shutil

shutil.make_archive('py36', 'zip', '.')
shutil.unpack_archive('py36.zip')
for i in shutil.get_archive_formats():
    print(i)

if __name__ == '__main__':
    pass
