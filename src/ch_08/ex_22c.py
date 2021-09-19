# to avoid RecursionError: maximum recursion depth exceeded
from ch_08.ex_22b import *


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        print('Add:', node)
        lhs = yield node.left
        print('left=', lhs)
        rhs = yield node.right
        print('right=', rhs)
        yield lhs + rhs

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield node.operand)


if __name__ == '__main__':
    a = Number(0)
    for n in range(1, 100000):
        a = Add(a, Number(n))

    e = Evaluator()
    print(e.visit(a))
