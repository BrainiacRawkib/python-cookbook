# serializing python objects
import pickle

data = '{"key": value}'

# dump python objects to a file
f = open('pickle', 'wb')
pickle.dump(data, f)

# dump python objects to a string
s = pickle.dumps(data)

# restore from a file
f2 = open('pickle', 'rb')
data2 = pickle.load(f2)

# restore from a string
data_ = pickle.loads(s)

if __name__ == '__main__':
    pass
