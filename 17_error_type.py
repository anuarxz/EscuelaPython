### Error type ###

import math

# NameError
lenguaje = 'Spanish' # Comentar para obtener el error
print(lenguaje)

#IndexError
my_list = ['Python', 'R', 'Java', 'Node']
print(my_list[0])
# print(my_list[18])  # Descomentar para obtener el error

# ModuleNotFoundError
# import emoji # Descomentar para obtener el error

# AttributeError
print(math.pi)
# print(math.PI) # Descomentar para obtener el error

# KeyError
my_dict = {'Nombre':'Alex', 'Apellido':'Marco'}
print(my_dict['Nombre'])
# print(my_dict['Edad']) # Descomentar para obtener el error

# TypeError
print(my_list[0])
# print(my_list["0"]) # Descomentar para obtener el error

# ImportError
# from math import PI  # Descomentar para obtener el error

# ValueError
my_int = int('10')
print(type(my_int))
# my_int = int('10 años') # Descomentar para obtener el error

# ZeroDivisionError
print(4/2)
# print(4/0) # Descomentar para obtener el error