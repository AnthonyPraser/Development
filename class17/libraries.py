import math # importing math library
import statistics # solving the  median of the lists
import pandas as pd # work
from datetime import date 
import requests




'''
Example
Import the math library.
Take the radius of a circle as user input.
Then, compute the area of the circle using the math library.
'''
# Area of a circle = pi * radius * raidus

# try:
# radius = int(input("Please enter your radius: "))
# area_or_a_circle = math.pi * radius * radius
# print(f'area_or_a_circle {area_or_a_circle : .2f} ')
# except ValueError:







'''
Exercise
Lets make some magic happen with the statistics library.
'''


# Middle value in odd numbered list
# odd_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
# median_of_an_odd_list = statistics.median(odd_list) # this will solve the median for us 
# print(median_of_an_odd_list)

# Average of two middle values
# even_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
# median_of_an_even_list = statistics.median(even_list)
# print(median_of_an_even_list)




'''
Exercise
Lets make some magic happen with the pandas library.
'''

# Dictionary with my users
users = {
  "acct_num": ['abb', 'cde', 'ggh', 'sdf'],
  "name": ['jim', 'sarah', 'tanya', 'bob']
}

# Load into a dataframe
# df = pd.DataFrame(users)
# print(df)


# generate a csv
# df.to_csv('test.csv',index=False)


'''
Exercise
Lets make some magic happen with the date time library.
'''
# today = date
# print(today)
# print(f'Today is {today}')




'''
https://jsonplaceholder.typicode.com/
This website provides free api testing. Lets leverage python's request module to see if we can do a get request against this data
'''

my_response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(my_response.text)


















































