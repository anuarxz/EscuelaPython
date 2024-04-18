### Exceptions ###

numberOne = 5
# numberTwo = 1
numberTwo = "1"

# print(numberOne + numberTwo)

# try:
#     print(numberOne + numberTwo)
#     print('No se ha producido error')
# except:
#     # Se ejecuta si se produce una excepción
#     print('Se ha producido un error')


# def sum_two_values(first: int, second:int):
#     try:
#         return first + second
#     except:
#         print('Se ha producido un error. Por favor pasa dos números enteros')

# sum_two_values(1, '5')


# try:
#     print(numberOne + numberTwo)
#     print('No se ha producido error')
# except ValueError:
#     print('Se ha producido un ValueError')
# except TypeError:
#     print('Se ha producido un TypeError')


try:
    print(numberOne + numberTwo)
    print('No se ha producido error')
except Exception as e:
    print(e)


# try:
#     print(numberOne + numberTwo)
#     print('No se ha producido error')
# except:
#     # Se ejecuta si se produce una excepción
#     print('Se ha producido un error')
# else: # Opcional
#     print('La ejecución continúa correctamente')
# finally:
#     print('La ejecución pasa por el finally')