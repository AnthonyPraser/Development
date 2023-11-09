# Get input from user
user_email = input("What is your email? " )
# user_email = "anthonyprasertsinh@outlook.com"

# Sanitize with .strip()
user_email = user_email.strip()


# Test 1 - Check if it has "." at the third-to-last index 
# kind the figure this out 
test_1 = (user_email[-4] == ".")
print("Test 1: Check if it has '.': ",test_1)


# Test 2 - Check if it has exactly one "@" symbol, at the fifth-to-last index or earlier 
# had to look at notes to figure that out
test_2 = ("@" in user_email[0:-5])
print("Test 2: Check if it has one '@': ",test_2)


# Test 3 - Check if there is at least one character before the "@" symbol
# very hard for me had to look at notes 
stop_value = user_email.index('@')
test_3 = (len(user_email[0:stop_value]) >=1)
print("Test 3: Check if there is at least one character before the '@': ",test_3)

# Test 4 - Check if it doesn't have any spaces (doesn't contain " ")
# kind the got it maybe 
test_4 = user_email.count(" ") == 0
print("Test 4: Check if there is any spaces: ",test_4)


# If all these conditions are met, print True. Otherwise, print False
passed_failed = (test_1 and test_2 and test_3 and test_4)
print("Are all conditions met?: ",passed_failed)











