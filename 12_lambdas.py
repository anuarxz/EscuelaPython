## lambdas ##

def sum_two_values(first_value:int, second_value):
    return first_value + second_value

sum_two_values(1,3)

def sum_five(value):
    return value +5

def sum_one(value):
    return value +1

lambda first, second: first+second

sum = lambda first, second: first+second
print(sum(1,2))

print(type(sum))

suma_f = lambda first, f: f(first)
print(suma_f(1, sum_five))
print(suma_f(3, sum_one))