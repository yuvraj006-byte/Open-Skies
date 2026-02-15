import random
lesser_demon_imps_attack_types = ["Small Fire Balls."]

class Enemy_Type_Lesser_Demons:
    def __init__(self, health, attack, defence):
        self.health = health
        self.attack = attack
        self.defence = defence

    def __str__(self):
        return f"Health: {self.health}, Attack: {self.attack}, Defence: {self.defence}"            
        

def Lesser_Demon_imps():
    health = random.randint(80, 120)
    attack = random.randint(10, 15)
    defence = random.randint(0,3)

    return health, attack, defence

Lesser_Demon_imps_stats = Lesser_Demon_imps()

demon_type_imps = Enemy_Type_Lesser_Demons(*Lesser_Demon_imps_stats)
print(demon_type_imps)
print(f"They are Firing {random.choice(lesser_demon_imps_attack_types)}")