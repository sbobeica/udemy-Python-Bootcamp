class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meaw!'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:   #polimorphism
    print(type(pet))
    print(pet.speak())

def pet_speak (pet):        #polimorphism
    print(pet.speak())

print(pet_speak(niko))