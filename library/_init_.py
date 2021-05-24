from . import dior # this imports the math.py file from within our package

# this is printed when the library is imported
print("This is a dior bag")

# when you do 'from library import *`, __all__ is the list of objects imported/introduced to the namespace
__all__ = [dior.func]
