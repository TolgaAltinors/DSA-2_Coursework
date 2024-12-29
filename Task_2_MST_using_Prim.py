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
    
    fig = plt.figure(figsize=(5, 4), frameon=False)
    
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
    
    plt.suptitle("Original graph - Close window to continue",color='red')
    plt.margins(0.2, 0.2)
    plt.show()

# CREATE ADJACENCY LIST
def create_adjacency_list(G):

    adj_list = { node:[] for node in G.nodes }

    # loop through nodes
    for node in G.nodes:
        
        # find all neighbors of node 
        neighbor_list = [n for n in G.neighbors(node)]
        
        print (f"Neighbors of ({node}) = {neighbor_list}")
        
        # loop through start node, destination node and weight properties
        for s, d, w in G.edges(data="weight"):
            
            if s == node and d in neighbor_list:
                
                # add the weight and destination node
                neighbor_to_add = (w, d)
                adj_list[node].append(neighbor_to_add)
                # also add the opposite direction
                neighbor_to_add = (w, node)
                adj_list[d].append(neighbor_to_add)

    return adj_list


def find_mst(G, adj_list, start_node):
    
    # add start node twice - second one representing the parent node
    start_node = start_node + '-' + start_node
    
    mst_edges = []  # return valus to draw mst
    visited = []
    
    # initialize heap value
    minHeap = [[0, start_node]] # distance, start_node

    number_of_nodes = len(adj_list)

    while len(visited) < number_of_nodes:
        
        # retrieve minimum valued node from heap
        dist, nodes = heapq.heappop(minHeap)
        
        # split nodes
        node, parent_node = nodes.split('-')
        
        print(f"Popping node {node} with weigth {dist} from the heap")

        # create list for creating final mst
        path = [] # [start_node, destination_node, distance]
        
        path.append(parent_node)
        path.append(node)
        path.append(dist)
        mst_edges.append(path)
        
        visited.append(node)
        
        for next_dist, next_node in adj_list[node]:
            
            if next_node not in visited:
                
                print(f"Pushing node {next_node} with weigth {next_dist} onto the heap")
                next_node = next_node + '-' + node
                heapq.heappush(minHeap, [next_dist, next_node])
                
    return mst_edges



def create_final_mst_graph(G_mst, mst_edges, node_pos):

    fig = plt.figure(figsize=(5, 4), frameon=False)
    
    # Add edges based on mst values
    for node in range(1,len(mst_edges)):
        
        node_elements = mst_edges[node]
        start_node = node_elements[0]
        end_node = node_elements[1]
        attribute = node_elements[2]

        G_mst.add_edge(start_node, end_node, weight=attribute)        

    pos = nx.spring_layout(G_mst)
    nx.draw(G_mst,
            pos=node_pos,
            with_labels=True,
            node_size=700,
            node_color='lightgreen',
            font_size=10,
            font_weight='bold')
    
    mst_edge_labels = nx.get_edge_attributes(G_mst, 'weight')
    nx.draw_networkx_edge_labels(G_mst, pos=node_pos, edge_labels=mst_edge_labels)
    
    plt.suptitle("Minimum Spanning Tree - Prim's Algorithm", color='green')
    plt.margins(0.2, 0.2)
    plt.show()


if __name__ == '__main__':
    
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
    adj_list = create_adjacency_list(G)
    
    # find mst (G, adj list, start node)
    mst_edges = find_mst(G, adj_list, 'A')
    
    # show final mst
    create_final_mst_graph(G_mst, mst_edges, node_pos)