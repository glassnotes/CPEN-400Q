import matplotlib.pyplot as plt
from pennylane import numpy as np
import networkx as nx

def plot_graph(edges, solution_string=None):
    """Use NetworkX to plot a graph and highlight the coloured vertices.
    
    Args:
        edges (List[(int, int)]): A list of edges comprising a graph.
        solution_string (str): A bit string where '1' in position i indicates 
            vertex i should be coloured.
    """
    G = nx.Graph(edges)
    
    colours = None
    if solution_string:
        colours = ["red" if c == '1' else "gray" for c in solution_string]
        
    nx.draw(G, node_color=colours, with_labels=True)


def plot_probs(probs):
    """Produces a bar plot of measurement outcome probabilities
    labelled by bitstrings.
    
    Args:
        probs (array[float]): An array of measurement outcome probabilities.
    """
    n_qubits = int(np.log2(len(probs)))
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.bar(range(len(probs)), probs)
    ax.set_xticks(range(len(probs)))
    ax.set_xticklabels(
        [str(np.binary_repr(x, n_qubits)) for x in range(len(probs))], 
        rotation=90
    )