import random
class LesserDemons:
    def __init__(self, health, attack, defence, name, attack_types):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.name = name
        self.attack_types = random.choice(attack_types)

    def __str__(self):
        return f"{self.name} | HP: {self.health}, ATK: {self.attack}, DEF: {self.defence}, ATK_TYPE: {self.attack_types}"
        
class LesserDemonimps(LesserDemons):
    @classmethod
    def create(cls):
        return cls(
            health = random.randint(80, 120),
            attack = random.randint(10, 15),
            defence = random.randint(0,3),
            name = "Imps",
            attack_types = ["Small Fire Balls."]
        )

class LesserDemonhellhounds(LesserDemons):
    @classmethod
    def create(cls):
        return cls(
            health = random.randint(80, 120),
            attack = random.randint(10, 15),
            defence = random.randint(0,3),
            name = "Hell hounds",
            attack_types = ["Hell Bite.", "Death Pounce."]
        )
imp = LesserDemonimps.create()
hellhound = LesserDemonhellhounds.create()

LesserDemon_List = [imp, hellhound]
print(random.choice(LesserDemon_List))