# Quiz: Population Density Function
# Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.

def population_density (population, land_area):
    return population / land_area
    
# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))
# result: expected result: 10, actual result: 10.0
test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
# result: expected result: 7123.6902801, actual result: 7123.690280065897


# Quiz: readable_timedelta
# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
# For example, calling the function and printing the result like this:

# Instructor Solution: readable_timedelta
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


# LAMDA EXPRESSION


