import networkx as nx
import matplotlib.pyplot as plt



# Create an empty graph
G = nx.Graph()

def nodes():
    with open('nodes.txt','r') as f:
        data = f.read().split(',')
    return data

# Add nodes to the graph
G.add_nodes_from(nodes())

def edges():
    with open('edges.txt','r') as f:
        lines = f.readlines()
    return [(node1.strip(), node2.strip(), int(weight)) for node1, node2, weight in (line.split(',') for line in lines if len(line.split(',')) == 3)]

# Add weighted edges to the graph
G.add_weighted_edges_from(edges())

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
#creates function that
def FindShortestPath():
    isShortesPath = 0
    checkShortestLetter = " "
    #asks user to input the node they want to start at
    startNode = input("What node would you like to start on?: ").upper()

    #A list of the destinations
    chargeStationList = ["H", "K", "Q", "T"]

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
    print("Path to Charger from " + startNode + ": ", nx.dijkstra_path(G, startNode, checkShortestLetter, "weight"))
    print("Distance from Node " + startNode + " " + "to Node " + checkShortestLetter + ": ", nx.dijkstra_path_length(G, startNode, checkShortestLetter))
        
        
FindShortestPath()

# Show the plot
plt.show()
print("Nodes:", nodes())
print("Edges:", edges())
