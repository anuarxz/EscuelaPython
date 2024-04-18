### Listas ###

my_list = list()
my_other_list = []

my_list = [35, 17, 52, 15, 35]
print(my_list)

my_string = ' Hola'

my_other_list = [174, my_string, 'Mundo', True]
print(my_other_list)

print(my_list[0])
print(my_list[-1])

print(my_list.count(35))

print(my_list + my_other_list)

my_list.insert(1, 27) # Inserta en una posición específica
print(my_list)

my_list.append(1000) # Inserta siempre al final de la lista
print(my_list)

my_list.remove(35) # Elimina la primera coincidencia que cumple la condición
print(my_list)

my_list.pop() # Elimina el último valor de la lista
print(my_list)

my_list = [35, 17, 52, 15, 35]
print(my_list)
my_list = [35, 17, None, 15, 35]
print(my_list)


my_new_list = [[1,2,3], my_list] # Listas de listas
print(my_new_list)

print(my_new_list[1][2])
print(my_list.index(17))