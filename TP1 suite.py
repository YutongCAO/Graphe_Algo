import networkx as nx
from matplotlib import pyplot as plt

print("Ex5:")
# le choix d’un itinéraire est un ’shortest path problem’
print("le choix d’un itinéraire est un ’shortest path problem’")
X = ['B', 'N', 'M', 'L', 'PM', 'PL', 'G']
U = [('B', 'N', 4), ('B', 'M', 9), ('B', 'L', 12), ('N', 'PM', 2), ('N', 'L', 7), ('PM', 'PL', 1), ('PL', 'G', 4.5),
     ('M', 'L', 2.5), ('M', 'G', 4.5), ('L', 'G', 1.25)]
G = nx.DiGraph()
G.add_nodes_from(X)
G.add_weighted_edges_from(U)
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
plt.savefig("itineraire.jpg")
plt.close()
sol = nx.shortest_path(G, 'B', 'G', weight='weight')
print('Le plus court chemin est :', sol)

# la détermination d’une session d’examen la plus courte possible est un ’coloring problem’
print("la détermination d’une session d’examen la plus courte possible est un ’coloring problem’")
X = ['C', 'E', 'I', 'M', 'P']
U = [('C', 'M'), ('C', 'P'), ('E', 'I'), ('I', 'M'), ('I', 'P'), ('M', 'P')]
G = nx.Graph()
G.add_nodes_from(X)
G.add_edges_from(U)
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
plt.savefig("sessionExam.jpg")
plt.close()
sol = nx.greedy_color(G)
print(sol)
print("Nombre de demi-journées : ", max(sol.values()) + 1)

# l’exploitation de gisement pétrolier est un ’minimum spanning tree’
print("l’exploitation de gisement pétrolier est un ’minimum spanning tree’")
X = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']
U = [('A', 'B', 2.8), ('A', 'I', 3.4), ('B', 'D', 2.7), ('B', 'C', 3.1), ('C', 'E', 2.6), ('C', 'F', 3.2),
     ('F', 'G', 2.9), ('I', 'D', 2.1), ('D', 'E', 2.3), ('E', 'H', 2.5), ('I', 'H', 3.9), ('H', 'G', 3.9),
     ('I', 'J', 5.8), ('H', 'J', 6.0)]
G = nx.Graph()
G.add_nodes_from(X)
G.add_weighted_edges_from(U)
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
plt.savefig("minimum_spanning_tree.jpg")
plt.close()
sol = nx.minimum_spanning_tree(G)
print("Arbre couvrant : ", sol.edges)
val = 0
for i in sol.edges:
     val += G[i[0]][i[1]]['weight']
print('Valeur optimale : ', val)

# la composition d’équipes est un ’matching problem’
G = nx.Graph()
U =[(1, 2), (1, 4), (1, 8), (2, 3), (2, 4), (2, 5), (2, 6), (4, 5), (4, 7), (4, 8), (5, 7), (5, 6)]
G.add_edges_from(U)
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
plt.savefig("pilotes.jpg")
plt.close()
sol = nx.maximal_matching(G)
print(G)

