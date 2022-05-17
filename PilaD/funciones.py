"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
import sys
from tkinter.messagebox import NO

sys.path.insert(1, 'PilaD')
from clases import Pila
from clases import Nodo
from clases import Dato

def crearPila():
	pila = Pila(0)
	pila.cabecera=None
	return pila


def apilar(p, dato):
	nodousuario= Nodo()
	nodousuario.dato.val=dato.val
	nodousuario.anterior=p.cabecera
	p.cabecera=nodousuario
	p.cursor=p.cursor+1
	#return 0

def desapilar(p):
    aux= Nodo()
    if(isEmpty(p) == False):
        
        aux=p.cabecera
        p.cabecera=aux.anterior
        aux.anterior=None
        p.cursor=p.cursor-1
        datoExtraido=aux.dato
        del aux
        return datoExtraido
    else:
        print("La pila no tiene datos")
	
	
	

def consultarCima(p):
	if(isEmpty(p)==False):
		print("El valor en la cima es: "+ p.cabecera.dato.val)
	else:
		print("La cima no contiene datos")

def consultarPila(pila):
    valorExtraido=Dato()
    pilaAux = crearPila()
    while(isEmpty(pila)==False):
        valorExtraido = desapilar(pila)
        apilar(pilaAux, valorExtraido)
        print("Valor extraido: "+ valorExtraido.val)
    while(isEmpty(pilaAux)==False):
        valorExtraido = desapilar(pilaAux)
        apilar(pila, valorExtraido)
    return pila

def vaciarPila(p):
	valorExtraido=Dato()
	print("Vaciando pila...")
	while(isEmpty(p)==False):
		valorExtraido = desapilar(p)
		print("Valor extraido: "+ valorExtraido.val)

def borrarPila(pila):
    while(isEmpty(pila)==False):
        desapilar(pila)
    del pila

def isEmpty(p):
	if(p.cabecera==None):
		return True
	else:
		return False
	
	