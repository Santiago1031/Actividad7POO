from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class ListaElementos:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento: Elemento):
        self.elementos.append(elemento)

class ConjuntoElementos:

    contador = 0
    def __init__(self, nombre_conjunto: str):
        self.nombre = nombre_conjunto
        self.elementos = []
        self.__id = type(self).contador
        type(self).contador += 1

    def agregar_elemento(self, elemento: Elemento):
        self.elementos.append(elemento)

    @property
    def id(self):
        return self.__id


