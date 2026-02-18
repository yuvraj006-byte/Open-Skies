import random


# RED - Demon Negotiation
# A demon tempts you with forbidden strength. Accepting it may empower or corrupt you.

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


# RED - Wire Trap
# A deadly trap blocks your path. Only one wire will disable it.

def red_trap_wire():

    print("\nThree wires block your path.")
    print("Red wire hums loudly.")
    print("Blue wire feels cold.")
    print("Green wire vibrates fast.")

    correct_wire = "blue"

    choice = input("Which wire do you cut? ")

    if choice.lower() == correct_wire:
        print("Trap disabled.")
        return True
    else:
        print("The trap explodes.")
        return False


# RED - Trial of Flame
# Solve the demon’s riddle or fail the trial.

def red_riddle():

    print("\nThe more you feed me, the stronger I grow.")
    print("But if you give me water, I die.")
    print("What am I?")

    answer = input("Your answer: ")

    if answer.lower() == "fire":
        return True

    return False


# RED - Symbol Memory
# Remember the demon’s pattern.

def red_symbol_memory():

    pattern = random.choice(["X O X O", "O X O X", "X X O O"])

    print("\nThe demon shows symbols:", pattern)
    input("Press Enter to continue...")

    answer = input("Repeat the pattern exactly: ")

    if answer == pattern:
        return True

    return False


# RED - Sequence Trial
# Complete the number pattern.

def red_sequence():

    print("\n3, 6, 9, 12, ?")

    answer = input("Next number: ")

    if answer == "15":
        return True

    return False


# RED - Duel of Strength
# Face a lesser demon in combat.

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


# RED - Corrupted Survivor
# A wounded survivor may not be what they seem.

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


def run_red_side_quest():

    print("\nRED SIDE QUEST STARTED")

    quests = [
        red_demon_negotiation,
        red_trap_wire,
        red_riddle,
        red_symbol_memory,
        red_sequence,
        red_duel,
        red_survivor
    ]

    quest = random.choice(quests)
    result = quest()

    if result:
        print("\nYou succeed. Medium reward granted.")
    else:
        print("\nYou fail. You take damage.")


if __name__ == "__main__":
    run_red_side_quest()
