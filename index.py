class Person:
    def move(self):
        print("Move 4 paces")
    def rest(self):
        print("Gains 4 health points")

class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")

class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Moves 6 paces") 

class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisible")
    def heal(self):
        print("Heals 15 health points")   
    def move(self):
        print("Moves 5 paces")

character1=Wizard()
character1.move()
character1.rest()

character1.heal()