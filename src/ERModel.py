__author__ = 'maria slanova'

import networkx as nx
import matplotlib.pyplot as plt
import math


def erdos_renyi_model(nodes, max_nodes, delta):
    """
    :param nodes: starting number of nodes in the graph
    :param max_nodes: maximum number of nodes in the graph
    :param delta: a step for increasing the number of nodes in each next graph
    :return: list of average shortest paths for each graph
    """
    # delta - step in nodes
    avg_shortest_path = []
    num_nodes = []
    while nodes <= max_nodes:
        p = 2.8 * math.log(nodes) / nodes
        my_graph = nx.erdos_renyi_graph(nodes, p, seed=None, directed=False)
        avg_sht = nx.average_shortest_path_length(my_graph, weight=None)
        avg_shortest_path.append(avg_sht)
        num_nodes.append(nodes)
        nodes += delta
    print(avg_shortest_path)

    plt.plot(num_nodes, avg_shortest_path, 'bs')

    plt.show()
    return avg_shortest_path

a = erdos_renyi_model(20, 1000, 20)


