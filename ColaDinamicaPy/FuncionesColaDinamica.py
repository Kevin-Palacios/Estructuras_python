import sys
sys.path.insert(1, 'Practica7Bicola')
from clases import cola
from clases import Nodo
from clases import Dato

def crearCola():
    c=cola(0)
    c.cabecera=None
    c.final=None
    return c

def encolar(c, datoIngreso):
    nodousuario=Nodo()
    if(estaVacia(c)):
        
        nodousuario.dato=datoIngreso
        c.cabecera=nodousuario
        c.final=nodousuario
    else:
        nodousuario.dato=datoIngreso
        c.final.siguiente=nodousuario
        c.final=nodousuario
    
    c.cursor=c.cursor+1



def estaVacia(c):
    if(c.cabecera==None and c.final==None and c.cursor==0):
        return True
    else:
        return False

def desencolar(c, datoExtraido):
    nodoAuxiliar = Nodo()
    if(estaVacia(c)):
        print("la cola está vacía")
    elif(c.cursor>1):
        nodoAuxiliar=c.cabecera
        c.cabecera=c.cabecera.siguiente
    elif(c.cursor==1):
        nodoAuxiliar=c.cabecera
        c.cabecera=None
        c.final=None
    
    c.cursor=c.cursor-1
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

def imprimirCola(c):
    datoExtraido=Dato()
    if(estaVacia(c)==False):
        while(estaVacia(c)==False):
            datoExtraido = desencolar(c, datoExtraido)
            print("Dato extraido: ")
            print(datoExtraido)