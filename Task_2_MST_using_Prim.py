import heapq
import networkx as nx
import matplotlib.pyplot as plt


def add_node_positions():

    node_pos = {
        "A" : [ 0, 2],
        "B" : [ 1, 3],
        "G" : [ 1, 1],
        "D" : [ 2, 3],
        "E" : [ 2, 1],
        "C" : [ 2, 2],
        "F" : [ 3, 3],
        "Z" : [ 3, 1]      
    }

    return node_pos    

def create_original_graph(G, edges, node_pos):
    
    G.add_weighted_edges_from(edges)

    pos = nx.circular_layout(G)

    nx.draw(G,
            pos=node_pos,
            with_labels=True,
            node_size=700,
            node_color='lightblue',
            font_size=12,
            font_weight='bold'
            )

    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(G, pos=node_pos, edge_labels=edge_labels)
    
    plt.suptitle("Original graph",color='red')
    plt.margins(0.2, 0.2)
    plt.show()


if __name__ == '__main__':


    fig = plt.figure(figsize=(5, 4), frameon=False)
    
    # Create a graph objects
    G = nx.Graph()
    G_mst = nx.Graph()

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
    create_original_graph(G, edges, node_pos)

    # create adjancey list to hold each nodes' neigbours
    
    
    # find mst (G, adj list, start node)
    
    
    # show final mst
