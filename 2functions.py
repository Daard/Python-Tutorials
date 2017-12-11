# Documentation

def foo():
    "I return 42."
    return 42

print(foo.__doc__)
print(help(foo))


#Named params
def min(x, y):
    return x if x <= y else y

print(min(-5, 12))
print(min(x=-5, y=12))
print(min(y=12, x=-5))

#Packig - unpacking
def min(*args):
    res = float("inf")
    for arg in args:
        if arg < res:
            res = arg
    return res

print(min(-5, 12, 13))
print(min())

def min(x, *args):
    res = float("inf")
    # unpacking creates tuples
    all = (x, ) + args
    for arg in all:
        if arg < res:
            res = arg
    return res

print(min(-5, 12, 13))
print(min(-3))
print(min(*[-5, 12, 13]))

def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    # unpacking creates tuples
    for arg in (first, ) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)

print(bounded_min(-5, 12, 13, lo=0, hi=255))


#details Key args
def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

xs = [1, 1, 2, 3]
#Func does not have defaults
print(unique(xs))
#[1, 2, 3]
#Now func is already has defaults
print(unique(xs))
#[]
print(unique.__defaults__)
#({1, 2 ,3}, )

#Right init
def unique(iterable, seen=None):
    seen = set(seen or []) # None is false
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

xs = [1, 1, 2 ,3]
print(unique(xs))
#[1, 2, 3]
print(unique(xs))
#[1, 2, 3]

#Unpacking key ars
def runner(cmd, **kwargs):
    if kwargs.get('verbose', True):
        print('Loggin enabled')

runner('mysql', limit=42)
#Loggin enabled
options = {'verbose':False}
runner('mysql', **options)
#Nothing

def flatten(xs, depth=None):
    pass

flatten([1, [2], 3], depth=1)
flatten([1, [2], 3], 1)
def flatten(xs, *, depth=None):
    pass
#If there are unknow number of args you need to set key args
flatten([1, [2], 3], depth=1)

#Initting
x = 3
y = 4
#swap
x, y = y, x
#the same
x, y = (y, x)
x, y, z = [1, 2, 3]
x, y, z = {1, 2, 3} #unrodered!
x, y, z = 'xyz'
rectangle = (0, 0), (4, 4)
(x1, y1), (x2, y2) = rectangle

#New unpacking in P3
first, *rest = range(1, 5)
print(first, rest)
#1 [2, 3, 4]
first, *rest, last = range(1, 5)
print(first, rest, last)
#1 [2, 3] 4
for a, *b in [range(4), range(2)]:
    print(b)
#[1, 2, 3]
#[1]
# Init works form left to right
x, (x, y) = 1, (2, 3)
print(x)
#2

#In Python 3 unpacking was extened
def f(*args, **kwargs):
    print(args, kwargs)

print(f(1, 2, *[3, 4], *[5], foo='foo', **{'baz':42}, boo=24))
#(1, 2, 3, 4, 5) {'foo': 'foo', 'baz': 42, 'boo': 24}

#SCOPES
def wrapper():
    def identify(x):
        return x
    return identify

f = wrapper()
print(f(42))
#42

def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first, ) + args:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)
    return inner

bounded_min = make_min(lo=0, hi=255)
print(bounded_min(-5, 12, 13))

min #builtin
min = 42 #global
def f(*args):
    min = 2
    def g(): # enclosing
        min = 4
        print(min)

# LEGB rule

def f():
    print(i)

for i in range(4):
    f()
# 0
# 1
# 2
# 3

#LEGB does not work with initting

min = 42
def f():
    global min
    #+= always create in locale scope, so we need to use global literal
    min += 1
    return min


def cell(value=None):
    def get():
        return value
    def set(update):
        nonlocal value
        value = update
    return get, set

get, set = cell()
set(42)
get()
#42

#You should always use nonlocal if you need global


#FUNCTIONAL PROGRAMMING

print(list(map(lambda  x: x ** 2, range(4))))

print(list(filter(lambda x : x % 2 != 0, range(10))))
xs = [0, None, [], {}, "", 42]
#we can pass None and we will be use default value of item
print(list(filter(None, xs)))
# [42]
print(list(zip('abs', range(3), [42j, 42j, 42j])))
# [('a', 0, 42j), ('b', 1, 42j), ('s', 2, 42j)]

#Generators

print([x ** 2 for x in range(10) if x % 2 == 1])
# [1, 9, 25, 49, 81]
#possible replacement
print(list(map(lambda  x : x ** 2, filter(lambda  x : x % 2 ==1, range(10)))))
# [1, 9, 25, 49, 81]
#Nested
nested = [range(5), range(8, 10)]
print([x for xs in nested for x in xs])
# [0, 1, 2, 3, 4, 8, 9]
res = []
for xs in nested:
    for x in xs:
        res.append(x)
print(res)
# [0, 1, 2, 3, 4, 8, 9]

date = {'year':2014, 'month':'September', 'day':''}
print({k : v for k, v in date.items() if v})
# {'year': 2014, 'month': 'September'}
print({x: x**2 for x in range(10) if x%2 == 0})
