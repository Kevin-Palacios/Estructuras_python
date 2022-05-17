"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
23/04/2022 
q:)->-</: 
"""
class Dato:
    def __init__(self):
        self.altura = None
        self.edad = None
        self.nombre = None

class Nodo:
    def __init__(self):
        self.dato = Dato()
        self.siguiente = None

class Lista:
    def __init__(self, cursor):
        self.cursor = cursor
        self.cabecera = Nodo()
        self.final = Nodo()

