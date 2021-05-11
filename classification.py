from treelib import Tree
from classification import decision_tree, c45, id3, cart
import pandas as pd
from sklearn import tree as sktree
from sklearn import preprocessing
import matplotlib.pyplot as plt
from graphviz import Digraph

if __name__ == '__main__':
    dot = Digraph(name="root")

    table = pd.DataFrame(columns=["No", "Age", "Gender", "MMR_Vaccine", "Has Measles"],
                         data=[
                             ["1", "y", "m", "n", "yes"],
                             ["2", "o", "m", "n", "yes"],
                             ["3", "y", "f", "y", "yes"],
                             ["4", "o", "f", "n", "yes"],
                             ["5", "y", "f", "y", "no"],
                             ["6", "y", "f", "y", "no"],
                             ["7", "o", "f", "y", "no"],
                             ["8", "o", "f", "y", "no"],
                         ])
    table = table.drop(columns=["No"])

    # If the 75% of itemsets with same label, we stop spliting
    decision_tree(treelib_tree=dot, target_table=table, to_which_column=table.columns[len(table.columns) - 1],
                  parent="Root",
                  calculate_func=cart, range_func=lambda s: 0.75 > s > 0.25)

    dot.render("test/c45.gv", view=False)
