class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a positive integer")
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

    def is_adult(self):
        return self.age >= 18

    def birthday(self):
        self.age += 1

    def rename(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("New name must be a string")
        self.name = new_name
