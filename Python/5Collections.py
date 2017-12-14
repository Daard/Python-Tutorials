#Tuple - immutable heterogenous data

date = 'October', 5
xs = (42,)
#unpacking
[x] = xs
print(x)
#42
x, = xs
print(xs)
#42

#Slicing
person = ('Gerorge', 'Carling', 'May', 12, 1937)
name, birthday = person[:2], person[2:]
print(name)
# ('Gerorge', 'Carling')
print(birthday)
# ('May', 12, 1937)

#reverse
print(tuple(reversed((1, 2, 3))))
#(3, 2, 1)
print((1, 2, 3)[::-1])
#(3, 2, 1)

#Concatanation
xs, ys = (1, 2), (3, )
print(id(xs), id(ys))
#4490368264 4489065248
# plus + returns new tuple
print(id(xs + ys))
#4515373920

#Compare works like in strings
print((1, 2, 3) < (1, 2, 4))
#True
print((1, 2, 3, 4) < (1, 2, 4))
#True
print((1, 2) < (1, 2, 42))
#True

#Namedtuple
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person('George', age=77)
print(p._fields)
# ('name', 'age')
print(p.name, p.age)
# George 77
print(p._asdict())
# OrderedDict([('name', 'George'), ('age', 77)])
p1 = p._replace(name='Bill')
print(p)
#Person(name='George', age=77)
print(p1)
#Person(name='Bill', age=77)

#List
[0] * 2
#[0, 0]
[""] * 2
["", ""]
chunks = [[0]] *2
print(chunks)
#[[0], [0]]
chunks[0][0] = 42
print(chunks)
#[[42], [42]]
#How to use chunks in right way?
chunks = [[0] for _ in range(2)]
print(chunks)
# [[0], [0]]
chunks[0][0] = 42
print(chunks)
# [[42], [0]]

#List methods
xs = [1, 2, 3]
xs.append(42) #-> [1, 2, 3, 42]
xs.extend({-1, -2}) #->[1, 2, 3, 42, -1, -2]

xs = [1, 2, 3]
xs.insert(0, 4) #-> [4, 1, 2, 3]
xs.insert(-1, 42) #->[4, 1, 2, 42, 3]
xs = [1, 2, 3]
xs[:2] = [0] * 2 #->[0, 0, 3]

#Concatanation
xs, ys = [1, 2], [3]
print(id(xs), id(ys))
#4549779144 4549778376
print(id(xs + ys))
#4432810120
xs += ys
print(id(xs))
#4493512392

xs = []
def f():
    #you must use global for +=
    global xs
    xs += [42]

#Deleting
xs = [1, 2, 3]
del xs[:2]
print(xs)
#[3]

xs = [1, 2, 3]
print(xs.pop(1))
#2
print(xs)
#[1, 3]

xs = [1, 1, 0]
xs.remove(1)
print(xs)
#[1, 0]

#Reverse vs reversed

#new list
print(list(reversed([1, 2, 3])))
#[3, 2, 1]

xs = [1, 2, 3]
#inplace
xs.reverse()
print(xs)
#[3, 2, 1]

#Sort vs sorted

xs = [3, 2, 1]
#new list
print(sorted(xs), xs)
#[1, 2, 3] [3, 2, 1]
#inplace
xs.sort()
print(xs)
# [1, 2, 3]

xs = [3, 2, 1]
xs.sort(key=lambda x: x % 2, reverse=True)
print(xs)
#[3, 1, 2]

#list is a stack, list is a queue
stack = []
stack.append(1)
stack.append(2)
stack.pop()
print(stack)
# [1]
q = []
q.append(1)
q.append(2)

print(q.pop(0))
#1
print(q)
# [2]

from collections import deque
q = deque()

q = deque([1, 2, 3])
q.appendleft(0)
print(q)
#deque([0, 1, 2, 3])
q.append(4)
print(q)
#deque([0, 1, 2, 3, 4])
print(q.popleft())
#0

#maxlen

q = deque([1, 2], maxlen=2)
q.appendleft(0)
print(q)
# deque([0, 1], maxlen=2)
q.append(2)
print(q)
#deque([1, 2], maxlen=2)

#Union

xs, ys, zs = {1, 2}, {2, 3}, {3, 4}
set.union(xs, ys, zs)
# {1, 2, 3, 4}
set.intersection(xs, ys, zs)
#set()
set.difference(xs, ys, zs)
#{1}
print(xs <= ys)
#False
print(xs < xs)
#False
print(xs | ys >= xs)
#True

#Adding
seen = set()
seen.add(42)
print(seen)
#{42}
seen.update([1, 2])
print(seen)
#{1, 42, 2}
seen.update([], [1], [2], [3])
print(seen)
#{3, 1, 42, 2}

#Dictionary
d = dict(foo='bar')
print(dict(d))
#{'foo': 'bar'}
print(dict(d, boo='baz'))
#{'foo': 'bar', 'boo': 'baz'}

print(d.keys())
# dict_keys(['foo'])
print(d.values())
# dict_values(['bar'])
print(d.items())
# dict_items([('foo', 'bar')])

d = {'foo':'boo'}
print(d['foo'])
#boo
print(d.get('boo', 42))
#42

d={'foo':'boo'}
d.setdefault('foo', '???')
#'bar'
d.setdefault('boo', 42)
#42
print(d)
# {'foo': 'boo', 'boo': 42}

#deleting

del d['foo']
d.pop('boo')
d.clear()

#Counter
from collections import Counter
c = Counter(['foo', 'foo', 'foo', 'bar'])
c['foo'] +=1
print(c)
# Counter({'foo': 4, 'bar': 1})
c.pop('foo') #->4
print(c)
#Counter({'bar': 1})

c = Counter(foo=4, bar=-1)
print(list(c.elements()))
# ['foo', 'foo', 'foo', 'foo']
print(c.most_common(1))
#[('foo', 4)]
c.update(['bar'])
print(c)
# Counter({'foo': 4, 'bar': 0})
c.subtract({'foo':2})
print(c)
# Counter({'foo': 2, 'bar': 0})

c1 = Counter(foo=4, bar=-1)
c2 = Counter(foo=2, bar=2)
print(c1 + c2)
#Counter({'foo': 6, 'bar': 1})
print(c1 - c2)
#Counter({'foo': 2})
print(c1 & c2)
#Counter({'foo': 2})
print(c1 | c2)
#Counter({'foo': 4, 'bar': 2})