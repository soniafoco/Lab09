import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        distanza_minima = int(self._view._txtIn.value)
        self._model.buildGraph(distanza_minima)

        numNodes = self._model.getNumNodes()
        numEdges = self._model.getNumEdges()
        aeroporti = self._model.getAeroportiGrafo()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo pesato correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {numNodes} nodi e {numEdges} archi"))
        for a in aeroporti:
            self._view._txt_result.controls.append(ft.Text(f"{a[0]} --> {a[1]} -- Avg Distance: {a[2]}"))
        self._view.update_page()

