from neural_networks.lstm import LSTM
import numpy as np


def q1():
    x_m = np.array([
        [0.5, 0.7],
        [0.3, 0.2]
    ])

    y_m = np.array([
        [0.7],
        [0.8]
    ])

    wf_m = np.array([
        [0.1],
        [0.2],
        [0.5]
    ])

    wi_m = np.array([
        [0.6],
        [0.3],
        [0.8]
    ])

    wa_m = np.array([
        [0.4],
        [0.7],
        [0.1]
    ])

    wo_m = np.array([
        [0.5],
        [0.8],
        [0.9]
    ])

    bf_m = 0.1
    bi_m = 0.2
    ba_m = 0.3
    bo_m = 0.4

    lstm = LSTM(input_matrix=x_m, output=y_m,
                bf=bf_m, bi=bi_m, ba=ba_m, bo=bo_m,
                wa=wa_m, wf=wf_m, wo=wo_m, wi=wi_m,
                )
    lstm.train(prev_y=0.9, prev_state=0.7)


if __name__ == '__main__':
    q1()
