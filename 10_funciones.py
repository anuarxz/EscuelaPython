## Funciones ##

def my_function():
    print('Esto es una función')

my_function()


def sum_two_values(first_value:int, second_value):
    '''
    first_value: int = Primer valor a sumar
    second_value: int = Segundo valor a sumar
    '''
    my_sum = first_value + second_value
    return my_sum

suma = sum_two_values(5, 3)
print(suma)

suma = sum_two_values('5', '3')
print(suma)

suma = sum_two_values(second_value=-5, first_value=3)
print(suma)


def print_full_name(nombre, apellido, alias='Sin Alias'):
    print(f'{nombre} ({alias}) {apellido}')

print_full_name('Alex', 'Marco')
print_full_name('Alex', 'Marco', 'amarco')

def print_full_name(nombre, apellido, alias='Sin Alias',edad=None, delegacion=None, lenguajes=None):
    print(f'{nombre} ({alias}) {apellido} de edad {edad} en la delegacion {delegacion} domina {lenguajes} lenguajes')

print_full_name('Alex', 'Marco', edad=29, delegacion='Valencia', lenguajes='Python')

def print_upper_text(nombre, *args):
    print(type(args))
    for i in args:
        print(i.upper())
    print(nombre)

print_upper_text('Hola','Mundo', nombre='Alex')



