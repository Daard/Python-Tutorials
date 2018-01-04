class VerySafe:
    def _get_attr(self):
        return self._x

    def _set_attr(self, x):
        assert x > 0, "non-negative"
        self._x = x

    def _del_attr(self):
        del self._x

    x = property(_get_attr, _set_attr, _del_attr)

very_safe = VerySafe()
very_safe.x = 42
print(very_safe.x)

# very_safe.x = -42
# AssertionError: non-negative

#Descriptors

class NonNegative:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        assert value > 0, "non_nagtive"
        pass

    def __delete__(self, instance):
        pass

class VerySafe:
    x = NonNegative()
    y = NonNegative()


class Descr:
    def __get__(self, instance, owner):
        print(instance, owner)

class A:
    attr = Descr()

A.attr
# None <class '__main__.A'>
A().attr
#<__main__.A object at 0x1064cbeb8> <class '__main__.A'>

class B(A):
    pass

A.attr
# None <class '__main__.A'>
B.attr
# None <class '__main__.B'>
B().attr
# <__main__.B object at 0x105b63eb8> <class '__main__.B'>

class Descr:
    def __set__(self, instance, value):
        print(instance, value)

class A:
    attr = Descr()

instance = A()
instance.attr = 42
#<__main__.A object at 0x103134f98> 42
A.attr = 44
#nothing, default behaviuor

class Descr:
    def __get__(self, instance, owner):
        print("Descr.__get__")
    def __set__(self, instance, value):
        print("Descr.__set__")

class A:
    attr = Descr()

instance = A()
instance.attr
#Descr.__get__
instance.__dict__["attr"] = 42
instance.attr
#Descr.__get__

#it is not a data descriptor
class Descr:
    def __get__(self, instance, owner):
        print("Descr.__get__")

class A:
    attr = Descr()

instance = A()
instance.attr
#Descr.__get__
instance.__dict__["attr"] = 42
instance.attr
#only 42

class Proxy:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = value

class Something:
    value = Proxy()

some = Something()
some.attr = 42
other = Something()
# print(other.attr)
#AttributeError: 'Something' object has no attribute 'attr'

#data dict
class Proxy:
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance not in self.data:
            raise AttributeError
        return self.data[instance]

    def __set__(self, instance, value):
        self.data[instance] = value

class Proxy:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return instance.__dict__[self.label]

class Something:
    attr = Proxy("attr")


# staticmethod and class method
class SomeClass:
    @staticmethod
    def do_something():
        pass

SomeClass.do_something()

class Settings:
    @classmethod
    def read_from(cls, path):
        return cls()

print(Settings.read_from("./settings.ini"))
#<__main__.Settings object at 0x1053969b0>

class staticmethod:
    def __init__(self, method):
        self._method = method

    def __get__(self, instance, owner):
        return self._method

class Something:
    @staticmethod
    def do_something():
       print("I am busy")

Something.do_something()

#Metaclasses
class Something:
    attr = 42

print(type(Something))
#<class 'type'>

#...useless abstract stuff

import abc
class Iterable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __iner__(self):
        pass

class Something(Iterable):
    pass

Something()
#TypeError: Can't instantiate abstract class Something with abstract methods __iner__


