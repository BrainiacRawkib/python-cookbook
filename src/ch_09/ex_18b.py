# The third argument may also contain other keyword arguments
import types


class Base:
    pass


class Spam(Base, debug=True, typecheck=False):
    pass


cls_dict = {}

# would translate to a new_class() call similar to this:
Spam = types.new_class('Spam', (Base,), {'debug': True, 'typecheck': False},
                       lambda ns: ns.update(cls_dict))
