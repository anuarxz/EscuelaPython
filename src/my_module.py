def sum_two_values(first_value:int, second_value):
    '''
    first_value: int = Primer valor a sumar
    second_value: int = Segundo valor a sumar
    '''
    my_sum = first_value + second_value
    return my_sum

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f'{self.name} {self.surname}'
        self.skills = []

    def get_name(self):
        return self.full_name
    
    def walk(self):
        print(f'{self.get_name()} está caminando y tiene estas skills {self.skills}')

    def add_skills(self, skill):
        saludo = 'Hola Mundo'
        self.skills.append(skill)