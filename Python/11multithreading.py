import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread
from threading import Lock
from collections import deque
from threading import Condition
import math
from functools import partial
from concurrent.futures import ProcessPoolExecutor

def countdown(n):
    for i in range(n):
        print(n - i - 1, 'left')
        time.sleep(1)

t = Thread(target=countdown, args=(3, ))
t.start()

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.n- i - 1, 'left', self.name)
            time.sleep(1)

t = CountdownThread(3)
t.start()
print(t.is_alive()) #True
t.join()
print(t.is_alive()) #False

#correct thread kill
class Task:
    def __init__(self):
        self.running = True

    def termminate(self):
        self.running = False

    def run(self, n):
        while self.running:
            #
            pass

class SharedCounter:
    def __init__(self, value):
        self._value = value
        self._lock = Lock()

    def increment(self, delta=1):
        self._lock.acquire()
        self._value += delta
        self._lock.release()

    def get(self):
        return self._value

dq = deque()
is_empty = Condition()

def producer():
    i = 0
    while True:
        is_empty.acquire()
        dq.append(i)
        is_empty.notify()
        is_empty.release()

def consumer():
    while True:
        is_empty.acquire()
        while not dq:
            is_empty.wait()
        print(dq.popleft())
        is_empty.release()


def integrate(f, a, b, *, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate_async(f, a, b, *, n_jobs, n_iter=1000):
    executor = ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in as_completed(fs))

print(integrate_async(math.cos, 0, math.pi / 2, n_jobs=2))

#Multiprocessing
def integrate_async(f, a, b, *, n_jobs, n_iter=1000):
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in as_completed(fs))





