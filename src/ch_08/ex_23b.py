# class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    # some subtle issues with garbage collection
    a = Data()
    del a  # Immediately deleted
    a = Node()
    del a  # Immediately deleted
    a = Node()
    a.add_child(Node())
    del a  # Not immediately deleted (no message)
