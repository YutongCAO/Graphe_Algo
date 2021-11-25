import time
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


def creeMatAdj(n, U: list):
    matAdj = [[0 for i in range(n)] for j in range(n)]
    for i in U:
        matAdj[i[0]][i[1]] = 1
    return matAdj


def creeListeSucc(n, U: list):
    listeSucc = [[] for i in range(n)]
    for i in U:
        listeSucc[i[0]].append(i[1])
    return listeSucc


def degreExt(indice, listeSucc):
    return len(listeSucc[indice])


def explore(succ, i, A, pref, suff, p, s):
    pref[i] = p
    p = p + 1
    for j in succ[i]:
        if pref[j] == 0:
            A.append([i, j])
            p, s = explore(succ, j, A, pref, suff, p, s)
    suff[i] = s
    s += 1
    return p, s



def DFS(n, U: list):
    pref = [0 for i in range(n)]  # matrice prefix
    suff = [0 for i in range(n)]  # matrice sufflex
    A = []  # arbre
    p = s = 1  # nombre de pref et suff
    succ = creeListeSucc(n, U)  # matrice de succeseurs
    for i in range(n):  # traverse la matrice
        if pref[i] == 0:
            p, s = explore(succ, i, A, pref, suff, p, s)  # liste est transport par pointeur
    return A, pref, suff

def arcs(n, U: list):
    arcAvant = []
    arcArriere = []
    arcTranverse = []
    A, pref, suff = DFS(n, U)
    for arc in U:
        if arc not in A:
            if pref[arc[0]] < pref[arc[1]]:
                if suff[arc[0]] > suff[arc[1]]:
                    arcAvant.append(arc)
            else:
                if  suff[arc[0]] < suff[arc[1]]:
                    arcArriere.append(arc)
                else:
                    arcTranverse.append(arc)
    return A,arcAvant, arcArriere, arcTranverse



n = 5
U = [[0, 1], [0, 3], [1, 0], [1, 2], [1, 4], [2, 3], [3, 1], [4, 2], [4, 3]]

print("EX1:")
matAdj = creeMatAdj(n, U)
print(matAdj)

listeSucc = creeListeSucc(n, U)
print(listeSucc)

indice = 3
degreE = degreExt(indice, listeSucc)
print(degreE)

A, pref, suff =DFS(n,U)
print(A)
print(pref)
print(suff)



arcArbre, arcAvant, arcArriere, arcTranverse = arcs(n, U)
print("arcArbre : pref(i) < pref(j) suff(i) > suff(j)")
print(arcArbre)
print("arcAvant : pref(i) < pref(j) suff(i) > suff(j)")
print(arcAvant)
print("arcArriere : pref(i) > pref(j) suff(i) < suff(j)")
print(arcArriere)
print("arcTranverse : pref(i) > pref(j) suff(i) > suff(j)")
print(arcTranverse)


def puisk(k, A):
    A = np.array(A)
    Apuisk = A
    for i in range(k-1):
        Apuisk = np.dot(A, Apuisk)
    return Apuisk

def connexiteForte(A):
    Apuisk = np.array(A)
    mat = np.array(A)
    for i in range(len(A)):
        Apuisk = np.dot(np.array(A), Apuisk)
        mat += Apuisk
    for i in mat:
        for j in i:
            if j == 0:
                return False
    return True


print("Ex2:")
matAdj = creeMatAdj(n, U)
Apuisk = puisk(5,matAdj)
print(Apuisk)
if(Apuisk[0][1] > 0):
    print("Il existe un chemin 1 vers 2")
if (connexiteForte(np.array(matAdj))):
    print("Le graphe est fortement connexe\n\n")
else:
    print("Le graphe n'est pas fortement connexe\n")


print("Ex3:")
X = [0, 1, 2, 3, 4]
U = [[0, 1], [0, 3], [1, 0], [1, 2], [1, 4], [2, 3], [3, 1], [4, 2], [4, 3]]
go = nx.DiGraph()
go.add_nodes_from(X)
go.add_edges_from(U)

color = []
for a in go.edges(): #U 最好使用[(0, 1), (0, 3)]格式，因为go.edges()使用这个
    if (list(a) in arcArbre):
        color.append('black')
    elif(list(a) in arcAvant):
        color.append('red')
    elif(list(a) in arcArriere):
        color.append('blue')
    else:
        color.append('green')

nx.draw(go, with_labels=True, edge_color=color)
plt.show()
plt.savefig("graphe.png")


# to_undirected() est une methode qui renvoie le graphe non oriente
if(nx.is_connected(go.to_undirected())):
    print("Le graphe est connexe")

for n in [100, 200, 300, 400]:
    gAlea = nx.gnp_random_graph(n, 0.5, directed=True)
    print("Connexité forte d'un graphe aléatoire de taille", n)
    tps = time.time()
    if(nx.is_strongly_connected(gAlea)):
        print("Le graphe est fortement connexe")
    else:
        print("Le graphe n'est pas fortement connexe")
    print('Temps avec networkx = ', round(time.time() - tps, 2))
    arcAlea = gAlea.edges()
    mat = creeMatAdj(n, arcAlea)
    tps = time.time()
    b = connexiteForte(np.array(mat))
    print('Temps avec produit matriciel = ', round(time.time() - tps, 2))
