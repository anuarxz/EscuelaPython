### Clase ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(type(MyEmptyPerson()))


class MyPerson:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f'{self.name} {self.surname}'

    def get_name(self):
        return self.name


persona1 = MyPerson('Alex', 'Marco')
print(persona1.name)
persona1.name = 'Alexander'
print(persona1.get_name())

class MyPerson2:
    def __init__(self, name, surname):
        self.__name = name # Propiedad privada
        self.surname = surname
        self.full_name = f'{self.__name} {self.surname}'

    def get_name(self):
        return self.__name
    
persona2 = MyPerson2('Alex', 'Marco')
print(persona2.surname)
persona2.__name= 'Alexander'
print(persona2.__name)
print(persona2.get_name())
print(persona2.full_name)
# print(persona2.__name) Esto da error

# persona2.__name


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

persona3 = Persona('Alex', 'Marco')
persona3.walk()
persona3.add_skills('Python')
persona3.add_skills('SQL')

print(persona3.skills)


class Student(Persona):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def person_info(self):
        print( f'{self.full_name} tiene las siguientes skill {self.skills}')
    
    def eliminar_ultima_skill(self, skill):
        self.add_skills(skill)
        skills = self.skills
        print(skills)
        self.skills = skills.pop()
        print(self.skills)


s1 = Student('Alex', 'Marco')
# s1.add_skills('Python')
s1.eliminar_ultima_skill('Machine learning')

class Student(Persona, MyPerson):
    def __init__(self, name, surname):
        super().__init__(name, surname)

s2 = Student('Alex', 'Marco')
s2.get_name()