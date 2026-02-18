import random
#Green side quests

# Quest Name: Math Trial
# Description: Solve a simple multiplication question.
def math_quest():

    a = random.randint(2, 10)
    b = random.randint(2, 5)

    answer = int(input(f"What is {a} x {b}? "))

    if answer == a * b:
        return True
    else:
        return False



# Quest Name: Shadow Riddle
# Description: Answer a basic riddle about light and darkness.
def riddle_quest():

    print("I follow you in light but disappear in darkness.")
    answer = input("What am I? ")

    if answer.lower() == "shadow":
        return True
    else:
        return False



# Quest Name: Hidden Word
# Description: Find the hidden word from the first letters.
def hidden_word_quest():

    print("Silent")
    print("Ash")
    print("Voices")
    print("Eternal")

    answer = input("What word is hidden? ")

    if answer.lower() == "save":
        return True
    else:
        return False



# Quest Name: Demon Coin
# Description: Guess heads or tails against a weak demon.
def demon_coin_quest():

    choice = input("Choose heads or tails: ")

    demon = random.choice(["heads", "tails"])
    print("Demon chose:", demon)

    if choice.lower() == demon:
        return True
    else:
        return False



# Quest Name: Demon Weakness
# Description: Choose the correct weakness of demons.
def demon_weakness_quest():

    print("A Lesser Demon blocks your path.")
    print("What is most effective against demons?")
    print("1 - Mithril")
    print("2 - Water")
    print("3 - Fire")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        return True
    else:
        return False



# RUN GREEN SIDE QUEST

def run_green_side_quest():

    print("\nGREEN SIDE QUEST STARTED")

    quests = [
        math_quest,
        riddle_quest,
        hidden_word_quest,
        demon_coin_quest,
        demon_weakness_quest
    ]

    quest = random.choice(quests)
    result = quest()

    if result:
        print("\nSuccess! You gain a small reward.")
    else:
        print("\nYou failed. Minor damage taken.")



# TEST

run_green_side_quest()




