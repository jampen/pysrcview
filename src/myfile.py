class Animal:
    def __init__(self):
        self.name = 'animal'

    def eat(self):
        pass

    def speak(self):
        pass


class Cat (Animal):
    def hiss(self):
        print('hisss')


class Dog(Animal):
    def bark(self):
        print('woof')


class Puppy(Dog):
    def pet(self):
        print('thanks')


dog = Dog()
