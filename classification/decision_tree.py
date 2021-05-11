import pandas as pd
from graphviz import Digraph
import uuid


def decision_tree(target_table: pd.DataFrame, to_which_column: str, treelib_tree, calculate_func,
                  range_func=lambda s: 1 > s > 0, parent=None, ):
    """
    Draw tree
    Args:
        range_func: range function will take score as parameter, return true if the score within the range. If within the range, further split is needed
        calculate_func: Calculate function, used to calculate the tree split
        target_table: data
        to_which_column: Which column need to use
        treelib_tree: treelib tree object. Used to draw the tree diagram
        parent: id3 tree's parent

    Returns:

    """
    tmp_table = target_table.copy()
    children, need_to_split, node_name = calculate_func(target_table=tmp_table, to_which_column=to_which_column,
                                                        range_func=range_func)

    if node_name != "":
        treelib_tree.node(node_name, node_name)

    for v, score, c, max_v in children:
        name = f"{node_name}-{v}"
        label = f"{len(c)} {v}: {score * 100}% {max_v}"

        treelib_tree.node(name, label=label)
        treelib_tree.edge(node_name, name, label=v)

    # treelib_tree.create_node(node_name, node_name, parent=parent)

    for v, t in need_to_split:
        t = t.drop(columns=[node_name])
        print()
        next_child = decision_tree(target_table=t, to_which_column=to_which_column, treelib_tree=treelib_tree,
                                   parent=node_name,
                                   calculate_func=calculate_func)
        if next_child != "":
            treelib_tree.edge(node_name, next_child, v)

    return node_name
