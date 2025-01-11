import heapq
import networkx as nx
import matplotlib.pyplot as plt


# Add fix positions for nodes so it displays the same way every time
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

# Display original graph
def create_original_graph(G, edges, node_pos):
    
    fig = plt.figure(figsize=(6, 5))
    
    G.add_weighted_edges_from(edges)

    pos = nx.circular_layout(G)

    # Draw graph
    nx.draw(G,
            pos=node_pos,
            with_labels=True,
            node_size=700,
            node_color='lightblue',
            font_size=12,
            font_weight='bold'
            )

    # get the weight' attribute for edges
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Add egde lables to graph
    nx.draw_networkx_edge_labels(G, pos=node_pos, edge_labels=edge_labels)
    
    print("*****")
    print("*****")
    print("***** The MST will show on a different figure after a 3 second pause.")
    print("*****")
    print("*****")
    
    plt.suptitle("Original graph",color='red')
    plt.margins(0.2, 0.2)
    plt.show(block=False)
    plt.pause(3)

# Create adjacency list
def create_adjacency_list(G):

    # Create adjaceny list for each node's neigbours including distance 
    # Store each neighbour as a set with weight and node name
    # Store weight as first value as the heapq will use that for priority
    adj_list = { node:[] for node in G.nodes }

    # loop through nodes
    for node in G.nodes:
        
        # find all neighbours of node 
        neighbour_list = [n for n in G.neighbors(node)]
        
        print (f"neighbours of ({node}) = {neighbour_list}")
        
        # loop through start node, destination node and weight properties
        for s, d, w in G.edges(data="weight"):
            
            if s == node and d in neighbour_list:
                
                # add the weight and destination node
                neighbour_to_add = (w, d)
                adj_list[node].append(neighbour_to_add)
                # also add the opposite direction
                neighbour_to_add = (w, node)
                adj_list[d].append(neighbour_to_add)

    return adj_list

# Find MST based on Prim's algorithm
def find_mst(G, adj_list, start_node):
    
    # add start node twice - second one representing the parent node
    start_node = start_node + '-' + start_node
    
    mst_edges = []  # return values to draw mst
    visited = []
    
    # initialize heap value
    minHeap = [[0, start_node]] # distance, start_node(start_node(start_node and parent_node))

    number_of_nodes = len(adj_list)

    while len(visited) < number_of_nodes:
        
        # retrieve minimum valued node from heap
        dist, nodes = heapq.heappop(minHeap)
        
        # split nodes
        node, parent_node = nodes.split('-')
        
        print(f"Popping node {node} with weigth {dist} from the heap")

        # initialise list for creating final mst
        path = [] # [parent_node, destination_node, distance]
        
        path.append(parent_node)
        path.append(node)
        path.append(dist)
        mst_edges.append(path)
        
        visited.append(node)
        
        for next_dist, next_node in adj_list[node]:
            
            if next_node not in visited:
                
                print(f"Pushing node {next_node} with weigth {next_dist} onto the heap")
                # This keeps track of the previous node
                next_node = next_node + '-' + node
                heapq.heappush(minHeap, [next_dist, next_node])
                
    return mst_edges

# Create final MST graph
def create_final_mst_graph(G_mst, mst_edges, node_pos):

    fig = plt.figure(figsize=(6, 5))
    
    total_distance = 0
    
    # Add edges based on mst values
    for node_index in range(1,len(mst_edges)):
        
        node_elements = mst_edges[node_index]
        start_node = node_elements[0]
        end_node = node_elements[1]
        attribute = node_elements[2]

        if node_index == 1:
            print("*****")
            print(f"***** Starting MST build with node ({start_node}).")
            print("*****")

        # distance covered
        total_distance += attribute
        
        G_mst.add_edge(start_node, end_node, weight=attribute)
        
        # display the last added node as red
        node_colour = []
        for ind in range(node_index):
            node_colour.append('lightgreen')

        node_colour.append('red')

        nx.draw(G_mst,
                pos=node_pos,
                with_labels=True,
                node_size=700,
                node_color=node_colour,  #'lightgreen',
                font_size=10,
                font_weight='bold')
        
        mst_edge_labels = nx.get_edge_attributes(G_mst, 'weight')
        nx.draw_networkx_edge_labels(G_mst, pos=node_pos, edge_labels=mst_edge_labels)

        print("*****")
        print(f"***** Adding node ({start_node}) --> ({end_node}) with weight {attribute} to MST.")
        print("*****")

        if node_index == len(mst_edges) -1:
            print("*****")
            print(f"***** Completed the MST build with total distance of {str(total_distance)}.")
            print("*****")
        
        plt.suptitle(f"Minimum Spanning Tree - Prim's Algorithm - Distance = {str(total_distance)}", color='green')        
        plt.margins(0.2, 0.2)
        plt.show(block=False)
        if node_index == len(mst_edges)-1:
            plt.pause(5)
        else:
            plt.pause(2)


if __name__ == '__main__':
    
    from random import randint
    # Create a graph objects
    G = nx.Graph()
    #G = nx.gnp_random_graph(10, 0.3, 20)
    # G = nx.complete_graph(10)

    pos = nx.circular_layout(G)    
    
    # nx.set_edge_attributes(G, {e: {'weight': randint(1, 10)} for e in G.edges})
    
    # fig = plt.figure(figsize=(6, 5))
    
    # nx.draw(G,pos =pos,
    #                 with_labels=True,
    #                 node_size=700,
    #                 node_color='lightgreen',
    #                 font_size=10,
    #                 font_weight='bold')
            
    # mst_edge_labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=mst_edge_labels)    
    
    # plt.suptitle("Original graph",color='red')
    # plt.margins(0.2, 0.2)
    # plt.show(block=False)
    # plt.pause(3)

    
    G_mst = nx.Graph()

    # nodes = ["A", "B", "G", "D", "E", "C", "F", "Z"]

    # edges = [("A", "B", 1), ("A", "G", 10), ("B", "D", 3), ("G", "E", 3),
    #         ("A", "C", 5), ("D", "C", 8), ("C", "E", 6), ("D", "F", 1),
    #         ("E", "Z", 1), ("F", "Z", 6), ("C", "Z", 9)
    #         ]

    edges = [('1', '2', 1), ('1', '7', 10), ('2', '4', 3), ('7', '5', 3),
            ('1', '3', 5), ('4', '3', 8), ('3', '5', 6), ('4', '6', 1),
            ('5', '0', 1), ('6', '0', 6), ('3', '0', 9)
            ]
    
    # # add node positions to dictionary
    # node_pos = add_node_positions()

    # # display original graph
    # create_original_graph(G, edges, node_pos)

    # create adjacency list to hold each nodes' neigbours
    adj_list = create_adjacency_list(G)
    
    # find mst (G, adj list, start node)
    mst_edges = find_mst(G, adj_list, '1')
    
    # show final mst
#    create_final_mst_graph(G_mst, mst_edges, node_pos)
    create_final_mst_graph(G_mst, mst_edges, pos)