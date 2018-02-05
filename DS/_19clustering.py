import DS._4linear_algebra as la
import random

class KMeans:
    """performs k-means clustering"""

    def __init__(self):
        self.k = k
        self.means = None


    def clasify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: la.distance(input, self.means[i]))

    def train(self, inputs):
        # choose k random points as the initial means
        self.means = random.sample(inputs, self.k)
        assignments = None

        while True:
            # Find new assignments
            new_assignments = map(self.clasify, inputs)

            # If no assignments have changed, we'ar done
            if assignments == new_assignments:
                return

            #Otherwise keep the new assignments,
            assignments = new_assignments

            # And compute new means based on the new assignments
            for i in range(self.k):
                #find all points assigned to cluster i
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                # make sure i_points is not empty so don't devide by 0
                if i_points:
                    self.means[i] = la.vector_mean(i_points)