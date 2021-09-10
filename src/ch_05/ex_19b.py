# alternative way of creating temporary files and direcories
import tempfile

print(tempfile.mkstemp())
print(tempfile.mkdtemp())
print(tempfile.gettempdir())

# f = tempfile.NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
# print(f.name)

if __name__ == '__main__':
    pass
