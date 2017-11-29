# Walkthrough¶
# Imagine that you work for a large retailer, writing software for its internal accounting system. You’ve been asked to write a function average_sales that can take a set of data representing daily sales at a given store, and calculate the average sales for each week represented by the data.

# The data is structured as follows:

# A single week of daily sales is a list with 7 entries, one for each day of the week (index 0 = Monday, index 6 = Sunday): [1512.30, 1555.72, 1989.77, 2101.33, 1884.45, 1333.33, 1456.23]

# You are given data for several weeks at once, collected into a list:

# sales = [[1512.30, 1555.72, 1989.77, 2101.33, 1884.45, 1333.33, 1456.23],
# [1215.340, 1565.99, 2989.34, 2301.77, 1234.81, 1923.44, 2282.39],
# ...]
# Therefore, sales is a list of lists. So here, sales[0] is a list of sales totals for each day of the first week, sales[1] a list of sales totals for each day of the second week, and so on. We will implement average_sales so that it returns a list of the averages for each week.

# So if sales is the list above and we call weekly_averages = average_sales(sales), then weekly_averages[0] is the average for week 0, and so on.

"""from test import testEqual

def average_sales(daily_sales):

    num_weeks = len(daily_sales)
    weekly_averages = [0 for i in range(num_weeks)]

    for week in range(0, num_weeks):

        # calculate the average for the given week
        week_sum = 0
        for day_total in daily_sales[week]:
            week_sum += day_total

        weekly_averages[week] = week_sum / len(daily_sales[week])

    return weekly_averages


sales = [[1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 2, 1, 1]]

testEqual(average_sales(sales), [1, 1])"""


import random
from test import testEqual

# The roll_dice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the list.
def roll_dice(num_dice, num_rolls):

    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]

    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
      for die in range(0, len(double_list[roll])):
          double_list[roll][die] = (int)(random.random()*6 + 1)

    return double_list


# This function takes a 2D list (which can be generated by roll_dice)
# and sums the value of all the dice in each row. It returns a 1
# dimensional list with the sum of each throw.
# Example:
# double_list: [[1, 5, 6],[2, 3, 1],[1, 3, 3]]
# sum_of_roll should return: [12, 6, 7]
def sum_of_roll(double_list):
    # Your code here


# Bonus function! Takes a 2D list and returns
# the number of times a person rolls Yahtzee (all dice have
# the same value). Hint: you may want to create a helper
# function that takes individual rows of the list.
def yahtzee(double_list):
    
    num_yahtzees = 0

    for roll in double_list:
        if roll_is_yahtzee(roll):
            num_yahtzees += 1
    
    return num_yahtzees

def roll_is_yahtzee(a_list):
    #[1, 5, 6]
    is_yahtzee = True
    first_die = a_list[0]

    for die in a_list:
        # If we still have a potential yahtzee, check the next die
        is_yahtzee = (is_yahtzee and (die == first_die))

    return is_yahtzee


# To play, yo'd do something like this
# dice = input("How many dice?")
# rolls = input("What is the number of rolls?")
# list = roll_dice(dice, rolls)
# print("Sum of roll:", sum_of_roll(list))

print("Testing sum_of_roll...")
testEqual(sum_of_roll([[4, 5, 2],[6,2,1],[4,4,4]]), [11, 9, 12])
testEqual(sum_of_roll([[3, 4, 6],[2,6,1],[3,4,3]]), [13, 9, 10])
print("Testing yahtzee...")
testEqual(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]), 1)
testEqual(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]), 0)