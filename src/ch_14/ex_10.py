# Reraising the Last Exception
def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise


# Useful case:
try:
    pass
except Exception as e:
    # Process exception information in some way
    # propagate the exception
    raise

if __name__ == '__main__':
    example()
