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

    # NEVER DEFINE LIKE THIS.
    # only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del self.parent
        del self.children

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    # some subtle issues with garbage collection
    a = Node()
    a.add_child(Node())
    del a  # No message (not collected)
    import gc
    gc.collect()  # No message (not collected)
    import weakref
    a = Node()
    a_ref = weakref.ref(a)
    print(a_ref)
    print(a_ref())
    del a
    print(a_ref())
