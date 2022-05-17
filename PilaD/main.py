"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
#from sympy import true
from audioop import mul
import time

from funciones import *

import sys
sys.path.insert(1, 'PilaD')
from clases import Pila
from clases import Nodo
from clases import Dato

pila = crearPila()


#entrada = int(input("Ingrese cuantos numeros va a ingresar: "))
opcion=0
while(opcion!=7):
    print("Que quieres hacer?")
    print("1-Apilar")
    print("2-Desapilar")
    print("3-consultar cima")
    print("4-Consultar pila")
    print("5-Vaciar pila")
    print("6-Borrar pila")
    print("7-Salir")
    opcion=int(input())
    if(opcion==1):
        datoIngreso=Dato()
        datoIngreso.val=str(input("Ingresa el dato a agregar: "))
        apilar(pila, datoIngreso)
        print("Dato ingresado")
    elif(opcion==2):
        datoExtraido=Dato()
        datoExtraido=desapilar(pila)
    elif(opcion==3):
        consultarCima(pila)
    elif(opcion==4):
        pila = consultarPila(pila)
    elif(opcion==5):
        vaciarPila(pila)
        print("Pila vaciada")
    elif(opcion==6):
        borrarPila(pila)
    elif(opcion==7):
        print("Adios")
    else:
        print("opcion no válida, ingresa una válida")