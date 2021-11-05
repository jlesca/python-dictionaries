# CAMBIAR EL VALOR DE LOS ITEMS
# Podremos acceder a una clave de nuestro diccionario y cambiar su valor.
# Teniendo en cuenta el caso de una librería, vamos a cambiar el precio de nuestro producto.

print('CAMBIAR EL VALOR DE UNA CLAVE') # Display tittle.
product = { # Open dictio.
    'art' : 'book', 
    'code' : 1234,
    'price' : 2.5,
    'genre' : 'fiction'
} # Close dictio

print('OLD PRICE: ', product['price']) # Display old price

product['price'] = 3.5 # Update price
print('NEW PRICE: ', product['price']) # Display new price.
input() # Close

# También podemos hacerlo mediante el método UPDATE()

print('CAMBIAR EL VALOR CON UPDATE()') # Display tittle.
product = { # Open dictio.
    'art' : 'book', 
    'code' : 1234,
    'price' : 2.5,
    'genre' : 'fiction'
} # Close dictio

print('OLD PRICE: ', product['price']) # Display old price

product.update({'price' : 3.5}) # With update() we need to use curly brakets to assign the key and value.
print('NEW PRICE: ', product['price']) # Display new price.
input()
