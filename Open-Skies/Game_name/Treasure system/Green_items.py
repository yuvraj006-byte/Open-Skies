import random
import mysql.connector


# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def get_query():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cat",
        database="game_project",
    )
    return connection


# -----------------------------
# GET GREEN ITEM NAMES
# -----------------------------
def get_item():
    connection = get_query()
    cursor = connection.cursor()

    sql_name_item = """
        SELECT item_name
        FROM items
        WHERE item_region = 'Green';
    """

    cursor.execute(sql_name_item)

    # Extract only the string from tuple
    result = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return result


# -----------------------------
# GET SKILLS FOR A SPECIFIC ITEM
# -----------------------------
def get_item_skill(item_name):
    connection = get_query()
    cursor = connection.cursor()

    sql_skill_item = """
        SELECT
            item_skill1,
            item_skill2,
            item_skill3,
            item_skill4
        FROM items
        WHERE item_name = %s AND item_region = 'Green';
    """

    cursor.execute(sql_skill_item, (item_name,))

    rows = cursor.fetchall()
    skills = []

    for row in rows:
        for skill in row:
            if skill is not None:
                skills.append(skill)

    cursor.close()
    connection.close()

    return skills


# -----------------------------
# BASE CLASS
# -----------------------------
class GreenItems:
    def __init__(self, damage_dealt, armor_strength, healing_done,
                 barrier_strength, name, skill, type):

        self.damage_dealt = damage_dealt
        self.armor_strength = armor_strength
        self.healing_done = healing_done
        self.barrier_strength = barrier_strength
        self.name = name
        self.skill = skill
        self.type = type

    def __str__(self):
        return (
            f"{self.name} | Type: {self.type} | Skill: {self.skill}\n"
            f"DMG: {self.damage_dealt}, "
            f"ARMOR: {self.armor_strength}, "
            f"HEAL: {self.healing_done}"
        )


# -----------------------------
# WEAPON CLASS
# -----------------------------
class GreenWeapons(GreenItems):

    @classmethod
    def create(cls):

        # Generate stat range for Green region
        green_item_points = random.randint(8, 12)

        # Get random item name from DB
        item_name = random.choice(get_item())

        # Get skills for that specific item
        item_skills = get_item_skill(item_name)

        # Pick random skill if available
        if item_skills:
            skill = random.choice(item_skills)
        else:
            skill = "No Skill"

        return cls(
            damage_dealt=green_item_points,
            armor_strength=green_item_points,
            healing_done=green_item_points,
            barrier_strength=green_item_points,
            name=item_name,
            skill=skill,
            type="Weapon"
        )


# -----------------------------
# TEST
# -----------------------------
greenitem = GreenWeapons.create()
print(greenitem)
