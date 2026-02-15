import mysql.connector 

def sign_in_details():   

    user_name = input("Enter a User Name: ")
    pws1 = input("Enter a Password: ")
    pws2 = input("Confirm the Passowrd: ")
    
    return user_name, pws1, pws2


def get_query(user, password):

    connection = mysql.connector.connect(
        host = "localhost",
        user = "your_user_name",
        password = "your_password",
        database = "game_project", # The Databse! Currenty Yuvraj has the databse!
    )

    cursor = connection.cursor()
    sql = """
    INSERT INTO users(username, password_hash)
    VALUES(%s,%s);
    """

    cursor.execute((sql), (user, password,))
    result = cursor.fetchall()
    connection.commit()

    cursor.close()
    connection.close()
    
    return result

def acc_register():
    apple_pi_games= "Game Name"
    user_name, pws1, pws2 = sign_in_details()  

    if pws1 != pws2:
        print("The Passwords Do NOT Match!\nPlease Try Again!")
    else:
        get_query(user_name, pws1)
        print(f"Your Account has been Registered!\nThank you for joining {apple_pi_games} Community!")
        print("Good Luck on your journey. Have Fun!")
    
    return
acc_register()