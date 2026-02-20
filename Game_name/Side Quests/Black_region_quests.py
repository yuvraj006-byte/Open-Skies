import random

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
# Accepting power always has a hidden cost.
import random

def black_void_bargain():

    print("\nA towering shadow stretches across the ruins.")
    print("Its voice echoes inside your mind:")
    print("'I can double your strength… but nothing is free.'\n")

    print("1 - Accept the power immediately")
    print("2 - Ask what the price is")
    print("3 - Refuse the offer")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        print("\nDark energy surges through your veins.")
        chance = random.randint(1, 100)

        if chance <= 40:
            print("You withstand the corruption. Your power increases.")
            return True
        else:
            print("The power overwhelms your mind. You lose control.")
            return False

    elif choice == "2":
        print("\nThe shadow smiles.")
        print("'Your memories… I will take one.'")

        print("You feel something slipping away…")
        print("But your body remains unharmed.")

        return True

    elif choice == "3":
        print("\nThe shadow fades.")
        print("You remain pure… but weaker than you could have been.")
        return False

    print("\nThe silence consumes you.")
    return False

def black_unseen_riddle():

    print("\nI have no blade, yet I can cut.")
    print("I have no hands, yet I can break.")
    print("The strongest warrior fears me.")
    print("What am I?")

    answer = input("Your answer: ")

    if answer.lower() == "fear":
        print("\nThe darkness acknowledges your insight.")
        return True

    print("\nYou fail to name the unseen force.")
    return False


def black_fragment_trial():

    print("\nA fallen demon drops spirit fragments.")
    print("Each fragment gives 6 power.")
    print("You collect 4 fragments.")
    print("But channeling them costs 5 power.")
    print("\nHow much power remains?")

    answer = input("Your answer: ")

    if answer == "19":
        print("\nThe fragments fuse perfectly into your core.")
        print("You feel darker… stronger.")
        return True

    print("\nThe fragments shatter in your hands.")
    print("Their power slips away into the void.")
    return False


def black_word_strength():

    print("\nSpeak a word of power.")
    print("It must be longer than 6 letters.")
    print("And contain at least 2 vowels (a, e, i, o, u).")

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

def black_hidden_number():

    secret = random.randint(10, 20)

    print("\nGuess the hidden number between 10 and 20.")
    guess = int(input("Your guess: "))

    if guess == secret:
        print("You guessed perfectly.")
        return True

    print("Wrong. The number was", secret)
    return False


# BLACK - Endurance Duel
# More complex duel system.
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


# BLACK - Element Alignment Puzzle
# Logical deduction.


# BLACK - Deep Riddle
# Abstract thinking.
def black_void_riddle():

    print("\nI am taken before you can see me.")
    print("I vanish the moment I am said.")
    print("What am I?")

    answer = input("Your answer: ")

    if answer.lower() == "silence":
        return True

    return False

def black_order_trial():

    print("\nFour statues stand in a line:")
    print("Warrior, Mage, Beast, King.")
    print("\nAn inscription reads:")
    print("'The Beast stands somewhere after the Mage.'")
    print("'The Warrior is not at either end.'")
    print("'The King stands at one of the ends.'")
    print("\nWho stands in the second position?")

    answer = input("Your answer: ")

    if answer.lower() == "warrior":
        print("\nThe statues grind as stone shifts into place.")
        return True

    print("\nNothing moves. The puzzle resets.")
    return False





# RUN BLACK SIDE QUEST