from typing import List
from itertools import combinations


def count_support(column):
    count = 0
    for i in column:
        if i == 1:
            count += 1

    return count


def join_table(table_a, table_b):
    assert len(table_b) == len(table_a)
    result = []
    for index, a in enumerate(table_a):
        b = table_b[index]
        if a == b and a == 1:
            result.append(1)
        else:
            result.append(0)
    return result


def generate_dataset(table: dict, candidates: List[str], size: int):
    final_candidates = [list(l) for l in combinations(candidates, size)]
    final_result = []

    for s in final_candidates:
        temp = []
        if len(s) == 1:
            final_result.append(table[s[0]])
            continue
        for i, c in enumerate(s):
            if i + 1 < len(s):
                if len(temp) == 0:
                    temp = join_table(table[c], table[s[i + 1]])
                else:
                    temp = join_table(temp, table[s[i + 1]])
        final_result.append(temp)
    return final_result, final_candidates


def apriori(input_tables, threshold):
    size = 1
    candidates = [key for key, value in input_tables.items()]
    while True:
        temp_itemsets, temp_candidates = generate_dataset(input_tables, candidates, size)
        large_itemsets = []
        large_candidates = []
        large_list_candidates = []
        for i, l in enumerate(temp_candidates):
            itemset = temp_itemsets[i]
            support = count_support(itemset)

            if support >= threshold:
                large_itemsets.append(temp_itemsets[i])
                large_list_candidates.append(l)
                for c in l:
                    if c not in large_candidates:
                        large_candidates.append(c)
        large_candidates.sort()
        candidates = sorted(large_candidates)
        print(f"==== Size {size} itemsets ====")
        print("Join step:")
        print(f"Itemsets: {temp_itemsets}")
        print(f"Candidates : {temp_candidates}")
        print("Prune step:")
        print(f"Itemsets  : {large_itemsets}")
        print(f"Candidates L{size}: {large_list_candidates}")
        print(f"Total: {large_candidates}")
        size += 1
        if len(candidates) == 0:
            break


if __name__ == '__main__':
    tables = {
        "a": [1, 1, 0, 1, 1],
        "b": [0, 0, 0, 0, 0],
        "c": [0, 0, 1, 1, 1],
        "d": [1, 1, 0, 1, 0],
        "e": [0, 1, 0, 1, 1],
    }

    apriori(input_tables=tables, threshold=2)
