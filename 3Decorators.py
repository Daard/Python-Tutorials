def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

@trace
def identity(x):
    "I do nothing useful."
    return x

print(identity(42))
# identity (42,) {}
# 42

#Help and doc
def identity(x):
    'I do nothing.'
    return x
print(identity.__name__, identity.__doc__)
# identity I do nothing.
identity = trace(identity)
print(identity.__name__, identity.__doc__)
# inner None

#how to resolve?
def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    inner.__module__ = func.__module__
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@trace
def identity(x):
    'I do nothing useful.'
    return x

print(identity.__name__, identity.__doc__)

#functools has logic that wraps all inner attributes

import  functools
def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    functools.update_wrapper(inner, func)
    return inner

@trace
def identity(x):
    'I do nothing useful.'
    return x

print(identity.__name__, identity.__doc__)
# identity I do nothing useful.

#or the same can be done with decorator
def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

@trace
def identity(x):
    'I do nothing useful.'
    return x

print(identity.__name__, identity.__doc__)
# identity I do nothing useful.

#We can use global variable to endable or disable wrappers
trace_enabled = False
def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner if trace_enabled else func

#decorators and args

#MADNASSSSSS!!!!
# def with_arguments(deco):
#     @functools.wraps(deco)
#     def wrapper(*dargs, **dkwargs):
#         def decorator(func):
#             resut = deco(func, *dargs, **dkwargs)
#             functools.update_wrapper(resut, func)
#             return resut
#         return decorator
#     return wrapper
#
# @with_arguments
# def trace(func, handle):
#     def inner(*args, **kwargs):
#         print(func.__name__, args, kwargs, file=handle)
#         return func(*args, **kwargs)
#     return inner
#
# @trace()
# def identity(x):
#     return x
#THE END

#now decorators with args
import sys
def trace(func = None, *, handle=sys.stdout):
    if func is None:
        return lambda func : trace(func, handle=handle)
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

#DECORATORS IN PRACTICE
import time
def timethis(func=None, n_iter=100):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=".....")
        acc = float('inf')
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result
    return inner

result = timethis(sum)(range(10 ** 3))
# sum.....1.792800003386219e-05

def profiled(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls +=1
        return func(*args, **kwargs)
    inner.ncalls = 0
    return inner

@profiled
def identity(x):
    return x

print(identity(42))
#42
print(identity.ncalls)
#1

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner

@once
def init_settings():
    print("Setting initialized.")
init_settings()
#Setting initialized.
init_settings()
#


def memorized(func):
    cache = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

@memorized
def ackermann(m, n):
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3, 4))

import warnings
def deprecated(func):
    code = func.__code__
    warnings.warn_explicit(
        func.__name__ + 'is deprecated',
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno + 1)
    return func

@deprecated
def identity(x):
    return x
#Will notify user during import

#Contract programming

# is_not_none = post(lambda  r: not math.isnan(r), 'not a number')
#
# @is_not_none
# def something_useful():
#     pass
import math

def pre(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)
        return inner
    return wrapper

@pre(lambda x: x >= 0, 'negative argument')
def checked_log(x):
    return math.log(x)

# checked_log(-42)
# AssertionError: negative argument

def post(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            assert cond(result), message
            return result
        return inner
    return wrapper

@post(lambda x : not math.isnan(x), 'not a number')
def something_useful(x):
    return float(x)

# something_useful('nan')
# AssertionError: not a number

# post(lambda x : not math.isnan(x), 'not a number')(something_useful)('nan')
# AssertionError: not a number

def square(func):
    return lambda x: func(x * x)

def addsome(func):
    return lambda x : func(x + 42)

@square
@addsome
#result = square(addsome(identity))(2)
def identity(x):
    return x

print(identity(2))
#46

@addsome
@square
#result = addsome(square(identity))(2)
def identity(x):
    return x

print(identity(2))
#1936


