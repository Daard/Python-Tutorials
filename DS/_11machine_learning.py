import random


def split_data(data, prob):
    """split data into fraction [prob, 1 - prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 0].append(row)
    return results


def train_test_split(x, y, test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

#Correctness
# https://en.wikipedia.org/wiki/F1_score

def accuracy(tp, fp, fn, tn):
    """fraction of correct prediction"""
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total


def precision(tp, fp):
    """precision measures how accurate out positives predictions are"""
    return tp / (tp + fp)


def recall(tp, fn):
    """recall measures what fraction of the positives out model identified"""
    return tp / (tp + fn)


def f1_scoure(tp, fp, fn, tn):
    """f1 is a harmonic mean of precision and recall"""
    p = precision(tp, fp)
    r = recall(tp, fn)
    return





