import pickle

f = open('pickled', 'wb')

pickle.dump([1, 2, 3, 4, 5, 6], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()

f = open('pickled', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

if __name__ == '__main__':
    pass
