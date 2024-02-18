from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar_inicio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.inicio:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def insertar_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.inicio:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def eliminar_por_carnet(self, carnet):
        actual = self.inicio
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.fin = actual.anterior

                return True
            actual = actual.siguiente
        return False

    def mostrar_lista(self):
        actual = self.inicio
        while actual:
            print(f"{actual.nombre} {actual.apellido} ({actual.carnet}) <-> ", end="")
            actual = actual.siguiente
        print("None")

lista_doble = ListaDoblementeEnlazada()

while True:
    print("\nMenu:")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Eliminar por carnet")
    print("4. Mostrar lista")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        carnet = input("Ingrese carnet: ")
        lista_doble.insertar_inicio(nombre, apellido, carnet)
    elif opcion == "2":
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        carnet = input("Ingrese carnet: ")
        lista_doble.insertar_final(nombre, apellido, carnet)
    elif opcion == "3":
        carnet = input("Ingrese carnet a eliminar: ")
        if not lista_doble.eliminar_por_carnet(carnet):
            print("Carnet no encontrado")
    elif opcion == "4":
        lista_doble.mostrar_lista()
    elif opcion == "5":
        break
    else:
        print("Opcion no valida")

"parte de grafica"
def visualizar_lista(lista):
    dot = Digraph(comment='Lista Doble Enlazada')
    actual = lista.inicio

    while actual:
        dot.node(actual.carnet, f"{actual.nombre} {actual.apellido}\n({actual.carnet})")
        if actual.siguiente:
            dot.edge(actual.carnet, actual.siguiente.carnet, constraint='false')
        if actual.anterior:
            dot.edge(actual.carnet, actual.anterior.carnet, constraint='false', dir='back')
        actual = actual.siguiente

    dot.render('lista_doble', format='png', cleanup=True)

visualizar_lista(lista_doble)