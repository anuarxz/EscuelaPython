## Operaciones numericas ##

#built-in functions
# str()
# int()
# float()

suma = 3+2
resta = 3-2
multiplicacion = 3*2
division = 7.4/2
resto = 5%2
parte_entera = 5//2
potencias = 2**3


print('suma = ', suma)
print('resta = ', resta)
print('multiplicacion = ', multiplicacion)
print('division = ', division)
print('resto = ', resto)
print('parte_entera = ', parte_entera)
print('potencias = ', potencias)
print(2**3 + 3 -7 / 1)

# print(int(division))
# print(float(multiplicacion))


print('-'*50)
### Operaciones con cadenas de texto
print('Hola'+'Python')
# print('Hola'-'Python') #Error no se pueden restar str
print('Hola'*3)
print('Hola'+str(2))

print('-'*50)
# Operaciones aritmeticas
print(3<4)
print(3>4)
print(3<=4)
print(3>=4)

print(3==4)
print(3!=4)

print('3'==3)

print('Hola'=='hola')
print('Hola' < 'Python')
print('aaab'<='aaaa')
print('Aaaa'<'aaaa')


print('-'*50)
Nombre1 = 'Alex'
Nombre2 = 'alex'

print(Nombre1 == Nombre2)
print(Nombre1.upper() == Nombre2.upper())


#Operadores logicos
print('-'*50)
print((3<4) and ('Hola'<'Python')) # Se tienen que cumplir ambas condiciones
print((3>4) and ('Hola'<'Python'))
print((3>4) or ('Hola'<'Python')) # Se tiene que cumplir al menos una de las condiciones
print(not(3>4))