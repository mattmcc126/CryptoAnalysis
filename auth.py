# imports



# Current starting code for authentification to retrieve data about the users account

live = True # run loop until input

while (True):
    print("\n\nHello! Enter your username and password to confirm account information... \n")

    try: 
        username_input = input("Username: ")
        username = str(username_input)
        
        password_input = input("Password: ")
        password = str(password_input)

        # Atempt to login with CbAPI, if successful...
            # live = False; 
        if username and password:
            break

        # If not successful...
    # except Login_Exception as e:
        # print("error on login... check username and password")
    
        # catch any other error
    except Exception as e:
        print(f"Error found inside program: {e}")

        # For planning/testing purposes ---------------------------- Remove later
    finally:
        print(f"\n\nusername is: {username}\npassword is: {password}\n")

# to do / implement 
print("data about user for them to see will now be printed.")

    
