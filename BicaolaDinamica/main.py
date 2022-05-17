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
sys.path.insert(1, 'BicolaDinamica')
from clases import cola
from clases import Nodo
from clases import Dato





bicola = crearCola()
print(bicola.cabecera)


#entrada = int(input("Ingrese cuantos numeros va a ingresar: "))
opcion=0

while(opcion!=8):
    print("Que quieres hacer?")
    print("1-Ingresar nodo por la derecha")
    print("2-Ingresar nodo por la izquierda")
    print("3-Mostrar el primer nodo")
    print("4-Mostrar todos los nodos")
    print("5-Contar los nodos")
    print("6-Eliminar el primer nodo")
    print("7-Eliminar toda la bicola")
    print("8-Salir")
    opcion=int(input())
    if(opcion==1):
        datoIngreso=str(input("Ingresa el dato: "))
        encolar(bicola, datoIngreso)
        print("Nodo ingresado por la derecha")
    elif(opcion==2):
        datoIngreso=str(input("Ingresa el dato: "))
        bicola=encolarIzq(bicola, datoIngreso)
        print("Nodo ingresado por la izquierda")
    elif(opcion==3):
        print("Primer nodo: ")
        mostrarPrimerNodo(bicola)
    elif(opcion==4):
        bicola = imprimirCola(bicola)
    elif(opcion==5):
        print("La cola tiene "+str(contarNodos(bicola))+" nodos")
    elif(opcion==6):
        eliminarPrimerNodo(bicola)
    elif(opcion==7):
        borrarCola(bicola)
        print("Bicola borrada")
    elif(opcion==8):
        print("Adios")
    else:
        print("opcion no válida, ingresa una válida")