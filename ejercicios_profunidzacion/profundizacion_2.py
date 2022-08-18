# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.2

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random

'''
Enunciado:
Alumno: Crear la función "contar"

Utilice la función "lista_aleatoria" creada antes 
para generar una lista de 5 números en
un rango de 1 a 6 inclusive

lista_numeros = lista_aleatoria(inicio, fin, cantidad)

Generar una una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista (también pasada por parámetro)

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior
def lista_aleatoria(inicio, fin, cantidad):
    cantidad_numero_repetido = 0
    cantidad_3 = 0
    lista = []
    for n in range(1, cantidad+1):
        numero = random.randint(inicio, fin)
        lista.append(numero)
        if numero_repetido == numero:
            cantidad_numero_repetido +=1
        if 3 == numero:
            cantidad_3 +=1
    return lista

# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar
def contar(lista_numeros, numero_repetido):
    cantidad_numero_repetido = 0
    for n in range(0, cantidad):
        if lista_numeros[n] == numero_repetido:
            cantidad_numero_repetido +=1
    return cantidad_numero_repetido

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive
    inicio = 1
    fin = 6
    cantidad = 5
    # lista_numeros = lista_aleatoria(...)
    print('¿que número del 1 al 6 queres saber cuantas veces se repite?')
    numero_repetido = int(input())
    lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    cantidad_repetido = contar(lista_numeros, numero_repetido)
    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":
    
    print('la lista aleatoria formada es:',lista_numeros)
    print('el número {} está {} veces'.format(numero_repetido, cantidad_repetido))
    # print(lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    # cantidad_tres = contar(lista_numeros, 3)

    # print(cantidad_tres)
    print('el número 3 está', contar(lista_numeros, 3), 'veces')

    print("terminamos")
