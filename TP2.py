import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

go = nx.DiGraph()
U = [(0, 1, 6), (0, 2, 2), (0, 3, 1), (1, 2, -3), (1, 4, 7), (2, 3, -2), (2, 4, -4), (3, 5, 2), (4, 5, 3), (4, 6, 3),
     (5, 6, 1)]
for a,b,w in U:
    go.add_edge(a, b, weights = w)
nx.draw(go, with_labels=True,node_color='lightgrey',node_size=600,font_weight='bold')
plt.show()
