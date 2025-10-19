class Dog:
    def speak(self):
        print("汪汪")
class Cat:
    def speak(self):
        print("喵喵")

def animal_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(cat)