import graphviz

class nodos:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        self.raiz = self._agregar(self.raiz, valor)

    def _agregar(self, nodo, valor):
        if nodo == None:
            return nodos(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._agregar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._agregar(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo == None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo == None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda == None:
                return nodo.derecha
            elif nodo.derecha == None:
                return nodo.izquierda
            nodo.valor = self._minimo_valor(nodo.derecha)
            nodo.derecha = self._eliminar(nodo.derecha, nodo.valor)
        return nodo

    def _minimo_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def graficar(self):
        grafico = graphviz.Digraph(comment='Arbol Binario de Busqueda')
        self._graficar(self.raiz, grafico)
        grafico.render('grafica_arbol', format='png', cleanup=True)

    def _graficar(self, nodo, grafico):
        if nodo:
            grafico.node(str(nodo.valor))
            if nodo.izquierda:
                grafico.edge(str(nodo.valor), str(nodo.izquierda.valor))
                self._graficar(nodo.izquierda, grafico)
            if nodo.derecha:
                grafico.edge(str(nodo.valor), str(nodo.derecha.valor))
                self._graficar(nodo.derecha, grafico)

def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\nMenu Interactivo:")
        print("1. Agregar numero")
        print("2. Buscar numero")
        print("3. Eliminar numero")
        print("4. Graficar arbol")
        print("5. Salir")

        opcion = input("Ingrese el numero de la opcion: ")

        if opcion == '1':
            numero = int(input("Ingrese un numero para agregar en el arbol: "))
            arbol.agregar(numero)
            print(f"Numero {numero} agregado correctamente")
        elif opcion == '2':
            numero = int(input("Ingrese un numero para buscar: "))
            resultado = arbol.buscar(numero)
            if resultado:
                print(f"Numero {numero} encontrado en el arbol")
            else:
                print(f"Numero {numero} no encontrado en el arbol")
        elif opcion == '3':
            numero = int(input("Ingrese un numero para eliminar: "))
            arbol.eliminar(numero)
            print(f"Numero {numero} eliminado correctamente")
        elif opcion == '4':
            arbol.graficar()
            print("Arbol graficado correctamente")
        elif opcion == '5':
            break
        else:
            print("Opcion no valida ingrese un numero del 1 al 5")

if __name__ == "__main__":
    menu()