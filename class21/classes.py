from datetime import datetime

'''
Classes
'''


class Point2d:
    pass

class Date:

    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def is_leap_year(self):
         pass



class Point2d:

    ''' This docstring can be 
    displayed as well'''

    # constructor with __init__
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Magic methods
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
         return Point2d(self.x - other.x, self.y - other.y)
    
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # Accessor Methods - returns an attribute to the user
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y




    # Mutator Methods - lets the user change the attribute
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


        


my_first_point = Point2d(10, 7) # class object or instance created
my_second_point = Point2d(11, 10)
my_fifth_point = Point2d(50, 100)

# Printing after adding __str__ magic method
print(my_first_point)
print(my_second_point)

# Equality __eq__

# print(my_first_point == my_second_point)

# Addition __add__
# my_third_point = my_first_point + my_second_point
# print(my_third_point)

# Subtraction __sub__
# my_fourth_point = my_first_point - my_second_point
# print(my_fourth_point)

# Less than __lt__
# print(my_first_point < my_second_point)

# Aceessor method
# print(my_first_point.get_x())
# print(my_second_point.get_x())
# print(my_fifth_point.get_x())

# print(my_first_point.get_y())
# print(my_second_point.get_y())
# print(my_fifth_point.get_y())

# Mutator method
# print(my_fifth_point)
# my_fifth_point.set_x(120) # mutator method changes x
# print(my_fifth_point)

# my_fifth_point.set_y(200)
# print(my_fifth_point)

# Doc String __doc__
# print(Point2d.__doc__)

    



































































