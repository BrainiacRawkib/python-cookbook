# to support nested binary structures
import struct
from ch_06.ex_12c import StructField, Structure


class NestedStruct:
    """
    Descriptor representing a nested structure.
    """
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:self.offset+self.struct_type.struct_size]
            result = self.struct_type(data)
            # Save resulting structure back on instance to avoid
            # further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    """
    Metaclass that automatically creates StructField descriptors.
    """
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y'),
    ]


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),
        (Point, 'max'),
        ('i', 'num_polys'),
    ]


if __name__ == '__main__':
    f = open('polys.bin', 'rb')
    phead = PolyHeader.from_file(f)
    print(phead.file_code == 0x1234)
    print(phead.min_x)
    print(phead.min_y)
    print(phead.max_x)
    print(phead.max_y)
    print(phead.num_polys)
