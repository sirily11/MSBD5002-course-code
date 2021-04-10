from neural_networks.activations.threshold_function import threshold_function
from neural_networks.neural_network import NeuralNetwork
import numpy as np

if __name__ == '__main__':
    x = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    output = np.array([
        [0],
        [0],
        [0],
        [1]
    ])

    learning_rate = 0.5

    weights = np.array([
        [0.1],
        [0.1]
    ])

    bias = 0.1

    neural_net = NeuralNetwork(input_matrix=x, desired_output=output, weights=weights, bias=bias,
                               learning_rate=learning_rate, activation_function=threshold_function)

    neural_net.train()
