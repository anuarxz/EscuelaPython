## Tuplas ##

my_tuple = tuple()
my_other_tuple = (15)

my_tuple = (35, 17, 250)
print(my_tuple)

my_tuple = (36, 15, 250, 84, 250)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[0:-1])

print(my_tuple.count(36))
print(my_tuple.index(250))

print(my_other_tuple)
del my_other_tuple
print(my_other_tuple)