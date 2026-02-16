import random
import mysql.connector

def get_query():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "your_password",
        database = "game_project",
    )
    return connection

def get_random_item():
    connection = get_query()
    cursor = connection.cursor()

    sql = """
    SELECT 
        item_name,
        item_type,
        item_rarity,
        item_skill1,
        item_skill2,
        item_skill3,
        item_skill4
    FROM items
    WHERE item_region = %s
    """

    cursor.execute(sql, ("Red",))
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    if not results:
        return None

    # Pick one random row
    row = random.choice(results)

    # Unpack the tuple
    (
        item_name,
        item_type,
        item_rarity,
        skill1,
        skill2,
        skill3,
        skill4
    ) = row

    skills = list(filter(None, (skill1, skill2, skill3, skill4)))

    return {
        "name": item_name,
        "type": item_type,
        "rarity": item_rarity,
        "skills": skills
    }


# ---- Usage ----
item = get_random_item()

class RedItems:
    def __init__(self, damage_dealt, armor_strength, shield_strength, healing_done, name, type, rarity, skills ):
        self.damage_dealt = damage_dealt,
        self.armor_strength = armor_strength,
        self.shield_strength = shield_strength,
        self.healing_done = healing_done,
        self.name = name,
        self.type = type,
        self.rarity = rarity,
        self.skills = skills

    def __str__(self):
        return f"NAME: {self.name}, TYP: {self.type},RARITY:{self.rarity}, SKL: {self.skills}\nDMG : {self.damage_dealt}, AR: {self.armor_strength}, SR: {self.shield_strength}, HEAL: {self.healing_done}"


class RedWeapons(RedItems):
    @classmethod
    def create(cls):
        red_item_points = random.randint(24, 35)
        red_item_multiplier = 2.6
        if item:
            red_item_name = (item["name"])
            red_item_type = (item["type"])
            red_item_rarity = (item["rarity"])
            red_item_skills = (item["skills"])
        return cls (
            name = red_item_name,
            type = red_item_type,
            rarity = red_item_rarity,
            skills = red_item_skills,
            damage_dealt = red_item_points * red_item_multiplier,
            armor_strength = red_item_points * red_item_multiplier,
            shield_strength = red_item_points * red_item_multiplier,
            healing_done = red_item_points * red_item_multiplier

        )

redItem = RedWeapons.create()
print(redItem)