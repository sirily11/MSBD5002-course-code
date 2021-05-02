from typing import Callable, List
import numpy as np

from neural_networks.activations.sigmoid import sigmoid
from neural_networks.activations.tanh import tanh


class LSTM:
    def __init__(self, input_matrix: np.ndarray, output: np.ndarray,
                 wf: np.ndarray, wi: np.ndarray, wa: np.ndarray, wo: np.ndarray,
                 bf: float, bi: float, ba: float, bo: float,
                 f_activation: Callable = sigmoid, i_activation: Callable = sigmoid,
                 a_activation: Callable = tanh, o_activation: Callable = sigmoid,
                 y_activation: Callable = tanh):
        self.input_matrix = input_matrix
        self.output = output
        self.f_activation = f_activation
        self.i_activation = i_activation
        self.a_activation = a_activation
        self.o_activation = o_activation
        self.y_activation = y_activation
        self.wf = wf
        self.wi = wi
        self.wa = wa
        self.wo = wo
        self.bf = bf
        self.bi = bi
        self.ba = ba
        self.bo = bo

    def train(self, prev_state: float = None, prev_y: float = None):
        states = []
        y_outs = []
        f_outs = []
        i_outs = []
        a_outs = []
        s_outs = []
        o_outs = []

        if prev_state:
            states.append(prev_state)

        if prev_y:
            y_outs.append(prev_y)

        start_index = 1 if prev_y is not None else 0

        for t in range(start_index, len(self.input_matrix) + start_index):
            print(f"At Time {t + 1}")
            x = self.input_matrix[t - start_index]
            y_prev = y_outs[t - 1] if len(y_outs) > 0 else [0]
            y = self.output[t - start_index][0]
            s = states[t - 1] if len(states) > 0 else 0

            f_out = self.f(w=self.wf, b=self.bf, x=x, y=y_prev)
            i_out = self.i(w=self.wi, b=self.bi, x=x, y=y_prev)
            a_out = self.a(w=self.wa, b=self.ba, x=x, y=y_prev)
            s_out = f_out * s + i_out * a_out
            o_out = self.o(w=self.wo, b=self.bo, x=x, y=y_prev)
            y_out = o_out * self.y_activation(s_out)
            error = y_out - y
            print(
                f"f_t = {round(f_out, 4)}, i_t = {round(i_out, 4)}, a_t = {round(a_out, 4)}, s_t = {round(s_out, 4)}, "
                f"o_t = {round(o_out, 4)}, y_t = {round(y_out, 4)}, error = {round(error, 4)}")

            states.append(s_out)
            y_outs.append(y_out)
            f_outs.append(f_out)
            i_outs.append(i_out)
            a_outs.append(a_out)
            s_outs.append(s_out)
            o_outs.append(o_outs)

        return y_outs, f_outs, i_outs, a_outs, s_outs, o_outs

    def f(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray):
        new_s = np.vstack((x.reshape((-1, 1)), y))
        new_s = w.T.dot(new_s) + b
        new_s = self.f_activation(new_s[0])

        return new_s[0]

    def i(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray):
        new_s = np.vstack((x.reshape((-1, 1)), y))
        new_s = w.T.dot(new_s) + b
        new_s = self.i_activation(new_s[0])

        return new_s[0]

    def a(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray):
        new_s = np.vstack((x.reshape((-1, 1)), y))
        new_s = w.T.dot(new_s) + b
        new_s = self.a_activation(new_s[0])

        return new_s[0]

    def o(self, w: np.ndarray, b, x: np.ndarray, y: np.ndarray):
        new_s = np.vstack((x.reshape((-1, 1)), y))
        new_s = w.T.dot(new_s) + b
        new_s = self.o_activation(new_s[0])

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

    wf_m = np.array([
        [0.7],
        [0.3],
        [0.4]
    ])

    wi_m = np.array([
        [0.2],
        [0.3],
        [0.4]
    ])

    wa_m = np.array([
        [0.4],
        [0.2],
        [0.1]
    ])

    wo_m = np.array([
        [0.8],
        [0.9],
        [0.2]
    ])

    bf_m = 0.4
    bi_m = 0.2
    ba_m = 0.5
    bo_m = 0.3

    lstm = LSTM(input_matrix=x_m, output=y_m,
                bf=bf_m, bi=bi_m, ba=ba_m, bo=bo_m,
                wa=wa_m, wf=wf_m, wo=wo_m, wi=wi_m,
                f_activation=sigmoid)
    lstm.train(prev_y=0.2107, prev_state=0.3220)
