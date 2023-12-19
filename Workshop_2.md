# Workshop 2

## More ways to manage/view your code
- Using an Integrated Development Environment (IDE)
- A Brief introduction to Jupyter Notebooks

## More Python Basics
- control statements (2):
    - Looping statements: for/while
    - (Transfer statements: break/continue/pass #!not covered in detail .. yet)
- List / Dictionary comprehensions.

  
## Functional Programming
- Functions
- Python Libraries 
- How to read documentation

- A brief introduction to environment management venv/conda
  
## Importing Data 
- Reading in data from a file (Pathlib)
- An Introduction to Pandas


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
We can also iterate over a dictionary. This is a little more complicated as we have to define two variables in the for loop. One for the key and one for the value.
```python
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over the dictionary
for key, value in my_dict.items():
    print(key, value)
```
In the above example, we are using the .items() method to return a list of tuples.
(If you don't remember what a tuple is, it's a list that can't be changed. we often see them as pairs i.e. a list of touples [(thing1, property1), (thing2, property2)]))
Each tuple contains a key and a value. 
We are then assigning the key to the variable key and the value to the variable value.

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
append() is a function that we can use to add to the end of a list.
the 'argument' of the append function is the thing that we want to add to the list.

```Python
#Define a list of seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

#Define the number of years
years = 5

#Create an empty list to store the seasons
all_seasons = []

#Iterate over a number of years
while years > 0:
    for season in seasons:
        all_seasons.append(season) #append the season to the list which is outside the loop
    years -= 1

print(all_seasons)
```

## Making dictionaries from other dictionaries
We can also make a new dictionary from an existing dictionary.

```python
# Define a dictionary
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'c': 4, 'd': 5, 'e': 6}
dict_3 = {'e': 7, 'f': 8, 'g': 9}

#Put dictionaries in a list
dict_list = [dict_1, dict_2, dict_3]

# Create an empty dictionary
compound_dict = {}

# Iterate over the dictionaries
for dictionary in dict_list:
    for key, value in dictionary.items():
        compound_dict[key] = value


print('compound dict', compound_dict)
print('dict_2', compound_dict['dict_2'])
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


# Functional Programming
## A simple function
It has to be said that now you can make virtually anything in python.
However, we often want to do the same thing over and over again.
This means you'll end up writing a million lines of code before you know it. 
This is where functions come in.

Wouldn't it be great if we could take a big chunk of our code, 
package it into a little black box in such a way that we can feed it some data and it will spit back out a result?

Well, we can!

the syntax for a function is:
```python
def function_name(argument1, argument2, argument3):
    # do something with the arguments
    return result
```

**def** tells the interpreter that we are defining a function.
**function_name** is the name of the function. It can be anything you want (as long as it doesn't have a space).
**argument1, argument2, argument3** are the arguments that we want to pass to the function.
**return** tells the function to return the result of the function.

```python
# Define a function that adds two numbers together
def add_two_numbers(number1, number2):
    result = number1 + number2
    print(result)
    return result

# Call the function
add_two_numbers(1, 2)
add_two_numbers(3, 4)
```

The big thing to notice here is something called scope.
Scope is the area of the code where a variable can be accessed.
In the above example, the variables number1 and number2 are defined within the function.
This means that they can only be accessed within the function.
If we try to access them outside of the function, we will get an error.

Before we call the function 'add_two_numbers', the variables number1 and number2 don't exist.
When we call the function, we pass the values 1 and 2 to the function.
We now have an instance of the function that has the values 1 and 2 assigned to the variables number1 and number2.

In the above example, we are printing the result of the function.
If however, we wanted to use the result of the function in another function, we would need to assign the result to a variable.


```python
# Define a function that adds two numbers together
def add_two_numbers(number1, number2):
    result = number1 + number2

    return result

# Call the function
result_1 = add_two_numbers(1, 2)
result_2 = add_two_numbers(3, 4)

print(result_1)
print(result_2)
```

## Returning multiple values
We can also return multiple values from a function.
We do this by separating the values with a comma.

```python
# Define a function that returns both the sum and the product of two numbers
def add_and_multiply_two_numbers(number1, number2):
    summed = number1 + number2
    product = number1 * number2

    return summed, product

# Call the function
result_a, result_b = add_and_multiply_two_numbers(1, 2)

print(result_a)
print(result_b)
```

Sometimes, you will also see the output of a function packed into a tuple.

```python
# Define a function that returns both the sum and the product of two numbers
def add_and_multiply_two_numbers(number1, number2):
    summed = number1 + number2
    product = number1 * number2

    return (summed, product)

# Call the function
result = add_and_multiply_two_numbers(1, 2)

#extract tuple
result_a = result[0]
result_b = result[1]
```



