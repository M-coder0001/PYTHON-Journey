class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog is barking")
        
b = dog()
b.eat()  
b.bark()  