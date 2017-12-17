import math
import DS._6probability as pr

def normal_appr_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


normal_probability_below = pr.normal_cdf


print(normal_probability_below(1))

print(pr.inverse_normal_cdf(0.86))


def normal_probability_above(lo, mu, sigma=1):
    return 1 - pr.normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu, sigma):
    return pr.normal_cdf(hi, mu, sigma) - pr.normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu=0, sigma=1):
    """"returns the z for which P(Z <= z) = probability"""
    return pr.inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return pr.inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


