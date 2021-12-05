# Inheriting and Overriding __init__() method directly from Exception
class CustomError(Exception):
    def __init__(self, message, status):
        super(CustomError, self).__init__(message, status)
        self.message = message
        self.status = status


try:
    raise RuntimeError('It Failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)

if __name__ == '__main__':
    pass
