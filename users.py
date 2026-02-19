class User:
    def __init__(self, rut, age, name, lastname):
        self.rut = rut
        self.age = age
        self.name = name
        self.lastname = lastname

    def id(self):
        print(f"Rut: {self.rut}, Age: {self.age}, Name: {self.name} {self.lastname}")


users = [
    User("21.859.xxx-x", 20, "Rodrigo", "Sánchez"),
    User("18.432.xxx-k", 25, "Ana", "García"),
    User("15.987.xxx-2", 35, "Juan", "Pérez"),
    User("21.974.xxx-2", 20, "Gabriel", "Azocar"),
    User("17.483.xxx-x", 27, "Julian", "Alvarez"),
]

for user in users:
    user.id()
