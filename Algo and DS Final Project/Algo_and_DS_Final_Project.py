import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Define the nodes (A to W)
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges and their weights
edges = [
    ('A', 'B', 6),
    ('A', 'F', 5),
    ('F', 'G', 8),
    ('G', 'B', 6),
    ('G', 'H', 9),
    ('B', 'C', 5),
    ('H', 'C', 5),
    ('C', 'D', 7),
    ('H', 'I', 12),
    ('D', 'I', 8),
    ('D', 'E', 7),
    ('I', 'E', 6),
    ('F', 'J', 7),
    ('J', 'K', 5),
    ('G', 'K', 8),
    ('K', 'L', 7),
    ('M', 'L', 7),
    ('I', 'M', 10),
    ('M', 'N', 9),
    ('N', 'E', 15),
    ('J', 'O', 7),
    ('O', 'P', 13),
    ('P', 'Q', 8),
    ('P', 'L', 7),
    ('Q', 'R', 9),
    ('R', 'N', 7),
    ('O', 'S', 9),
    ('S', 'T', 9),
    ('T', 'U', 8),
    ('U', 'V', 8),
    ('U', 'P',11),
    ('V', 'W', 5),
    ('R', 'W', 10),
    ]

# Add weighted edges to the graph
G.add_weighted_edges_from(edges)

# Compute the layout for visualization
pos = nx.spring_layout(G)

# Define edge labels
edge_labels = {(n1, n2): d['weight'] for n1, n2, d in G.edges(data=True)}

# Draw the graph with labels and edge labels
nx.draw(G, pos, with_labels=True,node_color="skyblue",node_size=400,edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5,
                             font_color='red', font_size=9, font_weight='bold')

#TASK TWO: SEARCH LOGIC

#Asks the user to input the start node

#creates function that
def FindShortestPath():
    isShortesPath = 0
    checkShortestLetter = " "
    #asks user to input the node they want to start at
    startNode = input("What node would you like to start on?: ").upper()

    #A list of the destinations
    chargeStationList = ["H", "K", "Q", "T"]

    print("-------------------------------LIST OF PATHS-------------------------------")
    for i in chargeStationList:
            print("Path to Charger from " + startNode + " to node " + i + " is:", nx.dijkstra_path(G, startNode, i, "weight"))
            print("Distance from Node " + startNode + " " + "to node " + i + ": ", nx.dijkstra_path_length(G, startNode, i))

    for i in chargeStationList:
        #checks if it is the first run through
        if i == "H":
            #sets up values for the first pass
            isShortesPath = nx.dijkstra_path_length(G, startNode, i)
            checkShortestLetter = i
        else:
            #checks if the shortest path is greater is so then update values
            if isShortesPath > nx.dijkstra_path_length(G, startNode, i):
                isShortesPath = nx.dijkstra_path_length(G, startNode, i) #sets the new shortest path to var
                checkShortestLetter = i
    #prints the shortest path
    print("-------------------------------SHORTEST PATH-------------------------------")
    print("The shortest path to Charger from " + startNode + " is: ", nx.dijkstra_path(G, startNode, checkShortestLetter, "weight"))
    print("Distance from Node " + startNode + " " + "to Node " + checkShortestLetter + ": ", nx.dijkstra_path_length(G, startNode, checkShortestLetter))

FindShortestPath()

# Show the plot
plt.show()