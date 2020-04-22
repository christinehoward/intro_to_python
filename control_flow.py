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

# Instructor Solution
#  number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num
# print the factorial of number
print(product)
# this solution is simple yet effective and in this case better suited for the problem:
# with a for loop, we do not need to tell the loop when to stop, as it will loop through the list it has been given, and then stop.


# Quiz: Count By
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.
# Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?
# After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num.

start_num = #provide some start number
end_num = #provide some end number that you stop when you hit
count_by = #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
# check against end_num

start_num = 1
end_num = 100
count_by = 2

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)


# Quiz: Count By Check
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.
# Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." Otherwise, set result to the value of break_num.

end_num = 100
count_by = 2
start_num = 1 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

break_num = start_num
while break_num < end_num:
    result = [break_num += count_by]
else:
    result = ["Oops! Looks like your start value is greater than the end value. Please try again."]

print(result)

end_num = 100
count_by = 2
start_num = 566 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

break_num = start_num
while break_num < end_num:
    break_num += count_by
if start_num > end_num:
    print("Oops! Looks like your start value is greater than the end value. Please try again.")
else:
    print(break_num)


# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 100
num = 0
while (num + 1)**2 < limit:
    num += 1
nearest_square = num**2
print(nearest_square)

# OUR SOLUTION
# Question: What type of loop should we use?
# You need to write a loop that takes the numbers in a given list named num_list:
# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

# Would you use a while or a for loop to write this code?

# We have provided our solution on the next page. Feel free to use the coding playground below to test your code.

## Please use this space to test and run your code
# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312,
# 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_numbers = []
for number in num_list:
    if number % 2 != 0:
        odd_numbers.append(number)
        
finalResult = []

# # wrap a list in enumerate in a for loop, and get access to the index

for i, item in enumerate(odd_numbers):
    if(i < 5):
        finalResult.append(item)

print(sum(finalResult))


# This solution is not the most performant (fastest), but is simple.
# First I do a loop in the list to get my odd numbers, store them in a 2nd list.
# Then I do another loop in this 2nd list result, and get only the first five odd numbers 
# # i stands for index
# # then I just print the sum of the list with sum(finalResult))


# Instructor solution
um_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))


# break statement: terminates a for or while loop

manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42)...]
# tuple
weight = 0
items = []
for cargo in manifest:
    print("current weight: {}".format(weight))
        if weight >= 100:
            print("breaking loop now!")
            break
        else:
            print(" adding {} ({})".format(cargo[0], cargo[1]))
            items.append(cargo[0])
            weight += cargo[1]

# continue: terminates only one iteration of a for or while loop


# skips an iteration when adding an item would exceed the limit
# # # breaks the loop if weight is exactly the value of the limit
# print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


# Quiz: Break the String
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = []

# MY RESULT
# write your loop here
length = 0
total_length = 140

for headline in headlines:
    print("current headline: {}".format(headline))
    if len(headline) >= total_length:
        # print(" breaking from loop")
        break
    elif length + len(headline) > total_length:
        # print(" skipping {}".format(headline))
        continue
    else: 
        # print(" adding {}". format(headline))
        news_ticker.append(headline)
        length += len(headline)

print(len(" ".join(news_ticker)))
print(" ".join(news_ticker))

# INSTRUCTOR RESULT

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


# Instructor Solution for Coding Quiz: Check for Prime Numbers
# Question: Write code to check if the numbers provided in the list check_prime are prime numbers. For each number, if the number is prime, the code should print that the number is a prime number. If the number is NOT a prime number, it should print that the number is not a prime number, and also print a factor of that number besides 1 and the number itself.

check_prime = [26, 39, 51, 53, 57, 79, 85]

# loop through each number in the check_prime list.
for num in check_prime:


# Create a "search-for-factors" loop beginning at 2, and continuing up to the (number-1)
    for i in range(2, num):

# Use a conditional statement with the modulo operator to check if our number when divided by the possible factor yields any remainder besides 0.
# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
# If we ever find one factor, we can declare that the number is not prime, and state the factor we found. 
# Then we can break out of the loop for that number.

# If we get up to the (number - 1) and haven't broken out of the loop, then we can declare that the number is prime.
# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))


# ZIP AND ENUMERATE

# zip: returns an iterator that combines multiple iterables into one sequence of tuples
    ## each tuple contains the elements in that position from all the iterables

items = ['bananas', 'mattresses', 'dog kennels']
weights = [15, 34, 42]
for item, weight in zip(items, weights):
    print(item, weight)

for cargo in zip(items, weights):
    print(cargo[0], cargo[1])

# can also unzip a list using an asterisk
items, weights = zip(*manifest)
print(items)
print(weights)

# enumerate: returns these tuples containing the indexes and values of a list in an iterable for you

# instead of:
for i, item in zip(range(len(items)), items):
    print(i, item)

for i, item in enumerate(items):
    print(i, item)
    

