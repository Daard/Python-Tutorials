#Exceptions

def something_dangerous():
    pass

try:
    something_dangerous()
except(ValueError, ArithmeticError):
    pass
except TypeError as e:
    pass

try:
    something_dangerous()
except Exception as e:
    try:
        something_dangerous()
    except type(e): # можно и так
        pass

try:
    1 + '42'
except TypeError as e:
    pass
#there is BaseException, but we need to handle only children of Exception

assert 2 + 2 == 4, ('Math', 'still', 'works')
# File "/Users/daard/Documents/CarND/tutorials/Python/7Exceptions.py", line 27, in <module>
#     assert 2 + 2 == 5, ('Math', 'still', 'works')
# AssertionError: ('Math', 'still', 'works')

# ImportError: No module named 'foobar'
# NameError: name 'foobar; ias not defined
# AttributeError: 'object object has no attribute 'foobar'
# KeyError: 'there is not such key in the dictionary
# IndexError: list index out of range
# ValueError: any other error
# TypeError: can't conacat byte to str

# New exceptions
class CSCException(Exception):
    pass

class TestFailure(CSCException):
    def __str__(self):
        return 'lecture test failed'

try:
    1 + '42'
except Exception as e:
    caught = e

print(caught.args) #("unsupported operand type(s) for +: 'int' and 'str'",)
print(caught.__traceback__) #<traceback object at 0x107c2acc8>

try:
    raise TypeError('type mismatch')
except TypeError as e:
    pass

try:
    {}['foobar']
except KeyError as e:
    try:
        raise RuntimeError('Oooops') from e
    except RuntimeError:
        pass

def do_something(handle):
    pass

try:
    handle = open('example.txt', 'wt')
    try:
        do_something(handle)
    finally:
        handle.close()
except IOError as e:
    print(e)


####
####Context managers
####
def acquire_resource():
    pass

def release_resource(r):
    pass

r = acquire_resource()
try:
    do_something(r)
finally:
    release_resource(r)

#it equals

# with acquire_resourse() as r:
#     do_something(r)
#
def acquire_other_resource():
    pass
#
# with acquire_resourse() as r, acquire_other_resource() as other:
#     do_something(r, other)

#with equals to
import sys
try:
    manager = acquire_resource()
    r = manager.__enter__()
    try:
        do_something(r)
    finally:
        exc_type, exc_value, tb = sys.exc_info()
        supress = manager.__exit__(exc_type, exc_value, tb)
        if exc_value is not None and not supress:
            raise exc_value
except AttributeError as e:
    pass

##SAMPLES

from functools import partial
class opened:
    def __init__(self, path, *args, **kwargs):
        self.opener = partial(open, *args, **kwargs)

    def __enter__(self):
        self.handle = self.opener()
        return self.handle

    def __exit__(self, *exc_info):
        self.handle.close()
        del self.handle

try:
    with opened('example.txt', mode='rt') as handle:
        pass
except TypeError as e:
    pass


#Synchronized
import threading
class synchronized:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock.release()

with synchronized():
    do_something(r)

#cd
import os
class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_cwd)

print(os.getcwd())
#/Users/daard/Documents/CarND/tutorials/Python
with cd('./..'):
    print(os.getcwd())
#/Users/daard/Documents/CarND/tutorials


#CONTEXTLIB
from contextlib import closing
from urllib.request import urlopen
url = 'http://comscinter.ru'
with closing(urlopen(url)) as page:
    do_something(page)

from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove('example.txt')

#### and more:
# closing
# redirect_stdout
# suppress
# ContextDecorator
# ExitStack


