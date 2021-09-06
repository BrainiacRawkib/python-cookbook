# creating data processing pipelines
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern.
    :param filepat:
    :param top:
    :return:
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    :param filename:
    :return:
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single sequence.
    :param iterators:
    :return:
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines.
    :param pattern:
    :param lines:
    :return:
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# For Example: to find all log lines that contain the word 'python'
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)

for line in pylines:
    print(line)

# this version finds the number of bytes transferred and sums the total
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes_ = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes_))
