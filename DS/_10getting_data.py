import matplotlib.pyplot as plt
from collections import Counter
import math
import DS._5statistics as stat
import DS._4linear_algebra as la

def bucketsize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketsize(point, bucket_size)
                   for point in points)

def plot_histogram(points, bucket_size, title=''):
    histogram = make_histogram(points, bucket_size)
    plt.bar(list(histogram.keys()), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

def correlation_matrix(data):
    """returns the num_columns x num_columns matrix whose (i,j)th entry
    is the correlation between columns i and j of data"""
    _, num_columns = la.shape(data)
    def matrix_entry(i, j):
        return stat.correlation(la.get_column(data, i),
                                la.get_column(A,j))
    return la.make_matrix(num_columns, num_columns, matrix_entry)