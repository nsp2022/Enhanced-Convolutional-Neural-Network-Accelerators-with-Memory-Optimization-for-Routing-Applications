import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from tabulate import tabulate
from save_load import *

def generate_random_graph(num_nodes, num_edges):
    G = nx.gnm_random_graph(num_nodes, num_edges)
    return G

def plot_graph_with_highlighted_path(G, source_node, target_node, shortest_path):
    pos = nx.spring_layout(G)

    # Plot the graph
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000)

    # Highlight the nodes along the shortest path with a different node color
    node_colors = ['red' if node in shortest_path else 'skyblue' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000)

    # Highlight the source and destination nodes with different node colors
    nx.draw_networkx_nodes(G, pos, nodelist=[source_node], node_color='green', node_size=1000, label='Source')
    nx.draw_networkx_nodes(G, pos, nodelist=[target_node], node_color='green', node_size=1000, label='Destination')

    # Add labels to the source and destination nodes
    labels = {source_node: f"Source {source_node}", target_node: f"Destination {target_node}"}
    nx.draw_networkx_labels(G, pos, labels=labels, font_color='black', font_size=12)

    #plt.legend()  # Show legend with source and destination labels
    plt.show()

def DSR():
    num_nodes = 20
    num_edges = 30
    random_graph = generate_random_graph(num_nodes, num_edges)

    # Choose random source and destination nodes
    source_node = random.choice(list(random_graph.nodes()))
    target_node = random.choice(list(random_graph.nodes()))
    while source_node == target_node:
        target_node = random.choice(list(random_graph.nodes()))

    # Find the shortest path
    shortest_path = nx.shortest_path(random_graph, source=source_node, target=target_node, method='dijkstra')

    # Print the source, destination, and shortest path
    print(f"Source Node: {source_node}")
    print(f"Destination Node: {target_node}")
    print(f"Shortest Path: {shortest_path}")

    # Plot the graph with the highlighted source, destination, and shortest path nodes
    plot_graph_with_highlighted_path(random_graph, source_node, target_node, shortest_path)
    data1 = load("res1")
    data2 = load("res2")
    data3 = load("res3")
    data4 = load("res4")

    headers = ["Utilization", "Available", "Utilization (%)"]
    headers1 = ["before", "after"]
    print(tabulate(data1, headers, tablefmt="pretty"))
    print(tabulate(data2, headers, tablefmt="pretty"))
    print(tabulate(data3, headers1, tablefmt="pretty"))
    print("giga operations per second (before) :", data4[0])

    print("giga operations per second (after) :", data4[1])

