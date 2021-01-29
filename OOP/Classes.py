#OOP

class PlayerCharacter:

    #Class Object Attribute
    membership = True

    # constructor function
    def __init__(self, name, age): 

        self.name = name # attribute
        self.age = age # attribute
    def run(self):
        print('run')

player1 = PlayerCharacter('Bob', 27)
player2 = PlayerCharacter('Marta', 25)

print(player1.membership)
print(player2.membership)