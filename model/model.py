from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._aeroporti = DAO.getAllAeroporti()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for a in self._aeroporti:
            self._idMap[a.id] = a

    def buildGraph(self, distanza_minima):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._aeroporti)
        print(self._grafo)
        allTratte = DAO.getAllTratte(distanza_minima)
        for t in allTratte:
            origine = t.id_origine
            dest = t.id_destinazione
            if (not self._grafo.has_edge(self._idMap[origine], self._idMap[dest])) and (not self._grafo.has_edge(self._idMap[dest], self._idMap[origine])):
                self._grafo.add_edge(self._idMap[origine], self._idMap[dest], weight=t.distanza)
                print(f"Added edge between {origine} and {dest} with distance {t.distanza} km")
        print(self._grafo)


    def getNumNodes(self):
        return len(self._grafo.nodes())

    def getNumEdges(self):
        return len(self._grafo.edges())

    def getAeroportiGrafo(self):
        result = []
        for u,v in self._grafo.edges:
           result.append((u, v, self._grafo[u][v]["weight"]))
        return result