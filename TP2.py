import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

X = [0, 1, 2, 3, 4, 5, 6]
start = [0,0]
to = [1,2]
value = [6,2]

go = nx.DiGraph()
go.add_nodes_from(X)
for j in range(len(start)):
     go.add_edges_from([(start[j], to[j], value[j])])
nx.draw(go, with_labels=True)
plt.show()
