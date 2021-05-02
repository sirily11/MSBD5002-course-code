from data_stream.false_positive import ItemSet, FalsePosNeg


def q1():
    expected = ItemSet(freq_items=["i1", "i2"], in_freq_items=["i3", "i4"])
    algorithm = ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"])
    algorithm = ItemSet(freq_items=["i1", "i2", "i3"], in_freq_items=["i4"])
    algorithm = ItemSet(freq_items=["i1", "i3"], in_freq_items=["i2", "i4"])
    fal = FalsePosNeg(expected_output=expected, algorithm_output=algorithm)
    fal.run()


if __name__ == '__main__':
    q1()
