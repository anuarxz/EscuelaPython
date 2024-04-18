## Diccionarios ##

my_dict = dict()
my_other_dict = {}

my_dict = {'Nombre':'Alex', 'Edad':29}
print(type(my_other_dict))

print(my_dict['Nombre'])
my_dict['Nombre'] = 'Alexander'
print(my_dict['Nombre'])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_list = ['Nombre', 'Apellido', 'Edad']
my_values = ['Alex', 'Marco', 29]

new_dict = dict.fromkeys(my_list, my_values)
print(new_dict)

# new_dict['Apellido'] = {15, 714}
# print(new_dict)

new_dict['Skills'] = {'Lenguajes de programacion': ['Python', 'SQL', 'Node.js']}
print(new_dict)

print(new_dict['Skills']['Lenguajes de programacion'])