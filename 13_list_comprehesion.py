### List Comprehesion ###

my_original_list = [0,1,2,3]
print(f'My original list = {my_original_list}')

my_list = []
for i in my_original_list:
    my_list.append(i)
print(f'my_list = {my_list}')

my_list_comprehesion = [i for i in my_original_list]
print('my_list_comprehesion= {}'.format(my_list_comprehesion))

my_list_80 = [i for i in range(0,81)]
print(my_list_80)

my_multiply_list = [i*2 for i in my_original_list]
print(f'my_multiply_list = {my_multiply_list}')

def suma_uno(first):
    return first +1


my_sum_list = [suma_uno(i) for i in my_original_list]
print(f'my_sum_list = {my_sum_list}')
print(list(map(suma_uno, my_original_list)))

my_lambda_list = [(lambda first: first+5) (i) for i in my_original_list]
print(f'my_lambda_list = {my_lambda_list}')