import networkx as nx
from matplotlib import pyplot as plt

print("l’exploitation de gisement pétrolier est un ’minimum spanning tree’")
G = nx.Graph()
U = []
f = open('arbreCouvrantTP2.txt','r')
str_list = f.read().split("\n")
n = int(str_list[0])
m = int(str_list[1])
del(str_list[0:2])
for i in str_list:
    temp = i.split(" ")
    tup = ()
    for j in temp:
        tup = tup + (float(j),)
    U.append(tup)

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