# CONDITIONAL STATEMENTS

# if statement:
if phone_balance < 5:
    ## condition to be checked, is checked with boolean expression, true or false?
    phone_balance += 10
    bank_balance -=10
    ## to be executed only if the condition is true

# else:
if n % 2 == 0:
    print("Number " + str(n) + " is even.")
else: 
    print("Number " + str(n) + " is odd.")

# elif: else if (for multiple conditions)
if season == "spring":
    print("plant")
elif season == "summer":
    print("water")
elif season == "fall"
    print("harvest")
elif season == "winter"
    print("stay indoors")
else:
    print("unrecognized season")

## note: = is an assignment operator that assigns value on the left to the name on the right
      ## == comparison operator that evaluates whether objects on both sides are equal
## note: indentation indicated to python what is inside/outside if statement

# #First Example - try changing the value of phone_balance
phone_balance = 9
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)
# output: 
# 19 
# 40

# # # #Second Example - try changing the value of number

number = 140
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")
# output: Number 140 is even.

# #Third Example - try to change the value of age

age = 46
# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
# # These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50
# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)
# output: Somebody who is 46 years old will pay $2.5 to ride the bus.


# Practice: Which Prize
# Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin
# All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

# In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Oh dear, no prize this time."

points = 174  # use this input to make your submission

# write your if statement here
small_prize_upto = 50
no_prize_upto = 150
med_prize_upto = 180
big_prize_upto = 200

if points <= small_prize_upto :
    print("Congratulations! You won a wooden rabbit!")
elif points <= no_prize_upto :
    print("Oh dear, no prize this time.")
elif points <= med_prize_upto :
    print("Congratulations! You won a wafer-thin mint!")
elif points <= big_prize_upto :
    print("Congratulations! You won a penguin!")
else:
    print("Oh dear, no prize this time.")

# OR

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"


# Quiz: Guess My Number
# You decide you want to play a game where you are hiding a number from someone. Store this number in a variable called 'answer'. Another user provides a number called 'guess'. By comparing guess to answer, you inform the user if their guess is too high or too low.
# Fill in the conditionals below to inform the user about how their guess compares to the answer.

answer = 78
guess = 78

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
else:
    result = "Nice!  Your guess matched the answer!"

print(result)
# Nice!  Your guess matched the answer


# Quiz: Tax Purchase
# Depending on where an individual is from we need to tax them appropriately. 
# The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. 
# Use this information to take the amount of a purchase and the corresponding state to assure that they are taxed by the right amount.

state = "MN"
purchase_amount = 100

state == "CA", "MN", "NY"

if state == "CA":
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY":
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


# COMPLEX BOOLEAN EXPRESSIONS

weight = 55
height = 164

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")
# output: BMI is considered 'normal'

if is_raining and is_sunny:
    print("Is there a rainbow?")
# both conditions need to be met here in order for result to be true
# if either condition is false, then the whole line will evaluate as false

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
# we want to send an email to customers who have not unsubscribed from emails AND
# whose location is either USA or CAN


# TRUTH VALUE TESTING
## by default, value will be considered true unless specified false


# Quiz: Using Truth Values of Objects

# You will use a new variable prize to store a prize name if one was won, and then use the truth value of this variable to compose the result message. This will involve two if statements.
# 1st conditional statement: update prize to the correct prize name based on points.
# 2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.
# If prize is None, result should be set to "Oh dear, no prize this time."
# If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize). This will avoid having the multiple result assignments for different prizes.
# At the beginning of your code, set prize to None, as the default value.

points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else: 
    result = "Oh dear, no prize this time."

print(result)
# output: Congratulations! You won a wafer-thin mint!


# LOOPS
## allow us to repeat blocks of code
## 2 kinds: for loops/while loops
## iterable: object that can return 1 of its elements at a time

# FOR LOOPS
cities = ['new york city', 'mountain view'...]
for city in cities:
    print(city.title())
# output: New York City, Mountain View
    ## for indicates this is a for loop
    ## cities is an iterable
    ## city is the loop's iteration variable: 1st iteration = new york city, 2nd = mountain view...

cities = ['new york city', 'mountain view'...]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
# this for loop goes through each city and capitalizes it for the new list

# modifying lists
    ## range(start, stop, step) - arguments must be integers
        ## start = first number, stop = one above the last number, step = range (difference in numbers between the sequence)
        ## if unspecified, start defaults to 0 and step to 1
    print(list(range(4)))
    # output: [0, 1, 2, 3]
    print(list(range(2, 6)))
    # output: [2, 3, 4, 5]
    print(list(range(1, 10, 2)))
    # output: [1, 3, 5, 7, 9]
