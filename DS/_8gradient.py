import math

def sum_of_squares(v):
    return sum(v_i**2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x+h) - f(x)) / h

def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimeate_graient(f, v, h=0.000001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    return [2*vi for vi in v]

def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f()

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """Use gradient descent to find theta that minimize target_fn"""
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_sizes)
                       for step_sizes in step_sizes]
        #choose the one that minimize the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_thetas, next_value


def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """the same if f returns a list of numbers"""
    return lambda *args, **kwargs : [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)