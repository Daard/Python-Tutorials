# Use a mapper function to turn each item into zero or more key-value pairs.
# (Often this is called the map function,
# but there is already a Python function called map and we don’t need to confuse the two.)

# Collect together all the pairs with identical keys.

# Use a reducer function on each collection of grouped values to produce
#  output values for the corresponding key.
from collections import Counter
from collections import defaultdict
from functools import partial


def word_count_old(documents):
    """word count not using MapReduce"""
    return Counter(word for document in documents for word in document)


def wc_mapper(document):
    """for each word in the document, emit (word, 1)"""
    for word in document:
        yield (word, 1)


def wc_reducer(word, counts):
    """sum up the counts for a word"""
    yield (word, sum(counts))


def word_count(documents):
    """count the words in the documents using MapReduce"""
    # place to store grouped values
    collector = defaultdict(list)
    for  document in documents:
        for word, count in wc_mapper(document):
            collector[word].append(count)
    return [output
            for word, counts in collector.items()
            for output in wc_reducer(word, counts)]

# Mapreduce More Generally

def map_reduce(inputs, mapper, reducer):
    """runs MapReduce on the inputs using mapper and reducer"""
    collector = defaultdict(list)
    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)
    return [output
            for key, values in collector.items()
            for output in reducer(key, value)]

#Sample Matrix Multiplication

def matrix_multiply_mapper(A_rows, B_cols, element):
    """element is a tuple (matrix_name, i, j, value)"""
    matrix, i, j, value = element
    if matrix == 'A':
        for column in range(B_cols):
            #A_ij is the i-th entry in the sum for each C_i_column
            yield((i, column), (j, value))
    else:
        for row in range(A_rows):
            # B_ij is the i-th entry in the sum for each C_row_j
            yield ((row, j), (i, value))


def matrix_multiply_reducer(key, indexed_values):
    results_by_index = defaultdict(list)
    for index, value in indexed_values:
        results_by_index[index].append(value)

    #sum up all the products of the positions with two results
    sum_product = sum(results[0] * results[1]
                      for results in results_by_index.values()
                      if len(results) == 2)
    if sum_product != 0.0:
        yield (key, sum_product)


entries = [( "A" , 0 , 0 , 3 ), ( "A" , 0 , 1 , 2 ),
 ( "B" , 0 , 0 , 4 ), ( "B" , 0 , 1 , - 1 ), ( "B" , 1 , 0 , 10 )]
mapper = partial ( matrix_multiply_mapper , 2 , 3 )
reducer = matrix_multiply_reducer
map_reduce ( entries , mapper , reducer ) # [((0, 1), -3), ((0, 0), 32)]




