import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time


def creeMatAdj(n, arcs):
    mat = [[0 for i in range(n)] for j in range(n)]
    for a in arcs:
        mat[a[0]][a[1]] = 1
    return mat


def creeListeSucc(n, arcs):
    succ = [[] for i in range(n)]
    for a in arcs:
        succ[a[0]].append(a[1])
    return succ


def degreExt(s, listeSucc):
    return len(listeSucc[s])


def explore(G, i, pref, suff, A, p, s):
    pref[i] = p
    p += 1
    for j in G[i]:
        if pref[j] == 0:
            A.append((i, j))
            p, s = explore(G, j, pref, suff, A, p, s)
    suff[i] = s
    s += 1
    return p, s


def DFS(n, arcs):
    succ = creeListeSucc(n, arcs)
    p = s = 1
    A = []
    pref = [0 for i in range(n)]
    suff = [0 for i in range(n)]
    for i in range(n):
        if pref[i] == 0:
            p, s = explore(succ, i, pref, suff, A, p, s)
    return A, pref, suff


def puisA(k, A):
    Apuisk = np.array(A)
    for i in range(k):
        Apuisk = np.dot(A, Apuisk)
    return Apuisk


def connexiteForte(A):
    Apuisk = np.array(A)
    R = np.array(A)
    for i in range(len(A)):
        Apuisk = np.dot(A, Apuisk)
        R = np.add(R, Apuisk)
    for i in R:
        for j in i:
            if j == 0:
                return False
    return True


# Exercice 1
print('Exercice 1')
n = 5
arcs = [(0, 1), (0, 3), (1, 0), (1, 2), (1, 4), (2, 3), (3, 1), (4, 2), (4, 3)]
A, pref, suff = DFS(n, arcs)
print('POUR SIMPLIFIER LES SOMMETS SONT NUMEROTES DE 0 A 4 !')
print('Ensemble des arcs d\'arbre:')
for a in A:
    print('(', a[0], ',', a[1], ')', sep='', end=' ')
print()
print(pref)
print(suff)
arcsAvant = []
arcsArriere = []
arcsCroise = []
for a in arcs:
    if not (a in A):
        if pref[a[0]] < pref[a[1]]:
            arcsAvant.append(a)
        else:
            if suff[a[0]] < suff[a[1]]:
                arcsArriere.append(a)
            else:
                arcsCroise.append(a)
print('Arcs avant :', arcsAvant)
print('Arc arrière :', arcsArriere)
print('Arcs croisés :', arcsCroise)
print('\n')

# Exercice 2
print('Exercice 2')
mat = creeMatAdj(n, arcs)
Apuisk = puisA(4, np.array(mat))
print(Apuisk)
if Apuisk[0][1] > 0: print('oui il existe un chemin allant de 1 à 2')
if (connexiteForte(np.array(mat))):
    print("Le graphe est fortement connexe\n\n")
else:
    print("Le graphe n'est pas fortement connexe\n")

# Exercice 3
print('Exercice 3')
go = nx.DiGraph()
go.add_edges_from(arcs)

color = []
for a in go.edges():
    if (a in A):
        color.append('r')
    else:
        color.append('b')

nx.draw(go, with_labels=True, edge_color=color)
plt.show()
plt.savefig("graphe.png")

# to_undirected() est une methode qui renvoie le graphe non oriente

if (nx.is_connected(go.to_undirected())):
    print("Le graphe est connexe")

for n in [100, 200, 300, 400]:
    gAlea = nx.gnp_random_graph(n, 0.5, directed=True)
    print("Connexité forte d'un graphe aléatoire de taille", n)
    tps = time.time()
    if (nx.is_strongly_connected(gAlea)):
        print("Le graphe est fortement connexe")
    else:
        print("Le graphe n'est pas fortement connexe")
    print('Temps avec networkx = ', round(time.time() - tps, 2))
    arcAlea = gAlea.edges()
    mat = creeMatAdj(n, arcAlea)
    tps = time.time()
    b = connexiteForte(np.array(mat))
    print('Temps avec produit matriciel = ', round(time.time() - tps, 2))

print("Exercice 5:")
# Le choix d’un itinéraire
G = nx.DiGraph()
G.add_nodes_from(['N', 'PM', 'PL', 'G', 'M', 'L', 'B'])
G.add_weighted_edges_from(
    [('B', 'N', 4), ('B', 'M', 9), ('B', 'L', 12), ('N', 'PM', 2), ('N', 'L', 7), ('M', 'L', 2.5), ('M', 'G', 4.5),
     ('PM', 'PL', 1), ('PL', 'G', 4.5), ('L', 'G', 1.25)])
nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
plt.savefig("itineraire.jpg")
plt.close()
sol = nx.shortest_path(G, source='B', target='G', weight='weight')
print('Le plus court chemin est :', sol)

# La détermination d’une session d’examen la plus courte possible
G = nx.Graph()
G.add_nodes_from(['C', 'Elec', 'Info', 'Math', 'Phy'])
G.add_edges_from([('C', 'Math'), ('C', 'Phy'), ('Elec', 'Info'), ('Info', 'Math'), ('Info', 'Phy'), ('Math', 'Phy')])
nx.draw(G, with_labels=True)
plt.show()
plt.savefig("sessionExam.jpg")
plt.close()
sol = nx.greedy_color(G)
print("Nombre de demi-journées : ", max(sol.values()) + 1)

# l'exploitation de gisement pétrolier
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
G.add_weighted_edges_from(
    [('A', 'B', 2.8), ('A', 'I', 3.4), ('B', 'C', 3.1), ('B', 'D', 2.7), ('C', 'D', 2.4), ('C', 'E', 2.6),
     ('C', 'F', 3.2), ('D', 'E', 2.3), ('D', 'I', 2.1), ('E', 'F', 3.4), ('E', 'H', 2.5), ('F', 'G', 2.9),
     ('G', 'H', 3.6), ('H', 'I', 3.9), ('H', 'J', 6.0), ('I', 'J', 5.8)])
nx.draw(G, with_labels=True)
plt.show()
plt.savefig("canalisation.jpg")
plt.close()
sol = nx.minimum_spanning_tree(G)
print("Arbre couvrant : ", sol.edges)
val = 0
for e in sol.edges:
    val += G[e[0]][e[1]]['weight']
print('Valeur optimale : ', val)

# La composition d’équipes
G = nx.Graph()
G.add_nodes_from(range(1, 9))
G.add_edges_from([(1, 2), (1, 4), (1, 8), (2, 3), (2, 4), (2, 5), (2, 6), (4, 5), (4, 7), (4, 8), (5, 6), (5, 7)])
nx.draw(G, with_labels=True)
plt.show()
plt.savefig("pilotes.jpg")
# plt.close()
sol = nx.maximal_matching(G)
print(sol)
