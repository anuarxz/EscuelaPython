## Modulos ##

import src.my_module as my_module
print(my_module.sum_two_values(5,3))
print(my_module.sum_five(5))

import src.my_module as mm
print(mm.sum_two_values(5,3))
print(mm.sum_five(5))

from src.my_module import sum_two_values, sum_five
print(sum_two_values(5,3))
print(sum_five(5))

p1 = mm.Persona('Alex', 'Marco')
print(p1.get_name())