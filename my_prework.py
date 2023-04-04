# Question 1:
# Write a function to print "Hello_USERNAME!" USERNAME is the input of the function.

# def hello_name(user_name):
#     user_name = input("\nWhat is your username:")
#     return user_name

# print(hello_name(user_name=''))

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():
#     numbers = list(range(1,100,2))
#     print(numbers)

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.
# def max_num_in_list(a_list):
#     groceries = [1, 2, 3, 4, 5, 6, 7, 8, 100, 1000, 99, 86]
#     print(max(groceries))

# max_num_in_list(a_list='')

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type 
# (true/false).
a_year = True
def is_lead_year(a_year):
    if a_year % 4 == 0:
        a_year = True
        print(a_year)
    else:
        a_year = False
        print(a_year)

is_lead_year(1988)    

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
# def is_consecutive(a_list):
#     # Your code here
#     pass