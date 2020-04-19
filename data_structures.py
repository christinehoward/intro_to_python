# LIST AND MEMBERSHIP OPERATORS

# list: data type for mutable ordered sequences of elements
months = ['January', 'February', 'March'] # and so on
    ## lists hold data in []
print(months[0])
print(months[1])
# results:
    ## January
    ## March
    ## can look up values in a list as they are ordered [=index]
print(months[-1])
# result: December
    ## indexing from the end of the list


#List slicing

months = ['January', 'February'...'November', 'December']
q3 = months [6:9]
print(q3)
# result:['July', 'August', 'September']
# upper bound = exclusive (6), while lower bound = inclusive (9)

months = ['January', 'February'...'November', 'December']
first_half = months[:6]
print(first_half)
second_half = months[6:]
print(second_half)

greeting = "Hello World"
months = ['January', 'February'...'November', 'December']
print(len(greeting)), len(months)
# result: 11 (characters in "Hello World") 12 (number of months)

greeting = "Hello there"
months = ['January', 'February'...'November', 'December']
print(greeting[6:9], months[6:9])
# result: 'the' ['July', 'August', 'September']

# Membership operators

# in: evaluates if object on left side is included in object on right side
# not in: evaluates if object on left side is not included in object on right side

# How are lists different from strings?
## strings: built of letters, lists: more diverse options
## lists can be modified, strings can't

# Mutability: whether an object can be modified after it's been created
    ## lists

# Immutable: can't be modified
    ## strings

# Order: whether the order of elements in an object matters 
# (and whether this can be used to access elements)
    ## both strings and lists, which is why indexing works


# Quiz: List Indexing
## Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.
## Remember to account for zero-based indexing!

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month - 1]

print(num_days)
# result: 31


# Quiz: Slicing Lists
## Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

print(eclipse_dates[-3:])
# This slice uses a negative index to begin slicing three elements from the end of the list. 
# The end index can be omitted because this slice continues until the end of the list.


# LIST METHODS

name = 'Jim'
student = name
name = 'Tim'
print(name)
print(student)
# student name does not change because strings are immutable

scores = ["B", "C", "A", "D"...]
grades = scores
print("scores: " + str(scores))
print("grades: " + str(grades))
# output: ["B", "C", "A", "D"...]
scores[3] = "B"
print("scores: " + str(scores))
print("grades: " + str(grades))
# output: ["B", "C", "A", "B"...]
    ## affects both scores and grades because they are different variable names for the same list

# Useful functions:
.len() # how many elements in a list
.max() # returns greatest element of a list
    ## how the greatest element is determined depends on the type of objects in list
    batch_sizes = [15, 6, 89]
    print(max(batch_sizes)) # = result: 89

    python_varieties = ['Burmese Python', 'Ball Python', 'Reticulated Python']
    print(max(python_varieties)) # = result: Reticulated Python
        ## this would be the last value if the list was sorted alphabetically

    # max function is undefined for mixed lists with incomparable types
.min() # opposite of max
.sorted() # returns copy of a list in order from smallest to largest, leaving original list unchanged
    sizes = [15, 6, 89, 34]
    print(sorted(sizes))
    # result: [6, 15, 34, 89], order ascending
    sizes = [15, 6, 89, 34]
    print(sorted(sizes, reverse=True))
    # result : [89, 34, 15, 6], order descending

# JOIN
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions) 
# result: 
fore 
aft 
starboard 
port 
# "\n" = separator, or line break

names = ["Garcia", "O'Kelly", "Davis"]
print("-".join(names))
# result: Garcia-O'Kelly-Davis

names = ["Garcia" "O'Kelly" "Davis"]
print("-".join(names))
# result: GarciaO'KellyDavis
    ## without the commas separating the values, this occurs, due to python's default string literal appending

# join only works for strings, we will get an error using for something else

python_varieties = ['Burmese Python', 'Ball Python', 'Reticulated Python']
python_varieties.append('Blood Python')
print(python_varieties)
# adds 'Blood Python' to the end of the list


