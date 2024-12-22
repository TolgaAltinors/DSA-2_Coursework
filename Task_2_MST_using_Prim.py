import networkx as nx
import matplotlib.pyplot as plt

def add_node_positions():
    start_x = 0.05
    start_y = 0.05

    x_adj = 0.0013
    y_adj = 0.0011

    node_pos = {"A" : [start_x, start_y]}

    next_x = start_x + x_adj
    next_y = start_y + y_adj
    node_pos["B"] = [next_x, next_y]

    next_x = start_x + x_adj
    next_y = start_y - y_adj
    node_pos["G"] = [next_x, next_y]

    x_adj = 0.0030
    next_x = next_x + x_adj
    next_y = start_y + y_adj
    node_pos["D"] = [next_x, next_y]

    next_y = start_y - y_adj
    node_pos["E"] = [next_x, next_y]

    next_y = start_y
    node_pos["C"] = [next_x, next_y]

    x_adj = 0.0025
    next_x = next_x + x_adj
    next_y = start_y + y_adj
    node_pos["F"] = [next_x, next_y]

    next_y = start_y - y_adj
    node_pos["Z"] = [next_x, next_y]

    return node_pos    


def display_graph(edges, node_pos):
    
    G = nx.Graph()

    G.add_weighted_edges_from(edges)

    pos = nx.circular_layout(G)

    # overwrite node x&y positions
    for k, v in pos.items():
        pos[k] = node_pos[k]

    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
    


if __name__ == '__main__':

    nodes = ["A", "B", "G", "D", "E", "C", "F", "Z"]

    edges = [("A", "B", 1),
            ("A", "G", 10),
            ("B", "D", 3),
            ("G", "E", 3),
            ("A", "C", 5),
            ("D", "C", 8),         
            ("C", "E", 6),        
            ("D", "F", 1),
            ("E", "Z", 1),
            ("F", "Z", 6),
            ("C", "Z", 9)
            ]

    # add node positions to dictionary
    node_pos = add_node_positions()

    # display original graph
    display_graph(edges, node_pos)
