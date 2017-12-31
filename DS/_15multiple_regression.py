import DS._4linear_algebra as la
import DS._8gradient as gr
import random
from functools import partial


def predict(x_i, beta):
    """assumes that the first element of each x_i is 1"""
    return la.dot(x_i, beta)


def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)


def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2


def squared_error_gradient(x_i, y_i, beta):
    """the gradient (with respect to beta) corresponding the i-th error term"""
    return [2 * x_ij * error(x_i, y_i, beta) for x_ij in x_i]

def estimate_beta(x):
    random.seed(0)
    beta_initial = [random.random() for _ in x[0]]
    return gr.minimize_batch(squared_error,
                             squared_error_gradient,
                             beta_initial,
                             tolerance=0.001)
# regularization

# alpha is a hyperparameter controlling how harsh the penalty is
# sometimes it's called 'lambda' but that already means something in Python

def ridge_penalty(beta, alpha):
    return alpha * la.dot(beta[1:], beta[1:])


def squraed_error_ridge(x_i, y_i, beta, alpha):
    """estimate error plus ridge penalty on beta"""
    return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)


def ridge_penalty_gradient(beta, alpha):
    """gradient of just the ridge penalty"""
    return [0] + [2 * alpha * beta_j for beta_j in beta[1:]]


def squared_error_ridge_gradient(x_i, y_i, beta, alpha):
    """the gradient corresponding to the i-th squared error term
        including the ridge penalty"""
    return la.vector_add(squared_error_gradient(x_i, y_i, beta),
                  ridge_penalty_gradient(beta, alpha))


def estimate_beta_ridge(x, y, alpha):
    """use gradient descent to fit a ridge regression with penalty alpha"""
    random.seed(0)
    beta_initial = [random.random() for _ in x[0]]
    return gr.minimize_batch(partial(squraed_error_ridge, alpha=alpha),
                             partial(squared_error_gradient, alpha=alpha),
                             beta_initial, tolerance=0.0001)
