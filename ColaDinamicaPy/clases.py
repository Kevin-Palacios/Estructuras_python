class Dato:
    def __init__(self):
        self.valor = None

class Nodo:
    def __init__(self):
        self.dato = Dato()
        self.siguiente = None

class cola:
    def __init__(self, cursor):
        self.cursor = cursor
        self.cabecera = Nodo()
        self.final = Nodo()

