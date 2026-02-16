import random
import mysql.connector

def get_query():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "password",
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

if item:
    print(item["name"])
    print(item["type"])
    print(item["rarity"])
    print(item["skills"])


