import random
import mysql.connector

def get_query():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "your_username",
        password = "Your_passwor",
        database = "game_project", 
    )
    return connection


def get_item():    
    connection = get_query()
    cursor = connection.cursor()
    sql_name_item = """
        SELECT
        item_name,
        item_type
        FROM items
        WHERE item_region = 'Green';
    """

    cursor.execute((sql_name_item))
    result = [row for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    
    return result

def get_item_skill():
    connection = get_query()
    cursor = connection.cursor()
    sql_skill_item = """
        SELECT
        item_skill1, 
        item_skill2, 
        item_skill3, 
        item_skill4 
        FROM items
        WHERE item_region = 'Green';
    """

    cursor.execute((sql_skill_item))

    rows = cursor.fetchall()
    skills = []

    for row in rows:
        for skill in row:
            if skill is not None:
                skills.append(skill)



    cursor.close()
    connection.close()
    
    return skills

class GreenItems:
    def __init__(self, damage_dealt, armor_strength, healing_done, barrier_strength, name, skill, type):
        self.damage_dealt = damage_dealt
        self.armor_strength = armor_strength
        self.healing_done = healing_done
        self.barrier_strenght = barrier_strength
        self.name = name    
        self.skill = skill
        self.type = type
    
    def __str__(self):
        return f"{self.name}, TYP: {self.type}, SKL: {self.skill}\nDMG : {self.damage_dealt}, AR: {self.armor_strength}, HEAL: {self.healing_done}"

class GreenWeapons(GreenItems):
    
    @classmethod
    def create(cls):
        green_item_points = random.randint(8, 12)
        item = random.choice(get_item())
        item_name, item_type = item
        return cls(
            damage_dealt = green_item_points,
            name = item_name,
            type = item_type,
            skill = random.choice(get_item_skill()),
            armor_strength = green_item_points * 1.0,
            barrier_strength = green_item_points * 1.0,
            healing_done = green_item_points * 1.0, 
        )

greenitem = GreenWeapons.create()
print(greenitem)