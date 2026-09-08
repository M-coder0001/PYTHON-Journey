class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog is barking")

class puppy(dog):
    def sleep(self):
        print("Puppy is sleeping")
        
p = puppy()
p.eat()  # Inherited method from animal class
p.bark()  # Inherited method from dog class
p.sleep()  # Method from puppy class
