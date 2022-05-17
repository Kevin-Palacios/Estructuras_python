"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
#from sympy import true
import time

from funciones import *

import sys
sys.path.insert(1, 'ColaDinamica')
from clases import cola
from clases import Nodo
from clases import Dato



cola = crearCola()

opcion=0

while(opcion!=7):
    print("Que quieres hacer?")
    print("1-Ingresar nodo por la derecha")
    print("2-Mostrar el primer nodo")
    print("3-Mostrar todos los nodos")
    print("4-Contar los nodos")
    print("5-Eliminar el primer nodo")
    print("6-Eliminar toda la cola")
    print("7-Salir")
    opcion=int(input())
    if(opcion==1):
        datoIngreso=str(input("Ingresa el dato: "))
        encolar(cola, datoIngreso)
        print("Nodo ingresado por la derecha")
    elif(opcion==2):
        print("Primer nodo: ")
        mostrarPrimerNodo(cola)
    elif(opcion==3):
        cola = imprimirCola(cola)
    elif(opcion==4):
        print("La cola tiene "+str(contarNodos(cola))+" nodos")
    elif(opcion==5):
        eliminarPrimerNodo(cola)
    elif(opcion==6):
        borrarCola(cola)
        print("cola borrada")
    elif(opcion==7):
        print("Adios")
    else:
        print("opcion no válida, ingresa una válida")