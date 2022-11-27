# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def desafio():
    print('Ejercicio de archivos')
    
    with open ("stock.csv") as csvfile:
        data = list(csv.DictReader(csvfile))
         
    
    cantidad_tornillos = 0
    for i in data:
        cantidad_tornillos += int(i['tornillos'])
    print(f'Cantidad de tornillo: {cantidad_tornillos}')
             

  
            

    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Al final de esta función retornar (return) el stock total de tornillos
    # Comenzar aquí, recuerde el identado dentro de esta funcion
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
