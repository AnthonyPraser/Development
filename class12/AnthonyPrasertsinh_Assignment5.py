'''
You are given a 2D list representing a table of data with rows and columns. Write a Python program to calculate the sum and average of each column in the table.
For example, if this is your list:
data = [[45,56,89],[67,34,78],[23,67,34]]
This would be your output:
Column 1: Sum = 135, Average = 45.0
Column 2: Sum = 157, Average = 52.33
Column 3: Sum = 201, Average = 67.0
Hint: Make a list to store the sums, and a list to store the averages.

'''
# The list

data = [
    [45,56,89],
    [67,34,78],
    [23,67,34]
    ]


# Making a list to store the columns

column_1 = [data[0][0], data[1][0], data[2][0]]

column_2 = [data[0][1], data[1][1], data[2][1]]

column_3 = [data[0][2], data[1][2], data[2][2]]

# The sums and averages on all columns

sum_1 = sum(column_1)
avg_1 = sum_1 / 3
print(f'Column 1: Sum = {sum_1}, Average = {avg_1}')

sum_2 = sum(column_2)
avg_2 = round(sum_2 / 3, 2)
print(f'Column 2: Sum = {sum_2}, Average = {avg_2}')

sum_3 = sum(column_3)
avg_3 = sum_3 / 3
print(f'Column 3: Sum = {sum_3}, Average = {avg_3}')


# Not sure if I did this right 


            
            

    

    
    

   






































