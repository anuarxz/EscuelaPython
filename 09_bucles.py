### Bucles ###

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition +=2
else:
    print('Mi condicion es mayor o igual que 10')


my_condition = 0
while my_condition < 20:
    my_condition+=1
    if my_condition == 5:
        print('Entro por el if\nDetengo la ejecución')
        break
    print(my_condition)

# For
print('-'*50)
my_list = [1,2,3,4,5]
for i in my_list:
    print(i)

print('-'*50)
for i in my_list:
    if i ==3:
        break
    else:
        i+=10
    print(i)

print('-'*50)
for i in my_list:
    if i ==3:
        pass # Continua ejecutando el resto del bucle
    else:
        i+=10
    print(i)

print('-'*50)
for i in my_list:
    if i ==3:
        continue # Pasa al siguiente elemento del bucle
    else:
        i+=10
    print(i)


my_dict = {'Nombre':'Alex', 'Edad':29}
for elemento in my_dict.values():
    print(elemento)

for i in range(5, 15+1, 2):
    print(i)