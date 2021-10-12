# making a directory or zip file runnable as a main script

"""
myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py
"""

"""
If __main__.py is present, you can simply run the Python interpreter on the top-level
directory like this:

bash % python3 myapplication

The interpreter will execute the __main__.py file as the main program
"""

"""
This technique also works if you package all of your code up into a zip file. For example:

bash % ls
spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py
bash % python3 myapp.zip
... output from __main__.py ...
"""