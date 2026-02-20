import random


# RED - Demon Negotiation
# A risky temptation. Accepting power may help or harm you.
def red_demon_negotiation():

    print("\nA demon offers you forbidden power.")
    print("1 - Accept the power")
    print("2 - Refuse")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        chance = random.randint(1, 100)

        if chance <= 50:
            print("The power strengthens you.")
            return True
        else:
            print("The demon corrupts you.")
            return False

    elif choice == "2":
        print("You resist temptation.")
        return True

    return False


# RED - Runic Seal
# Solve the rune correctly to open the ancient door.
def red_runic_seal():

    print("\nAn ancient stone door blocks your path.")
    print("Three glowing runes appear:")
    print("1 - Flame Rune")
    print("2 - Frost Rune")
    print("3 - Storm Rune")
    print("\nHint: 'Only cold can calm rising flame.'")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "2":
        print("The frost rune suppresses the magic.")
        return True

    print("The seal releases a burst of energy.")
    return False


# RED - Ancient Lock
# Interpret the inscription correctly to unlock the gate.
def red_ancient_lock():

    print("\nAn iron gate stands before you.")
    print("Symbols carved above it:")
    print("Sun  Moon  Star  Crown")
    print("\nInscription:")
    print("'Only that which rules the night may pass.'")

    answer = input("Type the correct symbol name: ")

    if answer.lower() == "moon":
        print("The gate unlocks with a heavy click.")
        return True

    print("The mechanism jams.")
    return False


# RED - Duel of Strength
# Compete in raw strength against a lesser demon.
def red_duel():

    print("\nA demon challenges you.")
    print("Choose your strength (10–20).")

    player = int(input("Enter your attack number: "))
    demon = random.randint(12, 22)

    print("You roll:", player)
    print("Demon rolls:", demon)

    if player > demon:
        return True

    return False


# RED - Iron Will
# Resist temptation to avoid a hidden curse.
def red_iron_will():

    print("\nA chest glows brightly.")
    print("Type 'open' to open it.")
    print("Or type anything else to walk away.")

    action = input("Your decision: ")

    if action.lower() != "open":
        print("You resist the trap.")
        return True

    print("The chest was cursed.")
    return False


# RED - Corrupted Survivor
# Decide whether to help a suspicious stranger.
def red_survivor():

    print("\nA wounded survivor begs for help.")
    print("Their eyes glow faintly red.")
    print("1 - Help them")
    print("2 - Walk away")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        chance = random.randint(1, 100)

        if chance <= 40:
            print("They were corrupted.")
            return False
        else:
            print("You saved an innocent person.")
            return True

    elif choice == "2":
        print("You avoid possible danger.")
        return True

    return False


# RED - Forest Path
# Choose a path through uncertain terrain.
def red_forest_path():

    print("\nYou reach a fork in the road.")
    path = input("Type 'left' or 'right': ")

    safe_path = random.choice(["left", "right"])

    if path.lower() == safe_path:
        print("You chose the safer path.")
        return True

    print("You walk into danger.")
    return False


# RUN RED SIDE QUEST
def run_red_side_quest():

    print("\nRED SIDE QUEST STARTED")

    quests = [
        red_demon_negotiation,
        red_runic_seal,
        red_ancient_lock,
        red_duel,
        red_iron_will,
        red_survivor,
        red_forest_path
    ]

    quest = random.choice(quests)
    result = quest()

    if result:
        print("\nYou succeed. Medium reward granted.")
    else:
        print("\nYou fail. You take damage.")


if __name__ == "__main__":
    run_red_side_quest()
