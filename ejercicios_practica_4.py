# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

# Objetivo:
# Leer y trabajar con un archivo CSV complejo y el
# manejo de excepciones

# Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de departamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion

def desafio(ambientes):
    print('Ejercicios con archivos CSV complejos')
    with open ('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))


    dos_ambientes = 0
    tres_ambientes = 0
 
    for i in data:    
        try:
            ambiente = int(i['ambientes'])
            if ambiente == 2:
               dos_ambientes += 1 

            elif ambiente == 3:
                tres_ambientes += 1         
                         
        except:
            continue   


    if ambientes == 2:  #382
        return dos_ambientes

    elif ambientes == 3:  #239 
        return tres_ambientes 
        
    else:
        print("Solo departamentos de 2 y 3 ambientes disponibles por el momento, muchas gracias vuelva prontos.")
        exit()
          
        


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    try:
        ambientes = int(input(f'Ingrese la cantidad de ambientes: '))
        print(f'La cantidad de departamentos de {ambientes} ambientes es de {desafio(ambientes)}.')
    except ValueError:
        print(f'Por favor ingresar un numero entero') 
