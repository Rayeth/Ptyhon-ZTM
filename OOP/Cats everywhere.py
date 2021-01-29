#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Bob', 6)
cat2 = Cat('Kinia', 9)
cat3 = Cat('Ray', 3)
   

# 2 Create a function that finds the oldest cat

def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')

# Additional, find the name of that cat
oldest_var = oldest_cat(cat1.age, cat2.age, cat3.age)


def oldest_cat_name(*args):
    for arg in args:
        if arg.age == oldest_var:
             print(f'Oldest cat is {arg.name}')
        else:
            continue
    

oldest_cat_name (cat1, cat2, cat3)
        


    