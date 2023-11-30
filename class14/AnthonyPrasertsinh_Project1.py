# How should I start? Telling the user the username and password requirments

# username_requirments = "Username Requirements: It must start with a lowercase letter and only contain letters, numbers, underscores, and not be in a list of taken usernames."
# taken_usernames = ['admin', 'admin123', 'root']
# print(username_requirments)

# password_requirments = "Password Requirements: At least 8 characters long, contains at least one uppercase letter, contains at least one lowercase letter, contains at least one digit, contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, and doesn't contain any spaces."
# # print(password_requirments)


# Trying to figure out the username requirments part

# user_input_username = input("What is your username: ")

# start_lowercase_letter = len(user_input_username[0]) == user_input_username.isalpha() and user_input_username.islower()

# contain_letters = (user_input_username.isalpha())

# contain_numbers = (user_input_username.isdigit())

# contain_underscores = (user_input_username == "_")

# taken_usernames = ['admin', 'admin123', 'root']

# username requirments in a list

# user_requirment_list = [start_lowercase_letter, contain_letters, contain_numbers, contain_underscores,]


# The user must be continuously prompted for input

# user_input_username = input()
# user_input_password = input()


# start_lowercase_letter = len(user_input_username[0]) == user_input_username.isalpha() and user_input_username.islower()
# contain_numbers = (user_input_username.isdigit())
# contain_underscores = (user_input_username == "_")
# taken_usernames = ['admin', 'admin123', 'root']
# contain_letters = (user_input_username.isalpha())

# taken_usernames = ['judith', 'robin', 'mohammad']

# while True:
#     # get the inputs
#     username = input('what is your first name ')
#     # password = input("what is your password ")
#     print(username)
#     # print(password)
    
  

#     # do your username testing




    # do your password testing

    








# user_input_username = input("Username: ")
# user_input_password = input("Password: ")
# taken_usernames = ['admin', 'admin123', 'root']

import re



while True:

    user_input_username = input("Username: ")

    start_uppercase = user_input_username[0]

    if start_uppercase.isupper():
        print("Invalid username: It must start with a lowercase letter")


        

    taken_usernames = ['admin', 'admin123', 'root']

    if user_input_username in taken_usernames:
        print("Username taken")

        continue

    

    



    

    

        
   
    
    
    

          




        
    
   


    
   
        


 

   




 

        
   
  
        

   
        
    
    
    

        
    


   
        
        
        
        
        
        












  
        
        

    
    
    

    
    












































