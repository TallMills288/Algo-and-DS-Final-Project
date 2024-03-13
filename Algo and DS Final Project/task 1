import networkx as nx
import matplotlib.pyplot as plt

# this command  will Create an empty graph
Graph = nx.Graph()
#appends the txt file to the array 
#--------------------------------------------------------------------------------------------------------------------
# This command will open a txt file called product_data.txt and it will read from it
with open('network of nodes and edge.txt','r') as f:
    # This command reads the lines in the file   
    lines = f.readlines()
    # This command starts a loop over each line in the file
    for i in range(len(lines)):
        # This command this command removed extra spaces from the start of the line and end of the line
        line = lines[i].strip()
        # This command checks of the line is empty then it will skip it
        if not line:
            continue
        # This command will split the lines into parts when there is a comma
        items = line.split(',')
        # This command makes a new list with 4 zeros
        row =[0 for _ in range(4)]
        # This command starts a loop over each part of the line
        for j in range(len(items)):
            # This command checks if thier are more than four parts, then it will stop looking 
            if j >= 4: 
                break
            # This command reokaces the zero at position j with the part form the line
            row[j] = items[j]
        # This command adds the information to the array
        products.append(row)
#--------------------------------------------------------------------------------------------------------------------
#this command defines edge lables
edge_labels = {(n1, n2): d['weight'] for n1, n2, d in Graph.edges(data=True)}

# this commad is going to draw thegraph with label and the edge labels 
nx.draw(Graph, pos, with_labels=True,node_color="skyblue",node_size=400,edge_color="gray")
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels, label_pos=0.5, font_color='red', font_size=9, font_weight='bold')

#this command shows the plot 
plt.show()
