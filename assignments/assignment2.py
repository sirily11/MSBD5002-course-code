from neural_networks.gru import GRU
from neural_networks.lstm import LSTM
import numpy as np


def lstm_question():
    x_m = np.array([
        [0.3, 0.6],
        [0.1, 1.0]
    ])

    y_m = np.array([
        [0.2],
        [0.4]
    ])

    wf_m = np.array([
        [0.7],
        [0.4],
        [0.1]
    ])

    wi_m = np.array([
        [0.2],
        [0.6],
        [0.7]
    ])

    wa_m = np.array([
        [0.3],
        [0.2],
        [0.1]
    ])

    wo_m = np.array([
        [0.6],
        [0.3],
        [0.1]
    ])

    bf_m = 0.1
    bi_m = 0.4
    ba_m = 0.3
    bo_m = 0.2

    lstm = LSTM(input_matrix=x_m, output=y_m,
                bf=bf_m, bi=bi_m, ba=ba_m, bo=bo_m,
                wa=wa_m, wf=wf_m, wo=wo_m, wi=wi_m,
                )
    lstm.train()


def gru_question():
    x_m = np.array([
        [0.3, 0.6],
        [0.1, 1.0]
    ])

    y_m = np.array([
        [0.2],
        [0.4]
    ])

    wr_m = np.array([
        [0.5],
        [0.2],
        [0.3]
    ])

    wa_m = np.array([
        [0.2],
        [0.4],
        [0.1]
    ])

    wu_m = np.array([
        [0.1],
        [0.3],
        [0.2]
    ])

    br_m = 0.2
    ba_m = 0.1
    bu_m = 0.1

    gru = GRU(input_matrix=x_m, output=y_m, wr=wr_m, wa=wa_m, wu=wu_m, br=br_m, ba=ba_m, bu=bu_m)
    gru.train()


if __name__ == '__main__':
    gru_question()
