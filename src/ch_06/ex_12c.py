# using metaprogramming
import struct
from ch_06.ex_12b import StructField


class StructureMeta(type):
    """
    Metaclass that automatically creates StructField descriptors.
    """
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_cls(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


if __name__ == '__main__':
    f = open('polys.bin', 'rb')
    phead = PolyHeader.from_cls(f)
    print(phead.file_code == 0x1234)
    print(phead.min_x)
    print(phead.min_y)
    print(phead.max_x)
    print(phead.max_y)
    print(phead.num_polys)
