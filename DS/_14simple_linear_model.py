import DS._5statistics as stat
import random
import DS._8gradient as grad

def predict(alpha, beta, x_i):
    return beta * x_i + alpha


def error(alpha, beta, x_i, y_i):
    """the error from predicting beta * x_i + alpha
    when the actual value is y_i"""
    return y_i - predict(alpha, beta, x_i)


def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))


def least_squares_fit(x, y):
    """given training values for x and y,
    find the least-sqa=uares values of alpha and beta"""
    beta = stat.correlation(x, y) * stat.std_deviation(y) / stat.std_deviation(x)
    alpha = stat.mean(y) - beta * stat.mean(x)
    return alpha, beta


# Using Gradient Descent

def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2


def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i),
            -2 * error(alpha, beta, x_i, y_i) * x_i]


class SimpleLinearClassifier:

    def __init__(self):
        self.alpha = 0
        self.beta = 0

    def train(self):
        random.seed(0)
        theta = [random.random(), random.random]
        self.alpha, self.beta = grad.minimize_batch(squared_error,
                                                    squared_error_gradient,
                                                    theta, tolerance=0.000001)

    def predict(self, x):
        return self.alpha + self.beta * x