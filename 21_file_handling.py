### Ficheros ###

# .txt file

# open('ruta', modo) # mode (r, a, w, t, b)

# Escribir o crear un fichero
text_file = open(r'data/my_file.txt', 'w+')
print(text_file)

text_file.write('Mi nombre es Alex\nMi apellido es Marco\nY mi lenguaje de programacion favorito es Python')
text_file.close()

# Leer ficheros
f = open(r'data/my_file.txt')
txt = f.read()
print(txt)
print(type(txt))
f.close()

f = open(r'data/my_file.txt')
print(f.readline())
print(f.readline())
f.close()

f = open(r'data/my_file.txt')
print(f.read(11))
f.close()

with open(r'data/my_file.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines[1])

with open(r'data/my_file.txt', 'a') as f:
    f.write('\nEste texto es un append')

# Eliminar fichero
import os

# ruta_fichero = r'data/my_file.txt'
# if os.path.exists(ruta_fichero):
#     os.remove(ruta_fichero)
# else:
#     print('El fichero no existe')

carpeta =  r'data/'
archivos = os.listdir(carpeta)
for archivo in archivos:
    if  archivo == 'my_file.txt':
        with open(carpeta+archivo) as f:
            lines = f.read().splitlines()
            # print(type(lines))
            print(lines[1])
    if archivo.startswith('P3'):
        print(archivo)


# JSON
import json
        
person_dict = {'name': 'Alex', 'surname': 'Marco', 'Skills': ['Python', 'R']}
with open(r'data/persona.json', 'w') as f:
    json.dump(person_dict, f, ensure_ascii=False, indent=4)


with open(r'data/persona.json') as f:
    person_dict = json.load(f)
    print(person_dict)


# PDF
from PyPDF2 import PdfReader
def get_pdf_text(pdf_doc):
    text = ''
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages[:5]:
        text += page.extract_text()
    return text

get_pdf_text(r'data/1911.01547.pdf')
with open(r'data/pdf_text.txt', 'w', encoding='UTF-8') as f:
    f.write(get_pdf_text(r'data/1911.01547.pdf'))
