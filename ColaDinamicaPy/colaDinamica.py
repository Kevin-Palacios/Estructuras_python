from sympy import true

from FuncionesColaDinamica import *

import sys
sys.path.insert(1, 'Practica7Bicola')
from clases import cola
from clases import Nodo
from clases import Dato





c = crearCola()
print(c.cabecera)


entrada = int(input("Ingrese cuantos numeros va a ingresar: "))

for i in range(0,entrada):
    # El range es 0 ya que las listas empiezan en 0
    
    datoIngreso = int(input(f"Ingrese el numero {i+1}: "))
    encolar(c, datoIngreso)
    #print(c.cursor)
    #print(c.cabecera.dato)
    #print(c.final.dato)

imprimirCola(c)