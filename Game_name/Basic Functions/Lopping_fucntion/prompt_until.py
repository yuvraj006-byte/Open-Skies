def prompt_until(task):
    retry_variable = "Do You Want To Continue (Y/N)?: "
    task() # Calls the function for the First time.

    while True:
        retry_input = input(retry_variable).strip().lower()

        if retry_input == "y":
            task() # Calling the function for lopping and continues the loop.
        
        elif retry_input == "n":
            print("Good Bye!\nSee You Soon.")
            break
        
        else:
            print("Invalid Input! Please Try Again!")
            # Continues the loop if Invalid Input
    return
prompt_until() # What ever Function you have defined than needs to be looped, call it inside here!

#Example:
import random
def roll_die():
    return print(random.randint(1,6))

def prompt_until(task):
    retry_variable = "Do You Want To Continue (Y/N)?: "
    task() # Calls the function for the First time.

    while True:
        retry_input = input(retry_variable).strip().lower()

        if retry_input == "y":
            task() # Calling the function for lopping and continues the loop.
        
        elif retry_input == "n":
            print("Good Bye!\nSee You Soon.")
            break
        
        else:
            print("Invalid Input! Please Try Again!")
            # Continues the loop if Invalid Input
    return
prompt_until(roll_die) # What ever Function you have defined than needs to be looped, call it inside here!