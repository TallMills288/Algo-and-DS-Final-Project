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

# Show the plot
plt.show()