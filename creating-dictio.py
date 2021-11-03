# CREANDO DICCIONARIOS EN PYTHON
# Con los diccionarios podemos almacenar datos en una sola variable.
# Se representan mediante la apertura y cierre con {llaves}
# Y se identifican por almacenarse con el par clave:valor.
# En el podremos almacenar cualquier tipo de dato. STR, INT, FLOAT, BOOLEAN, COMPLEX, LIST.

print('CREANDO UN DICCIONARIO') # Muestro título
product = { # Apertura diccionario
    'art' : 'book', # Creo la clave y asigno su valor
    'code' : 1234, # Creo la clave y asigno su valor
    'price' : 3.5, # Creo la clave y asigno su valor
    'genre' : 'fiction' # Creo la clave y asigno su valor
} # Cierro diccionario
print(product) # Muestro las claves y valores almacenados
input()

# MOSTRANDO EL VALOR DE UNA CLAVE
# Podemos mostrar individualmente los valores almacenados en cada clave almacenada en el diccionario.

print('MOSTRAR VALOR DE LA CLAVE ART') # Muestro título.
print(product['art']) # Muestro el valor de la clave 'art'. En este caso 'book'
input()


# LONGITUD DEL DICCIONARIO
# Mediante el método LENGTH() podemos ver la longitud de nuestro diccionario.
# El resultado será, la cantidad de claves almacenadas.

print('LONGITUD DEL DICCIONARIO') # Muestro título.
print(len(product)) # Muestro la longitud de la var diccionario. En este caso será 4.
input()

