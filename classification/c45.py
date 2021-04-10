from typing import Tuple, List, Any
import pandas as pd

from classification.entropy import entropy
from classification.utils import get_initial_information, information_gain, calculate_percentage


def calculate_split_info(target_table: pd.DataFrame, column: str) -> float:
    unique = target_table[column].unique()
    total = len(target_table)
    ps = []
    for v in unique:
        n = len(target_table[target_table[column] == v])
        ps.append(n / total)
    return entropy(ps) if entropy(ps) > 0 else 1


def c45(target_table: pd.DataFrame, to_which_column: str, range_func) -> Tuple[list, List[Tuple[str, pd.DataFrame]], Any]:
    """
    Calculate the c45 tree node
    Args:
        target_table:
        to_which_column:
        range_func: Return true if value in the range else false

    Returns: List of children, list of children need to split, current node name

    """
    tmp_table = target_table.copy()
    unique_to_column_values = target_table[to_which_column].unique()

    igs = []
    e = get_initial_information(tmp_table, unique_to_column_values, column=to_which_column)
    print(f"Entropy:{e}")
    for col in tmp_table.columns:
        if col != to_which_column:
            print("==================================")
            ig = information_gain(original_entropy=e, target_table=tmp_table, from_which_column=col,
                                  to_which_column=to_which_column, print_info=False)
            split_info = calculate_split_info(target_table=target_table, column=col)
            ig = ig / split_info
            print(f"For attribute: {col} related to {to_which_column}")
            print(f"Split info: {split_info}")
            print(f"Information gain: {ig}")
            igs.append((col, ig))

    igs.sort(key=lambda e: e[1], reverse=True)
    if len(igs) == 0:
        return [], [], ""
    print("==================================")
    print(f"Will use attribute {igs[0][0]} as node")

    unique_values = tmp_table[igs[0][0]].unique()
    children = []
    need_to_split_children = []
    for v in unique_values:
        data = tmp_table[tmp_table[igs[0][0]] == v]
        score = calculate_percentage(target_table=data, to_which_column=to_which_column)
        if range_func(score):
            need_to_split_children.append((v, data))
        else:
            children.append((v, score, data))

        print()
        print(f"{igs[0][0]} {v}: {score} {to_which_column}")
        print(data)

    return children, need_to_split_children, igs[0][0]
