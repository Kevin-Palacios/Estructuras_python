"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
15/05/2022 
q:)->-</: 
"""
class Dato:
    def __init__(self):
        self.val = None

class Nodo:
    def __init__(self):
        self.dato = Dato()
        self.anterior = None

class Pila:
    def __init__(self, cursor):
        self.cursor = cursor
        self.cabecera = Nodo()