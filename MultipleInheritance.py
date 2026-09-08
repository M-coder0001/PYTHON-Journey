class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog is barking")

class cat(animal):
    def meow(self):
        print("Cat is meowing")

class pet(dog, cat):
    def play(self):
        print("Pet is playing")

p = pet()
p.eat()  
p.bark()  
p.meow()  
p.play()  
