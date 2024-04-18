### Variables ###

my_variable : str = 'My string variable'
print(my_variable)

my_variable = 'Soy una variable string'
print(my_variable)

my_int_variable : int = 5
print(my_int_variable)

my_int_variable : int = 'My string variable'
print(type(my_int_variable))

a='1 + 1 = '
b = 2
c = True

# print(a+b)  #Error, no se puede concatenar str + int
print(a, b, c)
print('Este es el valor de b: ', b)

print(type(b))
print(type(str(True)))
print(str(True))