
class Counter:
    """I count."""
    def __init__(self, initial=0):
        self.value = initial

    def increment(self):
        self.value += 1

    def get(self):
        return self.value


c = Counter(42)
c.increment()
print(c.get()) # 43

#atributes

class Counter:
    all_counters = []

    def __init__(self, initial=0):
        Counter.all_counters.append(self)

Counter.some_ther_attributes = 42

#private anr protected
class Noop:
    some_attribute = 42
    _internal_Attribute = []

from collections import deque
class MemorizzingDict(dict):
    history = deque(maxlen=10)

    def set(self, key, value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return self.history

d = MemorizzingDict({'foo':42})
d.set('baz', 100500)
print(d.get_history()) #deque(['baz'], maxlen=10)

d = MemorizzingDict()
d.set('boo', 500100)
print(d.get_history()) #deque(['baz', 'boo'], maxlen=10)

#Init atrributes of classes and objects

class Noop:
    """I do nothing"""

print(Noop.__doc__, Noop.__name__, Noop.__module__, Noop.__bases__)
#I do nothing Noop __main__ (<class 'object'>,)
noop = Noop()
print(noop.__class__, noop.__dict__)
#<class '__main__.Noop'> {}
noop.some_att = 42
print(noop.__dict__)
#{'some_att': 42}
#adding, deleting, updating attributes are operations with DICTIONAY

noop.__dict__['other_att'] = 100500
print(noop.other_att)
#100500
print(noop.__dict__)
#{'some_att': 42, 'other_att': 100500}
del noop.other_att
print(noop.__dict__)
#{'some_att': 42}

#__slots__

class Noop:
    __slots__ = ['some_att']

noop = Noop()
noop.some_att = 42
print(noop.some_att)
#42

# noop.some_other_att = 100500 <--- ERROR !!!!

#class with __slots__ take les memory, becouse they don't have __dict__

#Bound and unbound methods
class SomeClass:
    def do_something(self):
        print('Doing something')

SomeClass().do_something() #bound
#Doing something

SomeClass.do_something #unbound
instance = SomeClass()
SomeClass.do_something(instance) #instance must to be set
#Doing something

from os.path import dirname
#Properties
class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "Path({})".format(self.current)

    @property
    def parent(self):
        return Path(dirname(self.current))

p = Path(".DS/_5statistics.py")
print(p.parent)
#Path(.DS)

class BigDataModlel:
    def __init__(self):
        self._params = []

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, new_params):
        assert all(map(lambda p:p>0, new_params))
        self._params=new_params

    @params.deleter
    def params(self):
        del self._params

model = BigDataModlel()
model.params = [0.1, 0.5, 0.9]
print(model.params)

#inheritance


class Counter:
    def __init__(self, initial=0):
        self.value = initial


class OtherCounter(Counter):
    def get(self):
        return self.value

c = OtherCounter()
print(c.get()) #0
print(c.value) #0

#overiding and super
class Counter:
    all_counters = []

    def __init__(self, initial=0):
        self.__class__.all_counters.append(self)
        self.value = initial

class OtherCounter(Counter):
    def __init__(self, initial=0):
        super().__init__(initial)

oc = OtherCounter()
print(vars(oc))
#{'value': 0}

#isintance

class A:
    pass

class B(A):
    pass

print(isinstance(B(), A)) #True

class C:
    pass

print(isinstance(B(), (A, C)))
#True

print(isinstance(B(), A) or isinstance(B(), C))

print(issubclass(B, A))
#True
print(issubclass(B, (C, A)))
#True

#Python has multyinheritance

#Mixins

class ThreadSafeMixin:
    get_lock = ...

    def increment(self):
        with self.get_lock():
            super().increment()

    def get(self):
        with self.get_lock:
            return super().get()

class ThreadSafeCounter(ThreadSafeMixin, Counter):
    pass

#Decorators

def thread_safe(cls):
    orig_increment = cls.increment
    orig_get = cls.get

    def increment(self):
        with self.get_lock():
            orig_increment(self)

    def get(self):
        with self.get_lock():
            return orig_get(self)

    cls.get_lock= ...
    cls.increment = increment
    cls.get = get
    return cls

# Singleton
import functools

def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return inner

@singleton
class Noop:
    """I do nothing at all."""

print(id(Noop()))
# 4425304440
print(id(Noop()))
# 4425304440

# Deprecated
import warnings
def deprecated(cls):
    origin_init = cls.__init__

    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        warnings.warn(cls.__name__ + 'is deprecated', category=DeprecationWarning)
        origin_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@deprecated
class Counter:
    def __init__(self, initial=0):
        self.value = initial

c = Counter()


#Magic methods

class trace:

    def __init__(self, initial=0):
        self.value = initial

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs)
            return func(*args, **kwargs)
        return inner

@trace(12)
def identity(x):
    return x

print(identity(42))
# identity (42,) {}
# 42

#Other

#__repr__
#__str__
#__hash__
#__format__






