import time

import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


def creeListePre(n, U: list):
    listePre = [[] for i in range(n)]
    for i in U:
        listePre[i[1]].append((i[0], i[2]))
    return listePre


def pcch(n, U: list):
    listeValeurChemin = [0 for i in range(n)]
    listePre = creeListePre(n, U)
    cpt = 0
    for i in listePre:
        sommetProchain = True
        for j in i:
            if (sommetProchain == True):
                listeValeurChemin[cpt] = j[1] + listeValeurChemin[j[0]]
            else:
                if listeValeurChemin[cpt] > j[1] + listeValeurChemin[j[0]]:
                    listeValeurChemin[cpt] = j[1] + listeValeurChemin[j[0]]
            sommetProchain = False
        cpt += 1
    return listeValeurChemin[n - 1]


G = nx.DiGraph()
n = 7
U = [(0, 1, 6), (0, 2, 2), (0, 3, 1), (1, 2, -3), (1, 4, 7), (2, 3, -2), (2, 4, -4), (3, 5, 2), (4, 5, 3), (4, 6, 3),
     (5, 6, 1)]
G.add_weighted_edges_from(U)
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
plt.close()
# sol = nx.shortest_path(G, 0, 6, weight='weight') Algo Dijkstra besoin nombre positif
print(creeListePre(n, U))
tps = time.time()
for i in range(10000):
    pcch(n,U)
print('Temps avec pcch = ', round(time.time() - tps, 2))

tps = time.time()
for i in range(10000):
    sol = nx.bellman_ford_path_length(G, source=0, target=6, weight='weight')
print(sol)
print('Temps avec Bellman_Ford = ', round(time.time() - tps, 2))

tps = time.time()
for i in range(10000):
    sol = nx.johnson(G,weight='weight')
print('Temps avec Johnson = ', round(time.time() - tps, 2))

#tps = time.time()
#for i in range(10000):
#    lenght=nx.floyd_warshall(G, weight='weight')
#print(lenght)
#print('Temps avec Floyd_warshall = ', round(time.time() - tps, 2))


n = 1000
U = []
f = open('bigDAG.txt','r')
str_list = f.read().split("\n")
for i in str_list:
    temp = i.split(" ")
    tup = ()
    for j in temp:
        tup = tup + (int(j),)
    U.append(tup)

G = nx.DiGraph()
G.add_weighted_edges_from(U)
tps = time.time()
#print(creeListePre(n, U))
print(pcch(n,U))
print('Temps avec pcch = ', round(time.time() - tps, 2))

tps = time.time()
sol = nx.bellman_ford_path_length(G, 0, 999, weight='weight')
print(sol)
print('Temps avec Bellman_Ford = ', round(time.time() - tps, 2))

#tps = time.time()
#sol = nx.johnson(G,weight='weight')
#print('Temps avec Johnson = ', round(time.time() - tps, 2))

#tps = time.time()
#lenght=nx.floyd_warshall(G, weight='weight')
#print(lenght)
#print('Temps avec Floyd_warshall = ', round(time.time() - tps, 2))