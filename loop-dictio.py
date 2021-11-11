# LOOP WITH DICTIONARIES
# Python allow loop trough a dictionary with FOR function.
# They can be trough KEYS, VALUES, or BOTH.

# DISPLAY KEYS IN THE DICTIONARY
print('DISPLAY KEYS IN THE DICTIONARY') # Display title
product = { # Open dictio
  'art' : 'book', 
  'code' : 1234,
  'price' : 2.5,
  'genre' : 'fiction'
} # Close dictio

for items in product: 
  print(items) # Display var item.
input()

# Also, we can loop trough VALUES in the dictionary.

print('DISPLAY VALUES IN THE DICTIONARY') # Display title
for items in product.values(): 
  print(items)
input()


# If you wish display KEYS and VALUES need to use ITEMS() method.
print('DISPLAY KEYS AND VALUES') # Display title
for keys, values in product.items():
    print(keys, values)
input()
