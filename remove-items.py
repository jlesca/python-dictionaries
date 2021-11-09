# REMOVE ITEMS FROM DICTIONARY
# We can remove or delete items from our dictionary.
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
print(product) # Display dictio updated 
input()


# Also we can remove the last item inserted with POPITEM() method.

print('REMOVE LAST ITEM INSERTED') # Display title
product = { # Open dictio
    'art' : 'book',
    'code' : 1234,
    'price' : 2.5,
    'genre' : 'fiction'
} # Close dictio

print(product) # Display dictio

product.pop('genre') # Remove the last inserted item. In this case 'genre'
print(product) # Display dictio updated
input()

# CLEAR DICTIONARY
# If you wish clear the dictionary complete, can use CLEAR() method.

print('CLEAR DICTIONARY') # Display title
product.clear() # Clear items from dictio
print(product) # Display dictio updated. In this case it will be '{}'
input()

# DELETING DICTIO
# You can to delete completely the dictionary with DEL keyword.

del product # Deleting dictio
print(product) # Display dictio, but will be an error. NameError: name 'product' is not defined