# Quiz: Zip Coordinates
# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. 
# Each string should be formatted as label: x, y, z. 
# For example, the string for the first coordinate should be F: 23, 677, 4

# Instructor Solution: Zip Coordinates

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
# first we zip all 4 lists together, then we append the matching values from the 4 lists (ex: F, 23, 677, 4) to the new points list.
for point in points:
    print(point)
# we then want to print each point (set of 4 values) separately to see all sets
Output:
F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1
# Notice here, the tuple was unpacked using * in the format method. 
# This can help make your code cleaner!


# Quiz: Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values.

# Instructor Solution: Zip Lists to a Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Output: The order of elements in this output may vary since dictionaries are unordered.
{'Lily': 66, 'Barney': 72, 'Marshall': 76, 'Ted': 72, 'Robin': 68}


# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)
print(names)
print(heights)

# output: 
# ('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
# (72, 68, 72, 66, 76)


# Quiz: Transpose with Zip
# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. 
# There's actually a cool trick for this! 
# Feel free to look at the solutions if you can't figure it out.

# Instructor Solution: Transpose with Zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
# Output:
((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
# This is a useful trick to know!

# Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. 
# For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

# My Solution: with new list
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
member_heights = []
# write your for loop here

for member_height in zip(cast, heights):
    member_heights.append("{} {}".format(*member_height))

for i, member_height in enumerate(member_heights):
    print(i, member_height)

# Instructor Solution
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

# i = index, this index needs to match in all 3 places
# for a certain index (starting with 0 and looping through list) and character in the enumerate of cast:
# the cast index = the character at this index + " " + the height at this same index (expressed as a string)

print(cast)
# output: ['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']


# LIST COMPREHENSIONS

# instead of:
cities = ['new york city', 'mountain view'...]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

# this:
cities = ['new york city', 'mountain view'...]
capitalized_cities = [city.title() for city in cities]

# example: instead of
squares = []
for x in range (9):
    squares.append(x**2)
print(squares)

# list comprehension:
squares = [x**2 for x in range(9)]
print(squares)

# result for both options:
[0, 1, 4, 9, 16, 25...]

# can also add conditionals:
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)
# here, x**2 is only evaluated when x is even

# when adding else:
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)


# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split(' ')[0].lower() for name in names]
print(first_names)


# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [x*3 for x in range(1, 21)]
print(multiples_3)


# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)


# Practice Questions
# Question 1.
# A. Create a dictionary that includes the count of Oscar nominations for each director in the nominations list.

nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

# ### 1A: Create dictionary with the count of Oscar nominations for each director 
nom_count_dict = {}

for year, directors in nominated.items():
    for director in directors:
        if director in nom_count_dict:
            nom_count_dict[director] += 1
        else:
            nom_count_dict[director] = 1
print(nom_count_dict)

# B. Provide a dictionary with the count of Oscar wins for each director in the winners list.

nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

win_count_dict = {}

for year, directors in winners.items():
    for director in directors:
        if director in win_count_dict:
            win_count_dict[director] += 1
        else:
            win_count_dict[director] = 1
print(win_count_dict)


# Question 2:
# Provide a list with the name(s) of the director(s) with the most Oscar wins. We are asking for a list because there could be more than 1 director tied for the most Oscar wins.

winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}


### For Question 2: Please provide a list with the name(s) of the director(s) with 
### the most Oscar wins. The list can hold the names of multiple directors,
### since there can be more than 1 director tied with the most Oscar wins.
win_count_dict = {}
most_win_director = []
# Add your code here

for year, directors in winners.items():
    for director in directors:
        if director in win_count_dict:
            win_count_dict[director] += 1
        else:
            win_count_dict[director] = 1
            
highest_number = 0            
            
for director, number_wins in win_count_dict.items():
    if number_wins > highest_number:
        highest_number = number_wins

for director, number_wins in win_count_dict.items():
    if number_wins == highest_number:
        most_win_director.append(director)
print(most_win_director)


# Question 2
# Provide a list with the name(s) of the director(s) with the most Oscar wins.
# Here's the logic for my solution:
# To address this question, I will need to first create a dictionary with the number of wins by each winning director. For that I can use the code we wrote for Question 1b above.

#FIRST PART OF SOLUTION
win_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1

# This win_count_dict dictionary provides a dictionary with the win count for the directors. We will need this to then identify which key (here, director name) has the highest value (here, win count).
# To perform this task, we use a variable highest_count to keep track of the highest count of wins.
# We iterate through the dictionary to see if the value for a key (i.e., wins for a director) is more than the highest count.
# If it is, we replace that value as the highest_count.
# Plus we add that key (here, director name) to our list tracking the most_win_director.
# Every time we come upon a value higher than the current highest_count, we replace highest_count with the new higher value, empty the most_win_director and replace it with the new key (i.e., director's name).

#ALTERNATIVE SECOND PART OF SOLUTION
highest_count = max(win_count_dict.values())

most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]