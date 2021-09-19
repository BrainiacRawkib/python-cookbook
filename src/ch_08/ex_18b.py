from collections import defaultdict, OrderedDict
from ch_08.ex_18 import LoggedMappingMixin, StringKeysMappingMixin, SetOnceMappingMixin


class LoggedDict(LoggedMappingMixin, dict):
    pass


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


class StringOrderedDict(StringKeysMappingMixin, SetOnceMappingMixin, OrderedDict):
    pass


if __name__ == '__main__':
    d = LoggedDict()
    d['x'] = 23
    print(d['x'])
    d = SetOnceDefaultDict(list)
    d['x'].append(2)
    d['y'].append(4)
    d['x'].append(6)
    d['y'].append(20)
    d['z'].append(6)
    print(d)
    # d['x'] = 34  # KeyError: 'x already set'
    d = StringOrderedDict()
    # d[4] = 34  # TypeError: Keys must be strings
    d['x'] = 'list'
    # d['x'] = 'set'  # KeyError: 'x already set'
    print(d)
