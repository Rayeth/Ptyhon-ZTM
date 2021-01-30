class Archer():
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    arrow_counter = 1
    quiver_counter = 0



    def attack(self):
        
        print(f'You have {self.num_arrows - Archer.quiver_counter} in your quiver. Attack with 1 arrow. Arrows left: {self.num_arrows - Archer.arrow_counter}')
        Archer.arrow_counter += 1
        Archer.quiver_counter += 1

archer1 = Archer('Bob', 100)

archer1.attack()
archer1.attack()
archer1.attack()
archer1.attack()


