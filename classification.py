from treelib import Tree
from classification import decision_tree, c45, id3, cart
import pandas as pd
from sklearn import tree as sktree
from sklearn import preprocessing
import matplotlib.pyplot as plt
from graphviz import Digraph

if __name__ == '__main__':
    dot = Digraph(name="root")
    # table = pd.DataFrame(columns=["Race", "Income", "Child", "Insurance"],
    #                      data=[
    #                          ["black", "high", "no", "yes"],
    #                          ["white", "high", "yes", "yes"],
    #                          ["white", "low", "yes", "yes"],
    #                          ["white", "low", "yes", "yes"],
    #                          ["black", "low", "no", "no"],
    #                          ["black", "low", "no", "no"],
    #                          ["black", "low", "no", "no"],
    #                          ["white", "low", "no", "no"]
    #                      ])

    # table = pd.DataFrame(columns=["Child", "Id", "Insurance"],
    #                      data=[
    #                          ["n", "1", "y"],
    #                          ["y", "2", "y"],
    #                          ["y", "3", "y"],
    #                          ["y", "4", "y"],
    #                          ["n", "5", "n"],
    #                          ["n", "6", "n"],
    #                          ["n", "7", "n"],
    #                          ["n", "8", "n"]
    #                      ])

    # table = pd.DataFrame(columns=["No", "Study CS", "Age", "Income", "Buy Bitcoin"],
    #                      data=[
    #                          ["1", "yes", "old", "fair", "yes"],
    #                          ["2", "yes", "middle", "fair", "yes"],
    #                          ["3", "no", "young", "fair", "yes"],
    #                          ["4", "no", "young", "high", "yes"],
    #                          ["5", "yes", "old", "low", "no"],
    #                          ["6", "yes", "young", "low", "no"],
    #                          ["7", "no", "young", "fair", "no"],
    #                          ["8", "no", "middle", "low", "no"],
    #                      ])
    # table = table.drop(columns=["No"])

    table = pd.DataFrame(columns=["Race", "Income", "Insurance"],
                         data=[
                             ["black", "high", "yes"],
                             ["black", "high", "yes"],
                             ["black", "low", "yes"],
                             ["black", "low", "yes"],
                             ["white", "low", "no"],
                             ["white", "low", "no"],
                             ["white", "low", "no"],
                             ["white", "low", "no"]
                         ])

    decision_tree(treelib_tree=dot, target_table=table, to_which_column=table.columns[len(table.columns) - 1],
                  parent="Root",
                  calculate_func=id3, range_func=lambda s: 1 > s > 0)

    dot.render("test/id3.gv", view=False)
    dot = Digraph(name="root")
    decision_tree(treelib_tree=dot, target_table=table, to_which_column=table.columns[len(table.columns) - 1],
                  parent="Root",
                  calculate_func=cart, range_func=lambda s: 1 > s > 0)
    
    dot.render("test/cart.gv", view=False)
    # tree.show()
