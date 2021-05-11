from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

import networkx as nx  # for drawing graphs
import matplotlib.pyplot as plt  # for drawing graphs

if __name__ == '__main__':
    ap = BbnNode(Variable(0, 'ap', ['yes', 'no']), [0.3, 0.7])
    p = BbnNode(Variable(1, 'p', ['yes', 'no']), [0.6, 0.4])
    sir = BbnNode(Variable(2, 'sir', ['yes', 'no']), [0.7, 0.3, 0.45, 0.55, 0.55, 0.45, 0.2, 0.8])
    wbc = BbnNode(Variable(3, 'wbc', ['high', 'low']), [0.6, 0.4, 0.3, 0.7])
    bbn = Bbn() \
        .add_node(ap) \
        .add_node(p) \
        .add_node(sir) \
        .add_node(wbc) \
        .add_edge(Edge(ap, sir, EdgeType.DIRECTED)) \
        .add_edge(Edge(p, sir, EdgeType.DIRECTED)) \
        .add_edge(Edge(sir, wbc, EdgeType.DIRECTED))
    options = {
        "font_size": 16,
        "node_size": 3000,
        "node_color": "white",
        "edgecolors": "black",
        "edge_color": "red",
        "linewidths": 5,
        "width": 5, }

    n, d = bbn.to_nx_graph()
    nx.draw(n, with_labels=True, labels=d, **options)
    join_tree = InferenceController.apply(bbn)
    ev = EvidenceBuilder() \
        .with_node(join_tree.get_bbn_node_by_name('ap')) \
        .with_evidence('yes', 1) \
        .build()

    ev2 = EvidenceBuilder() \
        .with_node(join_tree.get_bbn_node_by_name('p')) \
        .with_evidence('yes', 1) \
        .build()

    ev3 = EvidenceBuilder() \
        .with_node(join_tree.get_bbn_node_by_name('wbc')) \
        .with_evidence('high', 1) \
        .build()

    join_tree.set_observation(ev)
    join_tree.set_observation(ev2)
    join_tree.set_observation(ev3)

    # print the marginal probabilities
    for node in join_tree.get_bbn_nodes():
        potential = join_tree.get_bbn_potential(node)
        print(node)
        print(potential)
