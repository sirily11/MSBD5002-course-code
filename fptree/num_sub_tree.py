from itertools import combinations


def get_number_of_item_set(num_nodes):
    s = 0
    for i in range(num_nodes):
        s += len(list(combinations(range(num_nodes), i)))

    return s + 1


if __name__ == '__main__':
    print(get_number_of_item_set(4))
