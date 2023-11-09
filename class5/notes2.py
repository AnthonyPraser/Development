# Box around a string

# Get the user input
# user_input = input("What is your word? ")

# # Top and Bottom of box
# top_or_bottom = ((len(user_input) * '*') + '**')

# # Output
# print(top_or_bottom)
# print('*' + user_input + '*')
# print(top_or_bottom)

# Strings are Immutable

# first_name = 'ANTHONY'

# # apply method
# first_name = first_name.lower()

# print(first_name)

# my_string = "hello"

# my_string.upper()
# print(my_string)

# my_string = my_string.upper()
# print(my_string)

# Indexing
# mystr = "hello"
# print(mystr[0])
# print(mystr[4])
# print(mystr[len(mystr)-1])

# animal = 'kangaroo'

# print(animal[4])



# 1 - Get Input from the user
user_email = input("What is your email? ")

# 2 - sanitize with .strip()
user_email = user_email.strip()
# user_email = 'anthonyprasertsinh@outlook.com'

# 3 - Test 1 - '.' before top level domain (com, org, edu)
test_1 = (user_email[-4] == '.')
print("Test 1: Check for '.' before top level domain:",test_1)

# 4 - Test 2 - One '@' symbol at the fifth to last index or earlier
test_2 = ('@' in user_email[0:-5])
print("Test 2: Check for one '@' symbol before your '.' and top level domain:",test_2)

# 5 - Test 3 - At least 1 character before the "@" symbol (email can't start with '@')
stop_value = user_email.index('@') # index position of my @ symbol
test_3 = (len(user_email[0:stop_value]) >=1)
print("Test 3: At least 1 character before the @ symbol:", test_3)

# 6 - Test 4 - No spaces within the string itself
test_4 = user_email.count(' ') == 0
print("Test 4: Check for white space within the email address:", test_4)


# 7 - Confirm with boolean statements that all test either passed or failed 
passed_or_failed = (test_1 and test_2 and test_3 and test_4)
print("Did everything passed? ",passed_or_failed)















