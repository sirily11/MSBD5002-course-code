from typing import Tuple, List
import pandas as pd

from classification.entropy import entropy
from classification.gini import gini
from classification.utils import information_gain, calculate_percentage, get_initial_information


def cart(target_table: pd.DataFrame, to_which_column: str, range_func) -> Tuple[
    List[pd.DataFrame], List[pd.DataFrame], str]:
    """
    Calculate the cart tree node
    Args:
        target_table:
        to_which_column:
        range_func:

    Returns: List of children, list of children need to split, current node name

    """
    tmp_table = target_table.copy()
    unique_to_column_values = target_table[to_which_column].unique()

    igs = []
    e = get_initial_information(tmp_table, unique_to_column_values, column=to_which_column, calc_func=gini)
    print(f"Entropy:{e}")
    for col in tmp_table.columns:
        if col != to_which_column:
            print("==================================")
            ig = information_gain(original_entropy=e, target_table=tmp_table, from_which_column=col,
                                  to_which_column=to_which_column, print_info=False, calc_func=gini)

            print(f"For attribute: {col} related to {to_which_column}")

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
        score, max_value = calculate_percentage(data, to_which_column)

        if range_func(score):
            need_to_split_children.append((v, data))
        else:
            children.append((v, score, data, max_value))
        print(f"{igs[0][0]} {v}: {score} {to_which_column}")
        print(data)

    return children, need_to_split_children, igs[0][0]
