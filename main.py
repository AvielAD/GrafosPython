from EstructurasDatos import Pila

p= Pila()

print(p.es_vacia())

p.Apilar(1)
p.Apilar(2)
p.Apilar(3)
p.Apilar(4)

print(p.items)

print("Remover elemento: ", p.Desapilar())

print(p.items)