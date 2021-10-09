# the ast module can be used to compile python source code into
# an abstract syntax tree
import ast


ex = ast.parse('2 + 3 * 4 + x', mode='eval')
print(ex)
print(ast.dump(ex))

top = ast.parse('for i in range(10): print(i)', mode='exec')
print(top)
print(ast.dump(top))

if __name__ == '__main__':
    pass
