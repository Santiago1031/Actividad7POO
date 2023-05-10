from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.__elementos = []
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return elemento in self.__elementos

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.__elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.__elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.__elementos:
            if conjunto2.contiene(elemento):
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos = ", ".join([elemento.nombre for elemento in self.__elementos])
        return f"Conjunto {self.nombre}: ({elementos})"


