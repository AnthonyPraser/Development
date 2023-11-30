# How should I start? Telling the user the username and password requirments

# username_requirments = "Username Requirements: It must start with a lowercase letter and only contain letters, numbers, underscores, and not be in a list of taken usernames."
# print(username_requirments)

# password_requirments = "Password Requirements: At least 8 characters long, contains at least one uppercase letter, contains at least one lowercase letter, contains at least one digit, contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, and doesn't contain any spaces."
# # print(password_requirments)



# The user must be continuously prompted for input


import re



while True:
# Username requirments 
# It must start with a lowercase letter

    user_input_username = input("Username: ")

    start_uppercase = user_input_username[0]

    if start_uppercase.isupper():
        print("Invalid username: It must start with a lowercase letter")


        
# Not be in a list of taken usernames

    taken_usernames = ['admin', 'admin123', 'root']

    if user_input_username in taken_usernames:
        print("Username taken")


# Must not contain any special characters 

    special_characters = ['@', '!', '#', '$', '%', '^', '&', '*', '()', '<>', '?', '/','|','{', '}', '~', ':', '[]' ] 
    c = 0

    for i in range(len(user_input_username)):

        if user_input_username[i] in special_characters: # checking if any special character is present

            c += 1  # if special character found then add 1 to the c

    if c:
        print("Invalid username: Special character present")

    
# Password requirments 

    user_input_password = input("Password: ")

    # At least 8 character long
    eight_character_long = len(user_input_password)

    if eight_character_long < 8:
        print("Invalid password: Needs to be at least 8 characters long")

# contains at least one uppercase letter 

# using regex to check for any element to be uppercase

    upper_password = bool(re.match(r'\w*[A-Z]\w*', user_input_password))

    print(f"Does contain uppercase letter: {upper_password}")

# contains at least one lowercase letter

    lower_password = bool(re.match(r'\w*[a-z]\w*', user_input_password))

    print(f"Does contain lowercase letter: {lower_password}")

# contains at least one digit

# Using regex to check if there is at least one digit 
 
    digit_password = bool(re.search(r'\d', user_input_password))

    print(f"Does contain a digit: {digit_password}")

# contains at least one of these characters: !, ?, @, #, $, ^, &, *, _ , -

# Using a for loop to find at least one special character from that list

    special_characters_2 = ['!', '?', '@', '#', '$', '^', '&', '*', '_', '-']

    c_2 = 0

    for i in range(len(user_input_password)):

        if user_input_password[i] in special_characters_2:
            c_2 += 1

    if c_2:
        print("Does have at least one special character: True")
    else:
        print("Invalid password: Need at least one special character")

# Doesn't contain any spaces

# Using regex to check if there is any spaces 

    contain_spaces_password = bool(re.search(r"\s", user_input_password))

    print(f"Does password contain spaces: {contain_spaces_password}")

    break

print("Sign up successful")

# Logging in

user_sign_in_username = input("Log in - Username:  ")
user_sign_in_password = input("Log in - Password:  ")

if user_input_username == user_sign_in_username and user_input_password == user_sign_in_password:

    print("login successful")

else:
    print("Incorrect username or password")


    

  


    




    

        

    

    



    

    

        
   
    
    
    

          




        
    
   


    
   
        


 

   




 

        
   
  
        

   
        
    
    
    

        
    


   
        
        
        
        
        
        












  
        
        

    
    
    

    
    












































