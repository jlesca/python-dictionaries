# ACCEDIENDO A LOS ITEMS DE NUESTRO DICCIONARIO
# Podemos acceder a cada elemento almacenado en nuestro diccionario.
# Debemos hacerlo especificando la clave. 
# Por ejemplo para una librería crearemos el diccionario 'product'

print('ACCEDER A UN ITEM DE NUESTRO DICCIONARIO') # Muestro título.
product = { # Abro diccionario.
    'art' : 'book', # Creo clave y valor.
    'code' : 1234, # Creo clave y valor.
    'price' : 2.5, # Creo clave y valor.
    'genre' : 'fiction' # Creo clave y valor.
} # Cierro diccionario.

x = product['art'] # Creo var y le asigno el valor de la clave 'art' de nuestro diccionario.
print(x) # Muestro var.
input() # Salgo con enter.


# Recordando que los diccionario se almacenan con el par clave:valor, podemos mostrar cada uno de ellos.
# Para mostrar las claves almacenadas, debemos usar el método KEYS().

print('MOSTRAR LAS CLAVES ALMACENADAS') # Muestro título.
x = product.keys() # Creo una var con el valor de las claves de nuestro diccionario. 
print(x) # Muestro var. En este caso será ' art' 'code' 'price' ' genre'
input() # Salgo con enter.

# Lo mismo podemos hacer para visualizar los valores almacenados.
# Debemos usar el método VALUES()-

print('MOSTRAR LOS VALORES ALMACENADOS') # Muestro título.
x = product.values() #  Creo una var con los valores almacenados de nuestro diccionario. 
print(x) # Muestro var. En este caso será 'book' '1234' '2.5' 'fiction'.
input() # Salgo con enter.


# Si quisieramos visualizar los elementos almacenados en nuestro diccionario
# debemos hacerlo mediante el método ITEMS()

print('MOSTRAR LOS ITEMS ALMACENADOS') # Muestro título.
x = product.items() # Creo variable y le asigno como valor los items de nuestro diccionario.
print(x) # Muestro var.
input() # Salgo con enter.
