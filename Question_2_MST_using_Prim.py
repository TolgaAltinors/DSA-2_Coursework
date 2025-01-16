import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Helper: 
    def __init__(self, pos='', nodes=[]): 
        self.pos = pos
        self.nodes = nodes

    # getter method 
    def get_pos(self): 
        return self.pos

    # setter method 
    def set_pos(self, x): 
        self.pos = x

    def set_nodes(self, adj_list):
        
        for s, d, w in adj_list:
            if s not in self.nodes:
                self.nodes.append(s)
            if d not in self.nodes:
                self.nodes.append(d)
        self.nodes = sorted(self.nodes)

# Display original graph
def create_original_graph(G, edges):
# def create_original_graph(G, edges, node_pos):
    
    fig = plt.figure(figsize=(6, 5))
    
    G.add_weighted_edges_from(edges)

    pos = nx.circular_layout(G)
    
    # assign node positions so we can use then in the MST
    node_class.set_pos(pos)
    
    # Draw graph
    nx.draw(G,
            pos=node_class.get_pos(),
            with_labels=True,
            node_size=700,
            node_color='lightblue',
            font_size=12,
            font_weight='bold'
            )

    # get the weight' attribute for edges
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Add egde lables to graph
    nx.draw_networkx_edge_labels(G, pos=node_class.get_pos(), edge_labels=edge_labels)
    
    print("*****")
    print("*****")
    print("***** The MST will show on a different figure after a 3 second pause.")
    print("*****")
    print("*****")
    
    plt.suptitle("Original graph",color='red')
    plt.margins(0.2, 0.2)
    plt.show(block=False)
    plt.pause(8)

# Create adjacency list
def create_adjacency_list(G):

    # Create adjacency list for each node's neighbours including distance 
    # Store each neighbour as a set with weight and node name
    # Store weight as first value as the heapq will use that for priority
    adj_list = { node:[] for node in G.nodes }

    # loop through start node, destination node and weight properties
    for s, d, w in G.edges(data="weight"):
            
        # add the weight and destination node
        neighbour_to_add = (w, d)
        adj_list[s].append(neighbour_to_add)
        # also add the opposite direction
        neighbour_to_add = (w, s)
        adj_list[d].append(neighbour_to_add)

    return adj_list

# Find MST based on Prim's algorithm
def find_mst(G, adj_list, start_node):
    
    if node_data_type == "int":
        start_node = str(start_node)
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
        
        # split nodes (destination and origin)
        node, parent_node = nodes.split('-')
        
        print(f"Popping node {node} with weigth {dist} from the heap")

        # initialise list for creating final mst
        path = [] # [parent_node, destination_node, distance]
        
        if node_data_type == "int":
            parent_node = int(parent_node)
            node = int(node)

        # Create origin to destination node path with weight
        path.append(parent_node)
        path.append(node)            
        path.append(dist)
        mst_edges.append(path)
        
        # update list of visited nodes
        visited.append(node)
        
        for next_dist, next_node in adj_list[node]:
            
            if next_node not in visited:
                
                print(f"Pushing node {str(next_node)} with weigth {str(next_dist)} onto the heap")
                # This keeps track of the previous node
                next_node = str(next_node) + '-' + str(node)
                heapq.heappush(minHeap, [next_dist, next_node])
                
    return mst_edges

# Create final MST graph
# def create_final_mst_graph(G_mst, mst_edges, node_pos):
def create_final_mst_graph(G_mst, mst_edges):

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
                pos=node_class.get_pos(),
                with_labels=True,
                node_size=700,
                node_color=node_colour,  #'lightgreen',
                font_size=10,
                font_weight='bold')
        
        mst_edge_labels = nx.get_edge_attributes(G_mst, 'weight')
        nx.draw_networkx_edge_labels(G_mst, pos=node_class.get_pos(), edge_labels=mst_edge_labels)

        print("*****")
        print(f"***** MST build step: node ({start_node}) --> ({end_node}) with weight of ({attribute})")
        print("*****")

        if node_index == len(mst_edges) -1:
            print("*****")
            print(f"***** Completed the MST build with total distance of {str(total_distance)}.")
            print("*****")
        
        plt.suptitle(f"Minimum Spanning Tree - Prim's Algorithm - Distance = {str(total_distance)}", color='green')        
        plt.margins(0.2, 0.2)
        plt.show(block=False)
        if node_index == len(mst_edges)-1:
            plt.pause(final_pause)
        else:
            plt.pause(step_pause)

def generate_connected_graph(n_nodes,n_edges):
    import random
    while True:
        
        G = nx.gnm_random_graph(n_nodes, n_edges, seed=10)
        if nx.is_connected(G):
            # add random weight
            for (s, d, w) in G.edges(data=True):
                w['weight'] = random.randint(0,20)
    
            return G


if __name__ == '__main__':
    
    # Pause timings
    step_pause = 4
    final_pause = 30
    
    edges = [("A", "B", 1), ("A", "G", 10), ("B", "D", 3), ("G", "E", 3),
            ("A", "C", 5), ("D", "C", 8), ("C", "E", 6), ("D", "F", 1),
            ("E", "Z", 1), ("F", "Z", 6), ("C", "Z", 9)
            ]

    # for testing random graphs
    # edges = []
    # G = generate_connected_graph(10, 9)
    # for node in G.nodes():
    #     neighbour_list = [n for n in G.neighbors(node)]
    #     for s, d, w in G.edges(data="weight"):
    #         if s == node and d in neighbour_list:
    #             edges.append((s, d, w))

    node_class = Helper()
    # Set available nodes based on available edges. We use this to give the user input
    node_class.set_nodes(edges)
    
    # Create a graph objects
    G = nx.Graph()
    G_mst = nx.Graph()

        # create a list of potential edges for user o select as a starting point
    print("Please select one of the edges as starting node")

    for node in node_class.nodes:
        print (node)
    start_node = input("... ")

    # additional logic to cater for node names that are type integer
    node_data_type="str"
    if type(node_class.nodes[0]) == int:
        node_data_type="int"
    
    # display original graph
    create_original_graph(G, edges)

    # create adjacency list to hold each nodes' neigbours
    adj_list = create_adjacency_list(G)
    
    # find mst (G, adj list, start node)
    mst_edges = find_mst(G, adj_list, start_node)
    
    # show final mst
    create_final_mst_graph(G_mst, mst_edges)
