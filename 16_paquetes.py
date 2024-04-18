### Paquetes ###

# PIP https://pypi.org
# pip install pip

# pip install pandas

import pandas as pd
import numpy as np

my_list = [12,36,58]
print(type(my_list))

numpy_array = np.array([12,36,58])
print(type(numpy_array))
print(numpy_array)

import math

print(math.sqrt(25))

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())