import random

def probabality(items, weights):
    if len(items) != len(weights): # For debugging and making future proof.
        raise ValueError("Lists must be same length")    

    total_fav = sum(weights) # This is the total Favorabilty of the items.
    rand_chance = random.uniform(0, total_fav) 

    upto = 0 # Upto is the sum of weight so far.
    for item, weight in zip(items, weights):
        if upto + weight >= rand_chance:
            return item
        upto += weight 

weights = [] #This would contain the weightage of the items, you can call it favorability.
items = [] # Here you would add the items you want to randomize.

# Note that the items idenx should be = to the weights index.

items_prob = probabality(items, weights) #This contiains the list and weight of things you want to randomize
print(items_prob) # The Word items is subject to change in this function calling ONLY, in accordance to the main function.

# For Testing the Probability Assignment.
# results = {"A": 0, "B": 0, "C": 0}

# for _ in range(100000):
#     test = probabality(items, weights)
#     results[test] += 1

# print(results)