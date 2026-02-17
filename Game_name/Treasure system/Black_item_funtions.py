import random
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cat",
        database="game_project",
    )


def get_random_black_item():
    connection = get_connection()
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

    cursor.execute(sql, ("Black",))
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    if not results:
        return None

    row = random.choice(results)

    item_name, item_type, item_rarity, s1, s2, s3, s4 = row

    skills = [skill for skill in (s1, s2, s3, s4) if skill]

    return {
        "name": item_name,
        "type": item_type,
        "rarity": item_rarity,
        "skills": skills
    }


def generate_black_stats(item_type, item_rarity):

    base_points = random.randint(80, 100)

    if item_rarity == "Common":
        rarity_multiplier = 1.2
    elif item_rarity == "Rare":
        rarity_multiplier = 1.5
    else:
        rarity_multiplier = 1.8

    if item_type == "Weapons":
        damage = base_points * 3.0
        armor = base_points * 0.6
        shield = base_points * 0.4
        healing = 0

    elif item_type == "Armor":
        damage = base_points * 0.6
        armor = base_points * 3.0
        shield = base_points * 2.0
        healing = 0

    elif item_type == "Shields":
        damage = base_points * 0.4
        armor = base_points * 2.0
        shield = base_points * 3.0
        healing = 0

    elif item_type == "Medicine":
        damage = 0
        armor = 0
        shield = 0
        healing = base_points * 4.0

    else:
        damage = base_points
        armor = base_points
        shield = base_points
        healing = base_points

    damage *= rarity_multiplier
    armor *= rarity_multiplier
    shield *= rarity_multiplier
    healing *= rarity_multiplier

    return {
        "damage": round(damage, 1),
        "armor": round(armor, 1),
        "shield": round(shield, 1),
        "healing": round(healing, 1)
    }


def create_black_item():

    item = get_random_black_item()

    if not item:
        print("No Black items found.")
        return None

    stats = generate_black_stats(item["type"], item["rarity"])

    full_item = {
        "name": item["name"],
        "type": item["type"],
        "rarity": item["rarity"],
        "skills": item["skills"],
        "damage": stats["damage"],
        "armor": stats["armor"],
        "shield": stats["shield"],
        "healing": stats["healing"]
    }

    return full_item


def print_item(item):

    print("\n--- BLACK ITEM GENERATED ---")
    print("Name:", item["name"])
    print("Type:", item["type"])
    print("Rarity:", item["rarity"])
    print("Skills:", ", ".join(item["skills"]) if item["skills"] else "None")
    print("Damage:", item["damage"])
    print("Armor:", item["armor"])
    print("Shield:", item["shield"])
    print("Healing:", item["healing"])


if __name__ == "__main__":

    black_item = create_black_item()

    if black_item:
        print_item(black_item)
