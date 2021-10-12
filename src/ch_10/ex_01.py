# making a hierarchical package of modules

"""
graphics/
    __init__.py
    primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py
"""

"""
The purpose of the __init__.py files is to include optional initialization code
that runs as different levels of a package are encountered. 
For example, if you have the statement import graphics, the file graphics/__init__.py 
will be imported and form the contents of the graphics namespace. For an import such 
as import graphics.formats.jpg, the files graphics/__init__.py and graphics/formats/__init__.py 
will both be imported prior to the final import of the graphics/formats/jpg.py file.
More often that not, it’s fine to just leave the __init__.py files empty.
However, there are certain situations where they might include code. 
For example, an __init__.py file can be used to automatically load submodules like this: 
"""
# from . import jpg
# from . import png
