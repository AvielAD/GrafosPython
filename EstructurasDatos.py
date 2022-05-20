class Pila:
    """Operaciones:
    *   Apilar
    *   Desapilar
    *   Verificar pila Vacia
    """
    def __init__(self):
        self.items=[]

    def Apilar(self, value):
        self.items.append(value)

    def Desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    
    def es_vacia(self):
        return self.items == []


class Cola:
    """Operaciones:
    *   Encolar
    *   Desencolar
    *   Verificar cola vacia
    """

    def __init__(self):
        self.items=[]
    
    def Encolar(self, valor):
        self.items.append(valor)

    def Desencolar(self):
        try:
            self.items.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")
    
    def es_vacia(self):
        return self.items == []
