#Iterators

# class BinaryTree:
#     def __iter__(self):
#         return self.inorder_iter()
#
#     def inorder_iter(self):
#         pass
#
# xs = [1, 2, 3, 4, 5]
#
# for x in xs:
#     pass
#
# it = iter
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break
#     pass


#Generators

def g():
    print('Started')
    x = 42
    yield x
    x += 1
    yield x
    print('Done')

print(type(g))
# <class 'function'>
gen = g()
print(type(gen))
# <class 'generator'>
# Started
print(next(gen))
# 42
print(next(gen))
# 43

#unique
def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

xs = [1, 1, 2, 3]
unique(xs)
print(list(unique(xs)))
# [1, 2, 3]
print(1 in unique(xs))
# True

def map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)

xs = range(5)
print(map(lambda  x: x * x, xs))
#<generator object map at 0x1105751a8>
print(list(map(lambda  x: x * x, xs)))
#[0, 1, 4, 9, 16]

def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

xs = range(3)
ys = [42]
print(list(chain(xs, ys)))
#[0, 1, 2, 42]

def count(start=0):
    while True:
        yield start
        start += 1

counter = count()
for _ in range(5):
    print(next(counter))
# 0
# 1
# 2
# 3
# 4

#reusage

def g():
    yield 42

gen = g()
print(list(gen))
# [42]
print(list(gen))
#[0]

#more generators
gen = (x ** 2 for x in range(10 ** 42) if x % 2 == 1)
print(gen)
#<generator object <genexpr> at 0x103cd62b0>
print(next(gen))
#1
print(list(filter(lambda x: x % 2 ==1, (x ** 2 for x in range(10)))))
#[1, 9, 25, 49, 81]

def g():
    res = yield
    print('Got {!r}'.format(res))
    res = yield 42
    print('Got {!r}'.format(res))

gen = g()
next(gen)
#Got None
next(gen)
#Got None


