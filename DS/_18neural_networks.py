import DS._4linear_algebra as la
import math


def step_function(x):
    return 1 if x>=0 else 0


def perceptron_output(weights, bias, x):
    calculation = la.dot(weights, x) + bias
    return step_function(calculation)


def sigmoid(t):
    return 1.0 / (1.0 + math.exp(-t))


def neuron_output(weights, inputs):
    return sigmoid(la.dot(weights, inputs))


def feed_forward(neural_network, input_vector):
    """takes in a neural network
    (represented as a list of lists of lists of weights)
    and returns the output from forward-propagating the input"""
    outputs = []
    # process one layer at a time
    for layer in neural_network:
        input_with_bias = input_vector +\
                          [1] # add a bias input
        output = [neuron_output(neuron, input_with_bias) # compute the output
                  for neuron in layer]
        outputs.append(output)
         # then the input to the next layer is the output of this one
        input_vector = output
    return outputs

xor_network = [
                [[20, 20, -30], # and
                 [20, 20, -10]], # or
                [[-60, 60, -30]], # 2nd input
]

for x in [0, 1]:
    for y in [0, 1]:
        # feed_forward pruces the outputs of every neron
        print(x, y, feed_forward(xor_network, [x, y])[-1])

def backpropagate(network, input_vector, targets):
    hidden_outputs, outputs = feed_forward(network, input_vector)
    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - target)
                     for output, target
                     in zip(outputs, targets)]
    # adjust weights for output layer, one neuron at a time
    for i, output_neuron in enumerate(network[-1]):
        # focus on the i-th output layer neuron
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            # adjust the j-th weight
            # based on both this neuron's delta and its j-th input
            output_neuron[j] -= output_deltas[i] * hidden_output
            # back-propagate errors to hidden layer
            hidden_deltas = [hidden_output * (1 - hidden_output)
                             * la.dot(output_deltas, [n[i] for n in network[-1]])
                             for i, hidden_output in enumerate(hidden_outputs)]
            # adjust weights for hidden layer, one neuron at a time
            for i, hidden_neuron in enumerate(network[0]):
                for j, input in enumerate(input_vector + [1]):
                    hidden_neuron[j] -= hidden_deltas[i] * input
                    



