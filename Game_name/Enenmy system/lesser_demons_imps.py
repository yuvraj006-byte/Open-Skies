import random
class Lesser_Demons:
    def __init__(self, health, attack, defence, name, attack_types):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.name = name
        self.attack_types = attack_types

    def __str__(self):
        return f"{self.name} | HP: {self.health}, ATK: {self.attack}, DEF: {self.defence}, ATK_TYPE: {random.choice(self.attack_types)}"
        
class Lesser_Demon_imps(Lesser_Demons):
    @classmethod
    def create(cls):
        return cls(
            health = random.randint(80, 120),
            attack = random.randint(10, 15),
            defence = random.randint(0,3),
            name = "Imps",
            attack_types = ["Small Fire Balls."]
        )

class Lesser_Demon_hellhounds(Lesser_Demons):
    @classmethod
    def create(cls):
        return cls(
            health = random.randint(80, 120),
            attack = random.randint(10, 15),
            defence = random.randint(0,3),
            name = "Hell hounds",
            attack_types = ["Hell Bite.", "Death Pounce."]
        )
imp = Lesser_Demon_imps.create()
hellhound = Lesser_Demon_hellhounds.create()

Lesser_Demon_List = [imp, hellhound]
print(random.choice(Lesser_Demon_List))