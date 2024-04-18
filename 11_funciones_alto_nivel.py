## Funciones de alto nivel ##

from functools import reduce


def sum_one(value):
    return value +1

def sum_five(value):
    return value +5

def sum_two_values_and_add(first, second, fun):
    return fun(first + second)

print(sum_two_values_and_add(5,3,sum_one))
print(sum_two_values_and_add(5,3,sum_five))


# Map

numbers = [2,5,10,15,20]

def multiply_two(number):
    return number * 2

print(map(multiply_two, numbers))
print(list(map(multiply_two, numbers)))
print(list(map(sum_five, numbers)))


# Reduce

def sum_two_values(first, second):
    print(first)
    print(second)
    my_sum=first+second
    return my_sum

print(reduce(sum_two_values, numbers))

print(reduce(sum_two_values, range(0,51)))
