### String ###

my_string = 'My string'
my_other_string = 'My other string'

print(len(my_string))

print("Hola esto es un string")
print("Ella dijo \"Sí\"")
print('Ella dijo "Si"')

print('Esto es una tabulación: \t Hola')
print('Literalmente esto es una tabulación: \\t')

print(r'C:\Users\0016371\Desktop\EscuelaPython\Escuela022024')
print('Esto es un booleano:', True, 'Y esto es otro', False)
print('Esto es un str: {} Y esto es otro: {}'.format(my_string, my_other_string))
print(f'Esto es un string {my_string}, y esto esto es otro: {my_other_string}')

name = 'Alex'
saludo = 'hola mundo'

print('Mi nombre es %s' %(name))


print(name[0])
print(name[2])
print(my_other_string[-1])
print(my_other_string[-6])
print(my_other_string[3:])
print(my_other_string[:4])
print(my_other_string[3:-2])

print(name[3:-4])
print(name[3], name[-3])

print(saludo[0:-1:2])
print(saludo[::2])

print(name[0:2])