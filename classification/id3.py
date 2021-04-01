from typing import List, Tuple
import pandas as pd
import numpy as np
from treelib import Tree

from classification.entropy import entropy


def information_gain(original_entropy: float, target_table: pd.DataFrame, from_which_column: str,
                     to_which_column: str, print_info=True) -> float:
    """
    Calculate the information gain from [which column] [to which column]. For example, we want to calculate
    the information gain for attribute Race in related to attribute Insurance
    Args:
        to_which_column: To which column
        original_entropy: Original entropy
        target_table: The data
        from_which_column:
        print_info: Will print info

    Returns: Information gain
    """
    unique_from_column_values = target_table[from_which_column].unique()
    unique_to_column_values = target_table[to_which_column].unique()
    total_number = len(table)
    it = 0

    for ufc in unique_from_column_values:
        values = target_table[target_table[from_which_column] == ufc]
        total_ufc_number = len(values)
        probabilities = []

        for utc in unique_to_column_values:
            related_values = target_table[
                (target_table[from_which_column] == ufc) & (target_table[to_which_column] == utc)]
            filter_number = len(related_values)
            probability = filter_number / total_ufc_number
            probabilities.append(probability)

        e = entropy(probabilities)
        it += e * total_ufc_number / total_number

    if print_info:
        print(f"For attribute: {from_which_column} related to {to_which_column}")
        print(f"Information: {it}")
        print(f"Information gain: {original_entropy - it}")
    return original_entropy - it


def get_entropy(target_table: pd.DataFrame, unique_values: List[str], column: str) -> float:
    ps = []
    total = len(target_table)
    for v in unique_values:
        n = len(target_table[target_table[column] == v])
        ps.append(n / total)

    return entropy(ps)


def calculate_percentage(target_table: pd.DataFrame, to_which_column: str,
                         unique_values: List[str]):
    max_score = 0
    total = len(target_table)
    for v in unique_values:
        n = len(target_table[target_table[to_which_column] == v])
        s = n / total
        if s > max_score:
            max_score = s
    return max_score


def decision_tree(target_table: pd.DataFrame, to_which_column: str, id3_tree, calculate_func, parent=None, ):
    """
    Draw id3 tree
    Args:
        calculate_func: Calculate function, used to calculate the tree split
        target_table: data
        to_which_column: Which column need to use
        id3_tree: id3 tree object. Used to draw the tree diagram
        parent: id3 tree's parent

    Returns:

    """
    tmp_table = target_table.copy()
    children, need_to_split, node_name = calculate_func(target_table=tmp_table, to_which_column=to_which_column)
    id3_tree.create_node(node_name, node_name, parent=parent)

    for t in need_to_split:
        t = t.drop(columns=[node_name])
        print()
        decision_tree(target_table=t, to_which_column=to_which_column, id3_tree=id3_tree, parent=node_name,
                      calculate_func=calculate_func)


def id3(target_table: pd.DataFrame, to_which_column: str) -> Tuple[List[pd.DataFrame], List[pd.DataFrame], str]:
    """
    Calculate the tree node
    Args:
        target_table:
        to_which_column:

    Returns: List of children, list of children need to split, current node name

    """
    tmp_table = target_table.copy()
    unique_to_column_values = target_table[to_which_column].unique()

    igs = []
    e = get_entropy(tmp_table, unique_to_column_values, column=to_which_column)
    print(f"Entropy:{e}")
    for col in tmp_table.columns:
        if col != to_which_column:
            print("==================================")
            ig = information_gain(original_entropy=e, target_table=tmp_table, from_which_column=col,
                                  to_which_column=to_which_column)
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
        score = calculate_percentage(data, to_which_column, unique_values)
        if 1 > score > 0:
            need_to_split_children.append(data)
        children.append(data)
        print(f"{igs[0][0]} {v}: {score} {to_which_column}")
        print(data)

    return children, need_to_split_children, igs[0][0]


if __name__ == '__main__':
    tree = Tree()
    tree.create_node("Root", "Root")
    original_e = entropy([0.5, 0.5])
    table = pd.DataFrame(columns=["Race", "Income", "Child", "Insurance"],
                         data=[
                             ["black", "high", "no", "yes"],
                             ["white", "high", "yes", "yes"],
                             ["white", "low", "yes", "yes"],
                             ["white", "low", "yes", "yes"],
                             ["black", "low", "no", "no"],
                             ["black", "low", "no", "no"],
                             ["black", "low", "no", "no"],
                             ["white", "low", "no", "no"]
                         ])

    decision_tree(id3_tree=tree, target_table=table, to_which_column="Insurance", parent="Root", calculate_func=id3)
    tree.show()
