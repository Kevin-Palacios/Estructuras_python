"""
Palacios Elizondo Kevin Antonio
2BM1
Inteligencia Artificial
24/04/2022 
q:)->-</: 
"""
import sys
from tkinter.messagebox import NO

sys.path.insert(1, 'Examen_muestra')
from clasesLista import Lista
from clasesLista import Nodo
from clasesLista import Dato


def crearLista():
    l=Lista(0)
    l.cabecera=None
    return l

def agregarDerecha(l, datoIngreso):
    nodousuario=Nodo()
    nodousuario.dato=datoIngreso
    if(estaVaciaL(l)):
        l.cabecera=nodousuario
        l.cabecera.siguiente=None
        l.cabecera.pos=0
    else:
        nodoAux= Nodo()
        nodoAux = l.cabecera
        while(nodoAux.siguiente!=None):
            nodoAux=nodoAux.siguiente
        
        posAux = nodoAux.pos
        nodousuario.siguiente=None
        nodousuario.pos=posAux+1
        nodoAux.siguiente=nodousuario
    l.cursor=l.cursor+1

def agregarIzq(l, datoIngreso):
    listaAux = crearLista()

    nodousuario=Nodo()
    
    if(estaVaciaL(l)):
        agregarDerecha(l, datoIngreso)
        return l
    else:
        nodousuario.dato=datoIngreso
        agregarDerecha(listaAux, datoIngreso)
        while(l.cursor!=0):
            nodousuario.dato=extraerI(l)
            agregarDerecha(listaAux, nodousuario.dato)
        
        l=listaAux
        return listaAux

def agregarN(l, datoIngreso, n):
    listaAux = crearLista()
    
    nodousuario=Nodo()
    nodoAux=Nodo()
    if(estaVaciaL(l)):
        agregarDerecha(l, datoIngreso)
        return l
    else:
        i=0
        for i in range(n):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)
            print("se hace "+str(i)+"veces")
        
        nodousuario.dato=datoIngreso
        agregarDerecha(listaAux, datoIngreso)

        print("Fin del 1er while: ")
        l=recorrerLista(l)
        print("Fin lista original")
        listaAux= recorrerLista(listaAux)
        print("Fin lista nueva")
        while(l.cursor!=0):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)

    return listaAux


def extraerI(listaAux):
    nodoAuxiliar = Nodo()
    if(estaVaciaL(listaAux)):
        print("la lista está vacía")
        return None
    elif(listaAux.cursor>1):
        nodoAuxiliar=listaAux.cabecera
        listaAux.cabecera=listaAux.cabecera.siguiente
    elif(listaAux.cursor==1):
        nodoAuxiliar=listaAux.cabecera
        listaAux.cabecera=None
    
    listaAux.cursor=listaAux.cursor-1
    datoExtraido=nodoAuxiliar.dato
    del nodoAuxiliar
    return datoExtraido

def extraerD(l):
    listaAux=crearLista()
    
    
    if(estaVaciaL(l)):
        print("la lista está vacía")
        return None
    else:
        nodoAux=Nodo()
        i=0
        n=l.cursor
        for i in range(n):
            
            print("Veces: "+str(i))
            if(n-1!=i):
                nodoAux.dato=extraerI(l)
                agregarDerecha(listaAux, nodoAux.dato)
            else:
                nodoAux.dato=extraerI(l)
        datoExtraido=nodoAux.dato
        recorrerLista(listaAux)
        while(listaAux.cursor!=0):
            nodoAux.dato=extraerI(listaAux)
            agregarDerecha(l, nodoAux.dato)
            
    del nodoAux
    return datoExtraido



def extraerN(l, n):
    listaAux = crearLista()
    
    nodousuario=Nodo()
    nodoAux=Nodo()
    if(estaVaciaL(l)):
        print("la lista está vacía")
        return None
    else:
        i=0
        for i in range(n):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)
            print("se hace "+str(i)+"veces")
        
        nodoAux.dato= extraerI(l)
        datoExtraido=nodoAux.dato


        
        while(l.cursor!=0):
            nodoAux.dato= extraerI(l)
            agregarDerecha(listaAux, nodoAux.dato)

        while(listaAux.cursor!=0):
            nodoAux.dato=extraerI(listaAux)
            agregarDerecha(l, nodoAux.dato)

    del nodoAux
    return datoExtraido

def recorrerLista(l):
    if(estaVaciaL(l)):
        print("Sin clientes")
        return l
    listaAux=crearLista()
    nodoAux = Nodo()
    nodoAux=l.cabecera
    cont=1
    while(nodoAux!=None):
        print("Nombre del cliente "+str(cont)+": "+str(nodoAux.dato.nombre))
        print("Edad del cliente "+str(cont)+": "+str(nodoAux.dato.edad))
        agregarDerecha(listaAux, nodoAux.dato)
        nodoAux=nodoAux.siguiente
        cont=cont+1
    return listaAux

def estaVaciaL(l):
    if(l.cabecera==None and l.cursor==0):
        return True
    else:
        return False

def contarNodos(l):
    return l.cursor

def borrarLista(l):
    if(estaVaciaL(l)==False):
        nodoAuxiliar = Nodo()
        nodoAuxiliarRespaldo = Nodo()
        nodoAuxiliar=l.cabecera
        while(nodoAuxiliar!=None):
            nodoAuxiliarRespaldo=nodoAuxiliar.siguiente
            del nodoAuxiliar
            nodoAuxiliar=nodoAuxiliarRespaldo
        l.cabecera=None
        l.cursor=None
        del l