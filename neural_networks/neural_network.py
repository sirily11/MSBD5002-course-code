from typing import Callable

import numpy as np

from neural_networks.activations.sigmoid import sigmoid
from neural_networks.activations.tanh import tanh
from neural_networks.activations.threshold_function import threshold_function


class NeuralNetwork:
    def __init__(self, input_matrix: np.ndarray, desired_output: np.ndarray, learning_rate: float, weights: np.ndarray,
                 bias: float, activation_function: Callable[[float], np.ndarray]):
        self.input_matrix = input_matrix
        self.desired_output = desired_output
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.weights = weights
        self.bias = bias

    def train(self, epoch=1):
        for e in range(epoch):
            print("================================")
            print(f"Epoch: {e}")
            for i, x in enumerate(self.input_matrix):
                print()
                print(f"Round: {i}")
                d = self.desired_output[i]

                net = self.forward_pass(x)
                new_weights, new_bias = self.backward_pass(x=x, y=net, d=d)
                print(f"Weights: {np.round(new_weights, 2)}")
                print(f"Bias: {np.round(new_bias, 2)}")

                self.weights = new_weights
                self.bias = new_bias

    def forward_pass(self, x) -> float:
        net = 0
        for i, xi in enumerate(x):
            wi = self.weights[i]
            net += xi * wi

        net += self.bias
        net = self.activation_function(net)
        return net

    def backward_pass(self, x, y, d):
        weights = []
        for i, xi in enumerate(x):
            wi = self.weights[i]
            new_w = wi + self.learning_rate * (d - y) * xi
            print(f"w_{i + 1} + {self.learning_rate} \\times ( {d[0]} - {y} ) \\times x_{i} = {round(new_w[0], 4)}")
            weights.append(new_w)

        new_bias = self.bias + self.learning_rate * (d - y)
        print(f"b = {self.bias} + {self.learning_rate} \\times ( {d[0]} - {y} ) = {round(new_bias[0], 4)}")
        return weights, new_bias


if __name__ == '__main__':
    weights = np.array([[0.3], [0.2]])
    bias = 0.1
    x = np.array([
        [22, 50],
        [10, 15],
        [40, 22],
        [7, 6],
        [50, 30],
        [30, 20]
    ])

    y = np.array([
        [1],
        [-1],
        [1],
        [-1],
        [1],
        [-1]
    ])

    activation_function = tanh

    learning_rate = 0.4

    n = NeuralNetwork(input_matrix=x, desired_output=y, bias=bias, weights=weights,
                      activation_function=activation_function,
                      learning_rate=learning_rate)
    n.train()
