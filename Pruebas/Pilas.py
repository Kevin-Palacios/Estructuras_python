

class datosLegales:
    def __init__(self, casado):
        self.casado = casado

class Humano:
    def __init__(self, edad, cas):
        self.edad = edad
        self.cas = datosLegales(cas)


H1= Humano(28, 29)

print(H1.edad)
print(H1.cas.casado)
