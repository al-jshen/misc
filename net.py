import networkx as nx
from matplotlib import pyplot as plt
import random

G=nx.Graph()
for i in range(50):
    G.add_edge(random.randint(1, 20),random.randint(1, 20),weight=random.randint(1, 10))

pos = nx.circular_layout(G)

#weights = [j.get('weight') for j in [i[2] for i in list(map(list, G.edges(data=True)))]]
labels = nx.get_edge_attributes(G,'weight')

nx.draw(G,with_labels=True,pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print(nx.shortest_path(G, random.randint(1, 20), random.randint(1, 20)))
plt.show()
