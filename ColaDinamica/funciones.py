"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
import sys
sys.path.insert(1, 'ColaDinamica')
from clases import cola
from clases import Nodo
from clases import Dato

def crearCola():
    c=cola(0)
    c.cabecera=None
    c.final=None
    return c

def encolar(cola, datoIngreso):
    nodousuario=Nodo()
    if(estaVacia(cola)):
        
        nodousuario.dato=datoIngreso
        cola.cabecera=nodousuario
        cola.final=nodousuario
    else:
        nodousuario.dato=datoIngreso
        cola.final.siguiente=nodousuario
        cola.final=nodousuario
    
    cola.cursor=cola.cursor+1


def estaVacia(cola):
    if(cola.cabecera==None and cola.final==None and cola.cursor==0):
        return True
    else:
        return False

def desencolar(colaAuxiliar, datoExtraido):
    nodoAuxiliar = Nodo()
    if(estaVacia(colaAuxiliar)):
        #print("la cola está vacía")
        return None
    elif(colaAuxiliar.cursor>1):
        nodoAuxiliar=colaAuxiliar.cabecera
        colaAuxiliar.cabecera=colaAuxiliar.cabecera.siguiente
    elif(colaAuxiliar.cursor==1):
        nodoAuxiliar=colaAuxiliar.cabecera
        colaAuxiliar.cabecera=None
        colaAuxiliar.final=None
    
    colaAuxiliar.cursor=colaAuxiliar.cursor-1
    datoExtraido=nodoAuxiliar.dato
    del nodoAuxiliar
    return datoExtraido
    
def borrarCola(c):
    if(estaVacia(c)==False):
        nodoAuxiliar = Nodo()
        nodoAuxiliarRespaldo = Nodo()
        nodoAuxiliar=c.cabecera
        while(nodoAuxiliar!=None):
            nodoAuxiliarRespaldo=nodoAuxiliar.siguiente
            del nodoAuxiliar
            nodoAuxiliar=nodoAuxiliarRespaldo
        c.cabecera=None
        c.final=None
        c.cursor=0
        del c

def imprimirCola(cola):
    datoExtraido=Dato()
    colaAux=crearCola()
    
    if(estaVacia(cola)==False):
        while(estaVacia(cola)==False):
            datoExtraido = desencolar(cola, datoExtraido)
            encolar(colaAux, datoExtraido)
            print("Dato extraido: ")
            print(datoExtraido)
        
        #print(cola.cursor)
        return colaAux
    else:
        print("La cola está vacía")
        return cola

def mostrarPrimerNodo(cola):
    print(cola.cabecera.dato)

def contarNodos(cola):
    return cola.cursor

def eliminarPrimerNodo(c):
    datoExtraido = Dato()
    if(estaVacia(c)==False):
        print("Dato borrado: ")
        print(desencolar(c, datoExtraido))

