# REMOVE ITEMS FROM DICTIONARIE
# We can remove or delete items from our dictionarie.
# To do this, we have to use the POP() method.

print('REMOVE ITEM WITH POP()') # Display title
product = { # Open dictio
    'art' : 'book',
    'code' : 1234,
    'price' : 2.5,
    'genre' : 'fiction'
} # Close diction

print(product) # Display dictio

product.pop('genre') # Remove the specified item with pop() method. In this case, 'genre' was removed.
print(product) # Display 
input()


# Also we can remove the last item inserted with POPITEM() method.

print('REMOVE LAST ITEM INSERTED')
product = {
    'art' : 'book',
    'code' : 1234,
    'price' : 2.5,
    'genre' : 'fiction'
}

print(product)

product.pop('genre')
print(product)
