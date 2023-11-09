'''
Lists
1. Accessing lists with indexing
2. Updating lists with indexing
3. Lists in a For Loop
4. Exercise - Loop through a list, remove dupes
5. List Methods
6. Exercise - List of Pets
7. Example - Removing Values

'''

'''
1. Accessing lists with indexing
'''

# Assign the value of earth to a variable using indexing

# planets = ['venus', 'mercury', 'mars', 'earth']

# my_planet = planets[3]

# print(my_planet)
# print(planets[3])





# Assign the value of strawberry to a variable using indexing

# ice_cream = ['chocolate', 'strawberry', 'vanilla']

# my_ice_cream = ice_cream[1]

# print(my_ice_cream)




# Assign the value of bike to a variable using indexing

# transportation = ['bus', 'car', 'bike']

# my_transportation = transportation[2]

# print(my_transportation)





# Assign the value of green to a variable using indexing

# colors = ['red', 'green', 'blue']

# my_colors = colors[1]

# print(my_colors)




# Assign the value of 2.91 to a variable using indexing

# mixed_data_types = [3, 2.91, 'yarn', ["hello", 'everyone']]
# my_value =mixed_data_types[1]
# print(my_value)








'''
2. Updating lists with indexing
'''

# Update the value of earth to a jupiter using indexing

# planets = ['venus', 'mercury', 'mars', 'earth']
# planets[3] = 'jupiter'
# print(planets)

# Update the value of strawberry to mint chocolate chip using indexing

# ice_cream = ['chocolate', 'strawberry', 'vanilla']
# ice_cream[1] = 'mint chocolate chip'
# print(ice_cream)

# Update the value of bike to motorcycle using indexing

# transportation = ['bus', 'car', 'bike']
# transportation[2] = 'motorcycle'
# print(transportation)

# Update the value of green to orange to a variable using indexing

# colors = ['red', 'green', 'blue']
# colors[1] = 'orange'
# print(colors)


# Update the value of 2.91 to elephant using indexing

# mixed_data_types = [3, 2.91, 'yarn']
# mixed_data_types[1] = 'elephant'
# print(mixed_data_types)

'''
3. Lists in a For Loop
'''

# Lets loop through and display the results

# my_nums = [1, 2, 3, 4, 5]
# for m in my_nums:
#     print(m)







'''
Create a for loop that goes through this list and prints each item in the list, along with its 
index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars

'''

# planets = ["mercury", "venus", "earth", "mars"]
# counter = -1

# for p in planets:
#     counter +=1
#     print(f'{counter}: {p}')



name = input("What is your name? ")

fname, lname, = name.split(' ')

print(f"Hello, {fname} {lname}")


'''
4. Exercise
Write some code that takes one list and creates a second list that has the type for each entry in 
the list. Hint: Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

'''

# # Original list
# data = ['fido', 'fido', 'caravan', 'caravan', 10, 10, False, 8.12, ['hello', 'everyone'], ['leg']]
#
# # We will first create a list with no duplicates
# no_dupes = []
#
# # This will be our filtered list that captures our data types
# filtered_list = []

'''
Remove Dupes
This for loop will start appending items to our no dupes list. As we loop through, we will not 
add any additional items into no dupes that already exist there
'''
# for d in data:
#     if d not in no_dupes:
#         no_dupes.append(d)
# print(no_dupes)

'''
Type for each entry
We will now take our no dupes list and loop through, capture the types and append them to our final
list
'''

# for e in no_dupes:
#     filtered_list.append(type(e))
# print(filtered_list)

'''
5. List methods
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''

# Let's append our favorite color to this list

# colors = ['red', 'green','blue']
# colors.append('orange')
# print(colors)

# Let's remove all the elements from the list

# colors.clear()
# print(colors)

# Let's copy this list

# animals = ['dog', 'cat', 'bird', 'fish']
# animals_copy = animals.copy()
# print(animals_copy)

# Let's count the occurrences of 7 in this list

# numbers = [1, 2, 3, 3, 7, 7, 7, 7]
# seven_count = numbers.count(7)
# print(seven_count)

# Let's count the occurrences of apple in this list

# fruits = ['apple', 'grapes', 'apple', 'apple']
# apple_count = fruits.count('apple')
# print(apple_count)

# Let's add elements to a list from another list with extend

# movies = ['Back to the Future', 'Big', 'Lion King']
# more_movies = ['Avengers', 'King Kong', 'The Equalizer']
# movies.extend(more_movies)
# print(movies)

# Let's return the index of Lion King

# my_index = movies.index('Lion King')
# print(my_index)

# Let's insert Shawshank Redemption as second item in our list

# movies.insert(2,'Shawshank Redemption')
# print(movies)

# Let's remove the first movie

# movies.pop(0)
# print(movies)

# Let's remove the first instance of Toyota
# cars = ['ford', 'nissan', 'toyota', 'toyota', 'chevy']
# cars.remove('toyota')
# print(cars)

# Let's reverse our list of cars

# cars.reverse()
# print(cars)

# Now, lets try to sort

# cars.sort()
# print(cars)

'''
6. Exercise - List of Pets

You want to make a list containing the types of pets that the user has. Keep prompting the user 
for a pet until they enter "stop". If it's a new pet, add it to the list. If the list already has 
that pet, don't add it.
'''

# pets = [] # this will maintain our pets
#
# while True: # we will utilize breaks and continue to control our loop
#     user_input = input("What type of pet do you have? ").lower() # prompting user, adding lower
#     # for uniform data and our stop test
#
#     if user_input == 'stop': # if user types stop, we are all done
#         break
#     elif user_input not in pets: # lets add our pet to our list and give feedback
#         pets.append(user_input)
#         print(f'We have just added {user_input} to our pet list')
#         print(pets)
#     elif user_input in pets:
#         print(f'{user_input} is already in our pets list')
#         print(pets)
#         continue
#
# print("Have a great day")

'''
7. Example - Removing Values
You have a list of numbers, but it contains multiple of the number 2. Remove the number 2 until 
it only appears in the list once.

'''

# remove_dupes = [1, 2, 3, 2, 2, 3, 4, 5, 6, 2, 2, 2, 2, 2, 1, 1, 5, 6, 5]
#
# for d in remove_dupes:
#     if d == 2:
#         remove_dupes.remove(2)
# print(remove_dupes)

'''
8. Exercise: Removing All Duplicates

You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
Hint: How would you expand our previous example, which removed duplicates of one value, to remove 
duplicates of all values?
Hint 2: You might want to make a copy of the original list to use as reference. 
You may want to use more than one loop.

'''

# original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# create a copy, good practice so we don't modify original string
states_backup = states.copy()

# this will capture our unique states
states_no_duplicates = []

# we will loop through states_backup, and append only the first occurence of each state into
# states no duplicates
# for s in states:
#     if s not in states_backup:
#         states_no_duplicates.append(s)
# print(states_no_duplicates)






































