import math
import DS._4linear_algebra as la
from functools import reduce

def logistic(x):
    return 1.0 / (1.0 + math.exp(x))


def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))


def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(logistic(la.dot(x_i, beta)))
    else:
        return math.log(1 - logistic(la.dot(x_i, beta)))


def logistic_log_likelihood(x, y, beta):
    return sum(logistic_log_likelihood_i(x_i, y_i, beta)
               for x_i, y_i in zip(x, y))


def logistic_log_partial_ij(x_i, y_i, beta, j):
    """here i is the index of the data point,
    j the index of the derivative"""
    return (y_i - logistic(la.dot(x_i, beta))) * x_i[j]


def logistic_log_gradient_i(x_i, y_i, beta):
    """the gradient of the log likelihood
    corresponding to the i-th data point"""
    return [logistic_log_partial_ij(x_i, y_i, beta)
            for j, _ in enumerate(beta)]


def logistic_log_gradient(x, y, beta):
    return reduce(la.vector_add, [logistic_log_gradient_i(x_i, y_i, beta)
                                  for x_i, y_i in zip(x, y)])
