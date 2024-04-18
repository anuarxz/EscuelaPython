### Regular expressions ###

import re

my_string = 'Esta es una lección de expresiones regulares. Lección numero 20'
my_other_string = 'Hola Esta es una lección 6 de este curso'


# match # Solo busca desde el principio del string

macheo = re.match('Esta es una lección', my_string, re.I)
print(macheo)
start, end = macheo.span()
print(my_string[start:end])

# search # Busca el patrón en toda la cadena de texto

search = re.search('Esta es una lección', my_other_string, re.I)
print(search)
start, end = search.span()
print(my_other_string[start:end])

# findall

findall = re.findall('lección', my_string, re.IGNORECASE)
print(findall)

# split

print(re.split(':', my_string))

# sub
print(re.sub("[l|L]ección", "LECCIÓN", my_string))


# Patrones de regex

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\.'
print(re.split(pattern, my_string))



my_string_fechas = 'Rondaba 1994/11/09 cuando en Fuerteventura nación Alex'
pattern = r'\d{4}/\d{2}/\d{2}'
print(re.findall(pattern, my_string_fechas))

my_string_email = 'El mail de alex es amarco@viewnext.com y no tiene gmail'
pattern = r'.?@.\b'
print(re.findall(pattern, my_string_fechas))