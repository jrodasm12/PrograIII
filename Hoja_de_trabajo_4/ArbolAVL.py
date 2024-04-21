import csv
import os

class NodoArbol:
    def __init__(self, clave, datos):
        self.clave = clave
        self.datos = datos
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, datos):
        if not self.raiz:
            self.raiz = NodoArbol(clave, datos)
        else:
            self.raiz = self._insertar(self.raiz, clave, datos)

    def _insertar(self, nodo, clave, datos):
        if not nodo:
            return NodoArbol(clave, datos)
        elif clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, datos)
        else:
            nodo.derecha = self._insertar(nodo.derecha, clave, datos)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

        balance = self._balance(nodo)

        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotar_derecha(nodo)
        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _balance(self, nodo):
        if not nodo:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))

        return y

    def _rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))

        return y

class Registro:
    def __init__(self, id):
        self.id = id

arbol_registros = ArbolAVL()

def cargar_registros_desde_csv(ruta_archivo):
    if os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
        with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
            lector = csv.reader(csvfile)
            for fila in lector:
                if fila:  # Verificar si la fila contiene datos
                    id = fila[0]  # Suponiendo que el ID está en la primera columna
                    arbol_registros.insertar(id, Registro(id))
        return True
    else:
        return False

def encontrar_registro_por_id(id, nodo_actual):
    if not nodo_actual:
        return None

    if id == nodo_actual.datos.id:
        return nodo_actual.datos
    elif id < nodo_actual.datos.id:
        return encontrar_registro_por_id(id, nodo_actual.izquierda)
    else:
        return encontrar_registro_por_id(id, nodo_actual.derecha)
