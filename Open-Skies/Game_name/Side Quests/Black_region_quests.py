import random


# BLACK - Risk Trial
# You draw unstable energy from a Sanctuary core. Higher risk means higher chance of success… or failure.
def black_risk_trial():

    print("\nA fractured core pulses with unstable energy.")
    print("Low  - Light touch")
    print("Medium - Channel briefly")
    print("High - Absorb fully")

    choice = input("Choose risk (low / medium / high): ").lower()

    if choice == "low":
        chance = 40
    elif choice == "medium":
        chance = 60
    elif choice == "high":
        chance = 75
    else:
        return False

    roll = random.randint(1, 100)

    if roll <= chance:
        print("The energy obeys you.")
        return True

    print("The energy lashes back violently.")
    return False


# BLACK - Void Bargain
# A shadow offers power. Every choice carries consequence.
def black_void_bargain():

    print("\nA towering shadow stretches across the ruins.")
    print("'I can double your strength… but nothing is free.'\n")

    print("1 - Accept immediately")
    print("2 - Ask the price")
    print("3 - Refuse")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        chance = random.randint(1, 100)

        if chance <= 40:
            print("You withstand the corruption.")
            return True
        else:
            print("The power overwhelms you.")
            return False

    elif choice == "2":
        print("You learn the cost and survive the exchange.")
        return True

    elif choice == "3":
        print("You walk away weaker but unchanged.")
        return False

    return False


# BLACK - Unseen Riddle
# Solve the abstract riddle to proceed.
def black_unseen_riddle():

    print("\nI have no blade, yet I can cut.")
    print("I have no hands, yet I can break.")
    print("The strongest warrior fears me.")
    print("What am I?")

    answer = input("Your answer: ")

    if answer.lower() == "fear":
        print("The darkness acknowledges your insight.")
        return True

    print("You fail to name the unseen force.")
    return False


# BLACK - Fragment Trial
# Calculate remaining power after fragment fusion.
def black_fragment_trial():

    print("\nEach spirit fragment gives 6 power.")
    print("You collect 4 fragments.")
    print("Channeling costs 5 power.")
    print("How much remains?")

    answer = input("Your answer: ")

    if answer == "19":
        print("The fragments fuse into your core.")
        return True

    print("The fragments shatter.")
    return False


# BLACK - Word Strength
# Speak a powerful word meeting specific conditions.
def black_word_strength():

    print("\nSpeak a word of power.")
    print("Longer than 6 letters.")
    print("At least 2 vowels.")

    word = input("Your word: ").lower()

    vowel_count = 0

    if "a" in word:
        vowel_count += 1
    if "e" in word:
        vowel_count += 1
    if "i" in word:
        vowel_count += 1
    if "o" in word:
        vowel_count += 1
    if "u" in word:
        vowel_count += 1

    if len(word) > 6 and vowel_count >= 2:
        print("The word holds power.")
        return True

    print("Your word is too weak.")
    return False


# BLACK - Endurance Trial
# Survive three consecutive shadow strikes.
def black_endurance_trial():

    print("\nYou must survive 3 shadow strikes.")
    health = 30

    for i in range(3):
        damage = random.randint(8, 15)
        health -= damage
        print("Strike damage:", damage)

        if health <= 0:
            print("You collapse.")
            return False

    print("You endure the assault.")
    return True


# BLACK - Hidden Number
# Guess the hidden number between 10 and 20.
def black_hidden_number():

    secret = random.randint(10, 20)

    print("\nGuess the hidden number between 10 and 20.")
    guess = int(input("Your guess: "))

    if guess == secret:
        print("Perfect guess.")
        return True

    print("Wrong. The number was", secret)
    return False


# BLACK - Endurance Duel
# Win by beating the guardian’s strength by at least 3 points.
def black_endurance_duel():

    print("\nA powerful guardian stands before you.")
    print("Choose attack strength (15–30).")

    player = int(input("Enter your attack number: "))
    guardian = random.randint(20, 35)

    print("You roll:", player)
    print("Guardian rolls:", guardian)

    if player >= guardian + 3:
        return True

    return False


# BLACK - Void Riddle
# Solve the abstract silence riddle.
def black_void_riddle():

    print("\nI am taken before you can see me.")
    print("I vanish the moment I am said.")
    print("What am I?")

    answer = input("Your answer: ")

    if answer.lower() == "silence":
        return True

    return False


# BLACK - Order Trial
# Deduce the correct statue position.
def black_order_trial():

    print("\nFour statues stand in a line:")
    print("Warrior, Mage, Beast, King.")
    print("'The Beast stands after the Mage.'")
    print("'The Warrior is not at either end.'")
    print("'The King stands at one of the ends.'")
    print("Who stands in the second position?")

    answer = input("Your answer: ")

    if answer.lower() == "warrior":
        print("The statues shift.")
        return True

    print("The puzzle resets.")
    return False


# RUN BLACK SIDE QUEST
def run_black_side_quest():

    print("\nBLACK SIDE QUEST STARTED")

    quests = [
        black_risk_trial,
        black_void_bargain,
        black_unseen_riddle,
        black_fragment_trial,
        black_word_strength,
        black_endurance_trial,
        black_hidden_number,
        black_endurance_duel,
        black_void_riddle,
        black_order_trial
    ]

    quest = random.choice(quests)
    result = quest()

    if result:
        print("\nYou endure the darkness. High reward granted.")
    else:
        print("\nYou fail. Severe damage taken.")


if __name__ == "__main__":
    run_black_side_quest()
