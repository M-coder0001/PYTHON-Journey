class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog is barking")

class puppy(dog):
    def sleep(self):
        print("Puppy is sleeping")

class kitten(animal):
    def meow(self):
        print("Kitten is meowing")

class cat(animal):
    def meow(self):
        print("Cat is meowing")

a = animal()
d = dog()
p = puppy()
k = kitten()
c = cat()

        