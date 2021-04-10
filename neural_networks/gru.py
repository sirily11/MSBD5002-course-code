from typing import Callable, List
import numpy as np

from neural_networks.activations.sigmoid import sigmoid
from neural_networks.activations.tanh import tanh


class GRU:
    def __init__(self, input_matrix: np.ndarray, output: np.ndarray,
                 wr: np.ndarray, wa: np.ndarray, wu: np.ndarray,
                 br: float, ba: float, bu: float,
                 r_activation: Callable = sigmoid,
                 a_activation: Callable = tanh, u_activation: Callable = sigmoid):
        self.input_matrix = input_matrix
        self.output = output
        self.r_activation = r_activation
        self.a_activation = a_activation
        self.u_activation = u_activation
        self.wr = wr
        self.wu = wu
        self.wa = wa
        self.br = br
        self.ba = ba
        self.bu = bu

    def train(self, prev_y: float = None):
        y_outs: List[float] = []

        if prev_y:
            y_outs.append(prev_y)

        for t in range(len(self.input_matrix)):
            print(f"At Time {t + 1}")
            x = self.input_matrix[t]
            # y_{t-1}
            y_prev = y_outs[t - 1] if len(y_outs) > 0 else 0
            # current y value, real y
            y = self.output[t][0]

            r_out = self.r(w=self.wr, b=self.br, x=x, y=np.array(y_prev))
            a_out = self.a(w=self.wa, b=self.ba, x=x, y=np.array(y_prev), r=r_out)
            u_out = self.u(w=self.wu, b=self.bu, x=x, y=np.array(y_prev))
            y_out = (1 - u_out) * y_prev + u_out * a_out
            error = y_out - y

            print(
                f"r_t = {round(r_out, 4)}, a_t = {round(a_out, 4)}, u_t = {round(u_out, 4)}, "
                f"y_t = {round(y_out, 4)}, error = {round(error, 4)}")

            y_outs.append(y_out)

    def r(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray):
        new_s = np.vstack((x.reshape((-1, 1)), y))
        new_s = w.T.dot(new_s) + b
        new_s = self.r_activation(new_s[0])

        return new_s[0]

    def a(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray, r):
        new_s = np.vstack((x.reshape((-1, 1)), y * r))
        new_s = w.T.dot(new_s) + b
        new_s = self.a_activation(new_s[0])

        return new_s[0]

    def u(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray):
        new_s = np.vstack((x.reshape((-1, 1)), y))
        new_s = w.T.dot(new_s) + b
        new_s = self.u_activation(new_s[0])

        return new_s[0]


if __name__ == '__main__':
    x_m = np.array([
        [0.1, 0.4],
        [0.7, 0.9]
    ])

    y_m = np.array([
        [0.3],
        [0.5]
    ])

    wr_m = np.array([
        [0.7],
        [0.3],
        [0.4]
    ])

    wa_m = np.array([
        [0.2],
        [0.3],
        [0.4]
    ])

    wu_m = np.array([
        [0.4],
        [0.2],
        [0.1]
    ])

    br_m = 0.4
    ba_m = 0.3
    bu_m = 0.5

    gru = GRU(input_matrix=x_m, output=y_m, wr=wr_m, wa=wa_m, wu=wu_m, br=br_m, ba=ba_m, bu=bu_m)
    gru.train()
