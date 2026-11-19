from abc import ABC, abstractmethod
import inspect

class Animal(ABC):
    def __init__(self, name, habitat):
        self.name=name
        self.habitat=habitat

    def display(self):
        print(f"Name: {self.name} | Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, habitat, breed):
        Animal.__init__(self,name,habitat)
        self.breed=breed
    def speak(self):
        print(f"{self.name}({self.breed})says: WOOF! WOOF!!")

class Parrot(Animal):
    def __init__(self,name,habitat,phrase):
        super().__init__(name,habitat)
        if phrase=="":
            phrase="Hello"
        self.phrase=phrase
    def speak(self):
        print(f"{self.name} says: {self.phrase}!{self.phrase}")

class Lion(Animal):
    def __init__(self,name,habitat,pride):
        Animal.__init__(self,name,habitat)
        self.pride=pride

    def speak(self):
        print(f"{self.name} pride: ({self.pride}) says: ROAARRR!!!")

    def run_show(animals):
        if len(animals)==0:
            print("No animals in the show yet.")

