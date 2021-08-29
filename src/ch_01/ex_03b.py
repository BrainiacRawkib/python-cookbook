from collections import deque


q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)


if __name__ == '__main__':
    print(q)
    q.append(4); q.append(5)
    print(q)
    q.appendleft(89)
    print(q)
    print(q.popleft())
    print(q)
