from typing import List
from classification.entropy import entropy
import pandas as pd


def information_gain(original_entropy: float, target_table: pd.DataFrame, from_which_column: str,
                     to_which_column: str, print_info=True, calc_func=entropy) -> float:
    """
    Calculate the information gain from [which column] [to which column]. For example, we want to calculate
    the information gain for attribute Race in related to attribute Insurance
    Args:
        calc_func: Calculation function used to calculate information gain, Default is entropy.
        to_which_column: To which column
        original_entropy: Original entropy
        target_table: The data
        from_which_column:
        print_info: Will print info

    Returns: Information gain
    """
    unique_from_column_values = target_table[from_which_column].unique()
    unique_to_column_values = target_table[to_which_column].unique()
    total_number = len(target_table)
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

        e = calc_func(probabilities)
        it += e * total_ufc_number / total_number

    if print_info:
        print(f"For attribute: {from_which_column} related to {to_which_column}")
        print(f"Information: {it}")
        print(f"Information gain: {original_entropy - it}")
    return original_entropy - it


def get_initial_information(target_table: pd.DataFrame, unique_values: List[str], column: str,
                            calc_func=entropy) -> float:
    """
    Get entropy by given unique values from the table for the target column
    Args:
        calc_func: calculation function
        target_table:
        unique_values:
        column:

    Returns:

    """
    ps = []
    total = len(target_table)
    for v in unique_values:
        n = len(target_table[target_table[column] == v])
        ps.append(n / total)

    return calc_func(ps)


def calculate_percentage(target_table: pd.DataFrame, to_which_column: str):
    """
    Calculate the final score for the target column. 0 and 1 means no split needed
    Args:
        target_table:
        to_which_column:
        unique_values:

    Returns:

    """
    unique_values = target_table[to_which_column].unique()
    total = len(target_table)
    max_score = -1
    for v in unique_values:
        n = len(target_table[target_table[to_which_column] == v])
        s = n / total
        if s > max_score:
            max_score = s
    return max_score
