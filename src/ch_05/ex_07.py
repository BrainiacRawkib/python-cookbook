# reading and writing compressed datafiles
import bz2
import gzip

# gzip compression
# lower level compression offer better performance but not as much compression
# the default compression level is 9
with gzip.open('gz_compressed.gz', 'wt', compresslevel=5) as f:
    gz_text = 'this file is compressed with gzip algorithm.'
    gz_comp = f.write(gz_text)

# bz2 compression
with bz2.open('bz2_compressed.bz2', 'wt') as f:
    bz2_text = 'this file is compressed with bz2 algorithm.'
    bz2_comp = f.write(bz2_text)

# read compressed file
with gzip.open('gz_compressed.gz', 'rt') as f:
    gzip_text = f.read()
    print(gzip_text)

# bz2 compressed file
with bz2.open('bz2_compressed.bz2', 'rt') as f:
    bz_text = f.read()
    print(bz_text)

# performing operation using gzip on an existing file opened
f = open('compressed.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
    print(text)

if __name__ == '__main__':
    pass