cities = ['new york city', 'mountain view'...]
for index in range(len(cities)): # len(cities) = 4 [0, 1, 2, 3]
    cities[index] = cities[index].title()
# first iteration (ny city) will have index 0
# function will run, find 0 index value, capitalize it, and stick it back in place in original list
# output: ['New York City', 'Mountain View']

# Practice: Quick Brown Fox
# Use a for loop to take a list and print each element of the list in its own line.
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
    print(word)

# Practice: Multiples of 5
# Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
# This should output:
# 5
# 10
# 15
# 20
# 25
# 30
for i in range(5, 31, 5):
    print(i)

# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# should create the list:
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    usernames.append(name.replace(' ', '_').lower())
print(usernames)

# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. 
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)):
    usernames[index] = usernames[index].replace(' ', '_').lower()
print(usernames)
# result: ['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']


# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
# Output: 2


# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.
# You can assume that the list of strings will not contain empty strings.

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
# Output:
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>

# steps:
#     set html_str equal to (<ul>), because this is what we want at the start of the result
#     add \n for a line break after this
#     create a for loop, which will look at each item in the items list
#     then set html_str to where it will add "<li>{}</li>\n" after <ul>, and loop through using format
#     this will then add <li>{}</li>\n around each item (first string, etc.) using format
#     then add html_str += "</ul>" at the end, but reducing indent, so that this is only added after the loops have been completed (at the end of result)
#     then print html_str



# Building Dictionaries

# Method 1: Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

# Method 2: Using the get method
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
      }

# for key in cast:
#     print(cast)
    
for actor, character in cast.items():
    print("Actor: {}    Role: {}".format(actor, character))

# Fruit Basket - Task 1
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result

for item, total in basket_items.items():
    if item in fruits:
        result += total
print("There are {} fruits in the basket.".format(result))
# output: There are 23 fruits in the basket.

# Quiz: Fruit Basket - Task 3
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
#if the key is in the list of fruits, add to fruit_count.
#if the key is not in the list, then add to the not_fruit_count

for item, total in basket_items.items():
    if item in fruits:
        fruit_count += total
    else:
        not_fruit_count += total
print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))
# output: The number of fruits is 23.  There are 11 objects that are not fruits.


# WHILE LOOPS

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand) <= 17: # checking if the sum of the hand is <= 17
    # sum of an empty list = 0, 0 < 17.
    hand.append(card_deck.pop()) # popping last element from card_deck and appending to the hand list
print(hand)
# .pop() is the opposite of append for a list: removes the last element from a list and returns it
# if while sum(hand) <= 17: is True, then the loops body will be executed
# each time the loops body runs, the condition is evaluated again
# this process of checking the condition and then running the loop continues until the expression is false

print(hand) # result:
# 10
# 18
# [10, 8]
# this is where the value is large enough that the condition becomes false


# Practice: Factorials with While Loops
# Find the factorial of a number using a while loop.
# A factorial of a whole number is that number multiplied by every whole number between itself and 1. For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.
# We can write a while loop to take any given number and figure out what its factorial is.
# Example: If number is 6, your code should compute and print the product, 720.

# Our Solutions:

# number to find the factorial of
number = 6
# start with our product equal to one
result_factorial = 1
# track the current number being multiplied
current = 1

# write your while loop here
numbers = list(range(current, number + 1))
while len(numbers) > 0:
    product *= numbers.pop()
print(product)

# show notes with print statements:
numbers = list(range(current, number + 1))
while len(numbers) > 0:
    print('starting point each loop', result_factorial)
    print('values in the list', numbers)
    print('number of values in list', len(numbers))
    print('000000000000000000000')
        result_factorial *= numbers.pop()

# our other solution:
number = 4
result_factorial = 1
current = 1

while number > 0:
    result_factorial *= number
    number -= 1
print(result_factorial)

# Instructor Solution

number = 4
product = 1
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

# to check each step:
# number to find the factorial of
number = 3

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here

while current <= number:
    print('number:', number)
    print('product:', product)
    print('current:', current)
    product *= current
    print('product*current:', product)
    current += 1
    print('new current:', current)
    print('---------------------------------------------------------------')

# Practice: Factorials with For Loops
# Now use a for loop to find the factorial!

# My Solution
# number to find the factorial of
number = 0  
# start with our product equal to one
product = 1
# write your for loop here
numbers = list(range(1, number + 1))
for number in numbers:
    product *= number
    number -= 1
# print the factorial of number
print(product)