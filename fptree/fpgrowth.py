from typing import List
from fptree import find_frequent_patterns, print_tree
from collections import OrderedDict
from pprint import pprint


def find_frequency_table(transactions: List[List]):
    return_dic = {}
    for t in transactions:
        for e in t:
            if e not in return_dic:
                return_dic[e] = 1
            else:
                return_dic[e] = return_dic[e] + 1

    return dict(OrderedDict(sorted(return_dic.items(), key=lambda k: k[1], reverse=True)))


def find_dict_with_value_greater(data: dict, threshold: int):
    return dict(filter(lambda k: k[1] >= threshold, data.items()))


def get_list_transaction_by_frequency_table(transactions: List[List], frequency_table: dict) -> List[List]:
    return_list = []

    for t in transactions:
        temp = []
        for e in t:
            if e in frequency_table:
                temp.append(e)
        return_list.append(temp)

    return return_list


if __name__ == '__main__':
    transactions = [["a", "b", "c", "d", "e", "f", "g", "h"],
                    ["a", "f", "g"],
                    ["b", "d", "e", "f", "j"],
                    ["a", "b", "d", "i", "k"],
                    ["a", "b", "e", "g"]]

    transactions = [["b", "d", "f", "r"],
                    ["b", "c", "d", "s"],
                    ["c", "m", "t"],
                    ["b", "d", "f"],
                    ["a", "d", "f"],
                    ["e", "f"],
                    ["f", "h"],
                    ["b", "d", "c"],
                    ["a", "l"],
                    ["c", "g"],
                    ["c", "k"],
                    ["f", "n", "o"],
                    ["b", "c", "d", "p"],
                    ["f", "j", "q"],
                    ["c", "i"],
                    ["a", "d"]
                    ]
    threshold = 2

    print("Frequency table")
    frequency_table = find_frequency_table(transactions)
    pprint(frequency_table)

    print("Frequency table greater than threshold")
    frequency_table_greater = find_dict_with_value_greater(frequency_table, threshold)
    pprint(frequency_table_greater)

    print("New Transactions")
    new_transactions = get_list_transaction_by_frequency_table(transactions=transactions,
                                                               frequency_table=frequency_table_greater)
    pprint(new_transactions)

    print("Frequent patterns")
    patterns = find_frequent_patterns(transactions, threshold)
    pprint(patterns)

    print("FP Tree")
    print_tree(transactions, threshold)

