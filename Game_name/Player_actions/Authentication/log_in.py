import mysql.connector 

def sign_in_details():   

    user_name = input("Enter a User Name: ")
    pws = input("Enter a Password: ")
    
    return user_name, pws

def get_query(user, password):

    connection = mysql.connector.connect(
        host = "localhost",
        user = "your_user_name",
        password = "your_password",
        database = "game_project", # The Databse! Currenty Yuvraj has the databse!
    )

    cursor = connection.cursor()
    sql = """
    SELECT username, password_hash FROM users
    where username = %s and
    password_hash = %s;
    """

    cursor.execute((sql), (user, password,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return result

def acc_register():
    user_name, pws = sign_in_details()  

    if get_query(user_name, pws):
        print(f"Welcome Back {user_name}!")
    else:
        print(f"{user_name} does NOT exit in our system!\nPlease Try Again!")
         
    
    return
acc_register()