class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog is barking")

class puppy(animal):
    def sleep(self):
        print("Puppy is sleeping")
        
d = dog()
d.eat() 
d.bark() 

p = puppy()
p.eat()
p.sleep()


        