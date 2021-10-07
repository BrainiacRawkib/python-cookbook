# support for metaclasses
import types

cls_dict = {}
Stock = type('Stock', (), cls_dict)  # this approach skips through the invocation
# of the metaclass __prepare__() method.

# By using types.new_class() you ensure that all of the necessary
# initialization steps get carried out.

# if you want to carry out the preparation step, use types.prepare_class()
metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})
# this finds the appropriate metaclass and invokes its __prepare__() method.
# The metaclass, remaining keyword arguments, and prepared namespace are then returned.

print(metaclass)
print(kwargs)
print(ns)

if __name__ == '__main__':
    pass
