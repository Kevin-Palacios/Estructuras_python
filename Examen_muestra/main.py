
from ast import While
from funcionesC import *
from funcionesL import *
import random

import sys
sys.path.insert(1, 'Examen_muestra')
from clasesCola import cola
from clasesCola import Nodo
from clasesCola import Dato





c = crearCola()


entrada = int(input("Ingrese cuantos clientes va a ingresar: "))

for i in range(0,entrada):
    # El range es 0 ya que las listas empiezan en 0
    datoIngreso=Dato()
    datoIngreso.altura = float(input(f"Ingrese la altura del cliente {i+1}: "))
    datoIngreso.nombre = str(input(f"Ingrese el nombre del cliente {i+1}: "))
    datoIngreso.edad = random.randint(18, 60)
    encolar(c, datoIngreso)
    #print(c.cursor)
    #print(c.cabecera.dato)
    #print(c.final.dato)

c=imprimirCola(c)

robot1=crearLista()
robot2=crearLista()
robot3=crearLista()
robot4=crearLista()
robot5=crearLista()

while(estaVacia(c)==False):
    datoExtraido=Dato()
    datoExtraido=desencolar(c, datoExtraido)
    if(datoExtraido.edad>18 and datoExtraido.edad<22):
        agregarDerecha(robot1, datoExtraido)
    elif(datoExtraido.edad==18):
        agregarDerecha(robot2, datoExtraido)
    elif(datoExtraido.edad>22 and datoExtraido.edad<44):
        agregarDerecha(robot3, datoExtraido)
    elif(datoExtraido.edad==22 or datoExtraido.edad==44):
        agregarDerecha(robot4, datoExtraido)
    elif(datoExtraido.edad>44 and datoExtraido.edad<60):
        agregarDerecha(robot5, datoExtraido)
print("***********Atención en ventanillas****************")
cont=1
while(estaVaciaL(robot1)==False or estaVaciaL(robot2)==False or estaVaciaL(robot3)==False or estaVaciaL(robot4)==False or estaVaciaL(robot5)==False):
    
    print("Turno "+str(cont)+", robot 1")
    if(estaVaciaL(robot1)==False):
        datoExtraido=Dato()
        print("Personas en ventanilla: ")
        print("cliente 1")
        datoExtraido=extraerI(robot1)
        print("Nombre: "+str(datoExtraido.nombre))
        print("Edad: "+str(datoExtraido.edad))
        if(estaVaciaL(robot1)==False):
            datoExtraido=extraerI(robot1)
            print("cliente 2")
            print("Nombre: "+str(datoExtraido.nombre))
            print("Edad: "+str(datoExtraido.edad))
        else:
            print("Solo hay una persona en ventanilla ya que no hay mas clientes")
        print("En espera: ")
        robot1=recorrerLista(robot1)
    else:
        print("Lista del robot vacía (sin clientes)")
    
    print("Turno "+str(cont)+", robot 2")
    if(estaVaciaL(robot2)==False):
        datoExtraido=Dato()
        print("Personas en ventanilla: ")
        print("cliente 1")
        datoExtraido=extraerI(robot2)
        print("Nombre: "+str(datoExtraido.nombre))
        print("Edad: "+str(datoExtraido.edad))
        if(estaVaciaL(robot2)==False):
            datoExtraido=extraerI(robot2)
            print("cliente 2")
            print("Nombre: "+str(datoExtraido.nombre))
            print("Edad: "+str(datoExtraido.edad))
        else:
            print("Solo hay una persona en ventanilla ya que no hay mas clientes")
        print("En espera: ")
        robot2=recorrerLista(robot2)
    else:
        print("Lista del robot vacía (sin clientes)")

    print("Turno "+str(cont)+", robot 3")
    if(estaVaciaL(robot3)==False):
        datoExtraido=Dato()
        print("Personas en ventanilla: ")
        print("cliente 1")
        datoExtraido=extraerI(robot3)
        print("Nombre: "+str(datoExtraido.nombre))
        print("Edad: "+str(datoExtraido.edad))
        if(estaVaciaL(robot3)==False):
            datoExtraido=extraerI(robot3)
            print("cliente 2")
            print("Nombre: "+str(datoExtraido.nombre))
            print("Edad: "+str(datoExtraido.edad))
        else:
            print("Solo hay una persona en ventanilla ya que no hay mas clientes")
        print("En espera: ")
        robot3=recorrerLista(robot3)
    else:
        print("Lista del robot vacía (sin clientes)")

    print("Turno "+str(cont)+", robot 4")
    if(estaVaciaL(robot4)==False):
        datoExtraido=Dato()
        print("Personas en ventanilla: ")
        print("cliente 1")
        datoExtraido=extraerI(robot4)
        print("Nombre: "+str(datoExtraido.nombre))
        print("Edad: "+str(datoExtraido.edad))
        if(estaVaciaL(robot4)==False):
            datoExtraido=extraerI(robot4)
            print("cliente 2")
            print("Nombre: "+str(datoExtraido.nombre))
            print("Edad: "+str(datoExtraido.edad))
        else:
            print("Solo hay una persona en ventanilla ya que no hay mas clientes")
        print("En espera: ")
        robot4=recorrerLista(robot4)
    else:
        print("Lista del robot vacía (sin clientes)")

    print("Turno "+str(cont)+", robot 5")
    if(estaVaciaL(robot5)==False):
        datoExtraido=Dato()
        print("Personas en ventanilla: ")
        print("cliente 1")
        datoExtraido=extraerI(robot5)
        print("Nombre: "+str(datoExtraido.nombre))
        print("Edad: "+str(datoExtraido.edad))
        if(estaVaciaL(robot5)==False):
            datoExtraido=extraerI(robot5)
            print("cliente 2")
            print("Nombre: "+str(datoExtraido.nombre))
            print("Edad: "+str(datoExtraido.edad))
        else:
            print("Solo hay una persona en ventanilla ya que no hay mas clientes")
        print("En espera: ")
        robot5=recorrerLista(robot5)
    else:
        print("Lista del robot vacía (sin clientes)")
    cont=cont+1

"""
print("robot 1: ")
robot1=recorrerLista(robot1)
print("robot 2: ")
robot2=recorrerLista(robot2)
print("robot 3: ")
robot3=recorrerLista(robot3)
print("robot 4: ")
robot4=recorrerLista(robot4)
print("robot 5: ")
robot5=recorrerLista(robot5)
"""