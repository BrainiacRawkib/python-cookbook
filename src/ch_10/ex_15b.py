# To make the package something that you can distribute
# first write a setup.py
# setup.py
from distutils.core import setup


setup(name='projectname',
      version='1.0',
      author='brainiac',
      author_email='brainiac@admin.com',
      url='http://www.you.com/projectname',
      packages=['projectname', 'projectname.utils'],
)

# Next, make a file MANIFEST.in that lists various nonsource files that you want to include
# in your package:

# # MANIFEST.in
# include *.txt
# recursive-include examples *
# recursive-include Doc *

# Make sure the setup.py and MANIFEST.in files appear in the top-level directory of your
# package. Once you have done this, you should be able to make a source distribution by
# typing a command such as this:
# % bash python3 setup.py sdist
