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
p.eat()  
p.bark() 
p.sleep()
