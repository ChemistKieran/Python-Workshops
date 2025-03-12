- Workshop 2
    - More ways to manage/view your code
        - Using an Integrated Development Environment (IDE)
        - A Brief introduction to Jupyter Notebooks
    - More Python Basics
        - control statements (2):
            - Looping statements: for/while
            - (Transfer statements: break/continue/pass #!not covered in detail .. yet)
        - List / Dictionary comprehensions.

# Managing your code
## Integrated Development Environments (IDEs)
So far we have been using the python interpreter or notepad to input code. 
These show you that you can write code almost anywhere.

However, there are tools available that make writing code easier.
These include features such as:
- Syntax highlighting (different colours for different parts of the code)
- Code completion (suggesting the rest of a function name or variable name)
- Linting (checking your code for errors while you write it)
- version control (keeping track of changes to your code)
- variable explorer (viewing the contents of variables, particularly useful for lists and dictionaries)
- data visualisation (showing figures within the IDE)

There are two main IDE's that I suggest:
- Spyder
- Visual Studio Code (VS Code)

Spyder is a python specific IDE. 
It has a great variable explorer.

VS Code is a general purpose IDE. As well as python, it can be used for other languages such as HTML, CSS, Javascript, LaTeX, Markdown, R, C++, C#, Java etc.
VSCode has 'extensions' that can be installed to add functionality. 
If you can think of it, there's probably an extension for it.
The only downside is that the variable explorer is not as good as Spyder's and it's a little more complicated to set up.

### How to install:
### Spyder

``` PowerShell
winget install spyder
```
### VS Code

``` PowerShell
winget install vscode
```

The best way to understand how to use these IDE's work is an in-person demonstration.
failing that, here are some youtube videos:
- [vs code (offcial)](https://www.youtube.com/watch?v=-udPvjv8jyI)
- [vs code (corey schafer)](https://www.youtube.com/watch?v=-nh9rCzPJ20)
- [Spyder (official)](https://youtube.com/clip/UgkxLGmfW191xXEoH_93aVf1yve_1qjuKgAC?si=Cd-3G_dKuutiT4WF)


| objective 1 | Set up both a VScode and a sppyder IDE|
| --- | --- |

### Some notes on Spyder
Spyder is a bit weird in how it's set up. 
Firstly, if you look online, most install instructions will tell you to install Anaconda.
Anaconda in an environment manager. (see below)
It's not necessary to install Anaconda to use Spyder and for simplicity we won't (for now).
Spyder will initially use it's own copy of the python interpreter. 
Not the one we've been using in the terminal. 
As such, it will only come with the preinstalled packages. (see later for what packages are)
We can change this by going to Tools > Preferences > Python Interpreter.
We can then change the interpreter to the one we've been using in the terminal.
If you remember, we can find the path to the interpreter by typing 'where python' (or similar) and copying the path into spyder.

Spyder also uses something called IPython.
IPython is an interactive python interpreter. 
Basically, it's some extra code that is running in the background that lets us break down our code and run it bit by bit.
This means that we can run code line by line.
It was created for Jupiter notebooks (see below) but is also used in Spyder.
For this workshop series we won't be using this functionality but it's worth knowing about.

### Jupyter Notebooks
Jupyter notebooks are a way of writing code in a web browser.
They are great for data science as they allow you to write code and then add text and figures to explain what you're doing.
They are also great for sharing code as they can be exported as HTML or PDF files.

They also won't be covered in this workshop series as they add an additional layer of complexity.
For instance, you may have an error and not know if it's to do with the code or the notebook.
I also feel that when you get to more complicated i.e. concurrent programming tasks, you won't be thinking about code in the right mindset.

## Methods
If you remember, we talked about data types in the last workshop (can also say object types).
Each object type has something called methods. 
These are like functions that are built into the object type.
So while python  only had a limited number of built-in functions, each object type has a lot of built-in methods.
to use them, we use the syntax:
```python
object.method()
```
Again, you can think of each method as a function that is specific to the data/object type.

i.e.
```python
my_list.append(1)
```
You can think of them like functions for a specifc object that are applied through the use of the 'dot'.
 you can see all the methods for a list here:https://docs.python.org/3/tutorial/datastructures.html


# Assigning and reassigning lists and dictionaries
## Lists
we can define a list as follows, call the value of an element and reassign its value as follows:
```python
# Define a list
my_list = [1, 2, 3, 4, 5]

# Call the value of the first element
print(my_list[0])

# Reassign the value of the first element
my_list[0] = 6

# Call the value of the first element again
print(my_list[0])
```

## Dictionaries
```python
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Call the value of the key 'a'
print(my_dict['a'])

# Reassign the value of the key 'a'
my_dict['a'] = 4

# Call the value of the key 'a' again
print(my_dict['a'])
``` 

You can also add new elements to a list or dictionary using the append method (for lists) or by assigning a new key value pair (for dictionaries).

```python
# Define a list
my_list = [1, 2, 3, 4, 5]

# Add a new element to the list
my_list.append(6)

# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Add a new key value pair to the dictionary
my_dict['d'] = 4
```


# Control Statements II
## For Loops
### Iterating over a list
The most common iteration is over a list. Python will work out how many elements are in the list and iterate over each one.
```python

# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Use a for loop to iterate over the list
for number in numbers_list:
    print(number)
```
note the syntax (how it's written).

for __x__ in __an_actual_list__

x can be anything. We are defining an iterator variable. It's a variable that will be assigned the value of each element in the list as we iterate over it.

e.g.
```python

# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Use a for loop to iterate over the list
for sausage in numbers_list:
    print(sausage)
```
Also note that the second line is indented! The inerpreter will ignore any lines below until the loop is finished. 

### Iterating over a dictionary
We can also iterate over a dictionary. This is a little more complicated as dictionaries are not ordered.
Therefore, python won't know which order to display the elements in.
Fortunately, dictionaries have methods which allow us to iterate over them in a specific order.
These are: .keys(), .values() and .items().

.keys() will return a list of the keys in the dictionary.
.values() will return a list of the values in the dictionary.
.items() will return a list of tuples of the key and value pairs in the dictionary.


```python
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

#iterate over the dictionary using .keys() method
for key in my_dict.keys():
    print(key)

# Iterate over the dictionary using .values() method
for value in my_dict.values():
    print(value)


# Iterate over the dictionary using .items() method
for item in my_dict.items():
    print(item)
```



### A  note on unpacking
For the items method, it returns a list of tuples.
We can take a tuple and do something called unpacking.
This means that we can take the elements of the tuple and assign them to variables, so long as we have the same number of variables as elements in the tuple.

```python
# Define a tuple
my_tuple = ('a', 1)

# Unpack the tuple
first_variable, second_variable = my_tuple

print(first_variable)
print(second_variable)
```

Going back to our dictionary example, we can unpack the tuples that are returned by the .items() method.

```python
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over the dictionary using .items() method
for item in my_dict.items():
    key, value = item
    print(key, value)


# Or you can do it in one line...
for key, value in my_dict.items():
    print(key, value)
```



| objective 2 | Write a for loop that iterates over a list and prints each element. do the same for a dictionary.|
| --- | --- |

## In-place operators
In place operators are a shorthand way of writing code. They are used to update a variable in place. 
Common examples are:
- += (addition)
- -= (subtraction)
- *= (multiplication)
- /= (division)

we will use these in the loops below

## While Loops
While loops are a little different. They will continue to loop until a condition is met. 
```python
# Define a counter
counter = 0

# While the counter is less than 10
while counter < 10:
    print(counter)
    counter += 1
```
In the above example, we are defining a counter variable and setting it to 0.
We then have a while loop that will continue to loop until the counter is greater than or equal to 10.
Each time the loop runs, we print the value of the counter and then add 1 to it.

# Lists of lists
## Making lists from other lists
A task that we often need to do is to make a new list from an existing list.
We can do this using a for loop and an append statement.
append() is a **method** (see below) that we can use to add to the end of a list.
the 'argument' of the append function is the thing that we want to add to the list.



```Python
#Define a list of seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']


#Create an empty list to store the seasons
seasons_as_fstrings = []

# display the seansons with some commenatary using an fstring
for season in seasons:
    seasons_as_fstrings.append(f'the season is {season}') #append the season to the list which is outside the loop

print(seasons_as_fstrings)
```

## Making dictionaries from other dictionaries
We can also make a new dictionary from an existing dictionary.

```python
# Define a dictionary
dict_1 = {'a': 1, 'b': 2, 'c': 3}


# Create an empty dictionary
dict_as_fstrings = {}

# Iterate over the dictionaries
for key, value in dict_1.items():
    dict_as_fstrings[key] = f'the value is {value}'

print(dict_as_fstrings)

```

## List Comprehensions
List comprehensions are a shorthand way of creating a list and then using a for loop to append to it.

list comprehensions use the syntax: [ [thing to append] for [iterator] in [list] ]

i.e. [i +1 for i in [1, 2, 3, 4, 5]]

```python
# Define a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Add one to each number in the list
numbers_list_plus_one = [i + 1 for i in numbers_list]
```

This is the same as 
```python
numbers_list = [1,2,3,4,5]
# we want [2,3,4,5,6]


numbers_list_plus_one = []

for i in numbers_list:
	new_list.append(i+1)
```
but in this case we instantiate the list and generate it at the same time.  

## Dictionary Comprehensions
Dict comprehensions are similar to list comprehensions but they return a dictionary instead of a list.

dict comprehensions use the syntax: { [key]: [value] for [iterator] in [list] }

i.e. {k: v for k, v in [('a', 1), ('b', 2), ('c', 3)]}

```python
#Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

#Create a new dictionary with the values multiplied by 2
my_dict_times_two = {k: v * 2 for k, v in my_dict.items()}
```
**These shorthands are particularly useful in data science.**

| objective 3 | Write a list comprehension that takes a dictionary of strings and returns a list of the lengths of the strings.|
| --- | --- |


## Homework
This week I phoned-it-in and asked ChatGPT to write some suggestions. 
They're good - you can check out the suggestions here: [workshop_2_HomeworkChatGPT.md](workshop_2_HomeworkChatGPT.md)


# Things to ask the AI

- What is an IDE?
- How do I choose my python interpreter in spyder/VScode?
- What is a linter and how do I install one in VScode?
- How do I use a for loop to iterate over a list?
- How do I use a for loop to iterate over a dictionary?
- How do I use a while loop?
- What are some examples of in-place operators and how do I use them?
- What are list and dictionary comprehensions and how do I use them?