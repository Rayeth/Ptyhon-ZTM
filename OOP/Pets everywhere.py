class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    @classmethod
    def show_cls(cls):
        print(cls.animals)

    def show(self):
        print(self.animals)

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Dog():
    is_lazy = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Rex(Dog):
    def sing(self, sounds):
        return f'{sounds}'

class Iceberg(Dog):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Bobby(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)

my_cats = [Simon('Simon', 7), Sally('Sally', 5), Bobby('Bobby', 6)]
#3 Instantiate the Pet class with all your cats use variable my_pets


cats = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
print(cats.walk())

my_dogs = [Rex('Rex', 10), Iceberg('Iceberg', 6)]

cats.show()
dogs = Pets(my_dogs)

dogs.show()

Pets.show_cls()

print(my_cats[0].is_lazy)