# TUPLES

# a data type for immutable ordered sequences of elements
# similar to lists but immutable (unchangeable), can't be sorted
# 2 or more closely related values that are usually used together (like latitude/longitude)

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {}x{}x{}".format(length, width, height))
# output: The dimensions are 52x40x100

# could also ommit first line:
length, width, height = 52, 40, 100
print("The dimensions are {}x{}x{}".format(length, width, height))

# SETS

# a data type for mutable unordered collections of unique elements

countries = ['Angola', 'Maldives', 'India', 'United States'...7 Stat77 more countries not displayed]
country_set = set(countries)
print(len(country_set))
#  shows the number of unique countries (no repeats) - 196

countries = ['Angola', 'Maldives', 'India', 'United States'...777 more countries not displayed]
country_set = set(countries)
print('India' in countries)
print('India' in country_set)
#  shows True, True as India is included in both lists

countries = ['Angola', 'Maldives', 'India', 'United States'...777 more countries not displayed]
country_set = set(countries)
country_set.add("Italy")
# adding a new country to the set


# DICTIONARIES AND IDENTITY OPERATORS

# dictionaries are more flexible than sets
# data type for mutable objects that store mappings of unique keys to values

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['carbon'])
# result = 6

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
elements['lithium'] = 3
print(elements)
# here we add lithium to the dictionary and assign it the value of 3

# keys do not have to have the same type in dictionaries

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print('mithril' in elements)
# checking if value is in dictionary the same as checking in list or set
# output here = False because it is not in dictionary

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements.get('dilithium'))
# .get() function - checks if value is in dictionary, and returns None or a value of your choice if not

# Quiz: Define a Dictionary
## Define a dictionary named population that contains this data:
#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population)


# COMPOUND DATA STRUCTURES

elements = {'hydrogen': {'number': 1, 'weight': 1.07, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.02, 'symbol': 'He'}}
print(elements['helium']['weight'])
# result: 4.02
# this first searches the elements dictionary for helium, and then searches the helium dictionary for the weight

# Quiz: Adding Values to Nested Dictionaries
## Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. After inserting the new entries you should be able to perform these lookups:

# >>> print(elements['hydrogen']['is_noble_gas'])
## False
# >>> print(elements['helium']['is_noble_gas'])
## True

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas': True}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

# This is how I added values to the elements dict. The syntax for adding elements to nested data structures is about the same as it is for reading from them.
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True


# Quiz: Count Unique Words
## Your task for this quiz is to find the number of unique words in the text. In the code editor below, complete these three steps to get your answer.
## Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
## Convert the list into a data structure that would keep only the unique elements from the list.
## Print the length of the container.

verse = "if you can keep your head when all about you are losing theirs and blaming it on you if you can trust yourself when all men doubt you but make allowance for their doubting too if you can wait and not be tired by waiting or being lied about don’t deal in lies or being hated don’t give way to hating and yet don’t look too good nor talk too wise"

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)

# Quiz: Verse Dictionary
# In the code editor below, you'll find a dictionary containing the unique words of verse stored as keys and the number of times they appear in verse stored as values. Use this dictionary to answer the following questions. Submit these answers in the quiz below the code editor.

# Try to answer these using code, rather than inspecting the dictionary manually!

# How many unique words are in verse_dict?
# Is the key "breathe" in verse_dict?
# What is the first element in the list created when verse_dict is sorted by keys?
# Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. Use this list of keys to answer the next two questions as well.
# Which key (word) has the highest value in verse_dict?

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# # find whether 'breathe' is a key in the dictionary
print('breathe' in verse_dict)
# OR
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# # create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict)
#  OR
sorted_keys = sorted(verse_dict.keys())

# # get the first element in the sorted list of keys
print(sorted_keys[0])

# # find the element with the highest value in the list of keys
print(max(sorted_keys)) 
# OR
print(sorted_keys[-1]) 

