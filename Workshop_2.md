- Workshop 2
    - More ways to manage/view your code
        - Using an Integrated Development Environment (IDE)
        - A Brief introduction to Jupyter Notebooks
    - More Python Basics
        - control statements (2):
            - Looping statements: for/while
            - (Transfer statements: break/continue/pass #!not covered in detail .. yet)
        - List / Dictionary comprehensions.
    - Functional Programming
        - Functions
        - Python Libraries 
        - How to read documentation
        - A brief introduction to environment management venv/conda
    - Importing Data 
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
for iten in my_dict.items():
    print(item)
```



### A  note on unpacking
For the itens method, it returns a list of tuples.
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

#Define the number of years

#Create an empty list to store the seasons
seasons_as_fstrings = []

#Iterate over a number of years

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
Also note the indentation.



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

## Arguments and Keyword Arguments
When we define a function, the order that we define the arguments in is the order that we need to pass them to the function.
i.e. the first thing we put in brackets in the function definition is the same thing as the first thing when we are using the function.

We can also explicitly name the arguments when we define the function.
we call these keyword arguments. we define them by using an equals sign "=".

```python
# Define a function that adds two numbers together
def add_two_numbers(FirstNumber = 0, SecondNumber = 0):
    result = FirstNumber + SecondNumber

    return result

# Call the function
result_1 = add_two_numbers(FirstNumber = 1, SecondNumber = 2)
```
This allows us to pass the arguments in any order we want. They are also assigned a default value.
This is often used for optional arguments. (i.e. our function will still work if we don't pass them a value)

| objective 4 |  write a function that takes a dictionary of strings and returns a dictionary of the lengths of the strings.|
| --- | --- |






# Importing Functions
## Importing our own functions from other files
We can also import functions from other files.
This is particularly useful if we have a function that we use a lot and we don't want to have to copy and paste it into every file we use it in.

To do this, we need to create a file with the function in it.
We can then import the function using the syntax:
```python
from [file_name] import [function_name]
```
For example:
in python_functions.py
```python
# Define a function that adds two numbers together
def add_two_numbers(number1, number2):
    result = number1 + number2

    return result
```
in main.py
```python
from python_functions import add_two_numbers

result = add_two_numbers(1, 2)
```

## Python Libraries
The most powerful tool in python is the ability to import libraries.
Libraries are collections of functions that have been written by other people.
Built into Spyder are the following libraries:
- numpy (numerical python)
- pandas (data analysis)
- matplotlib (data visualisation)
- scipy (scientific python)
- scikit-learn (machine learning)

For our version of python (at our given python path), we need to install these libraries from the internet.
We can do this using the package manager pip.

```powershell
pip install numpy
```

```powershell
pip install pandas
```
etc. etc.

Most packages come from a website called **pypi.org.**

To import a package, we use the syntax:
```python
import [package_name]
```
To import a specific function from a package, we use the syntax:
```python
from [package_name] import [function_name]
```

Sometimes, we want to import a package but we don't want to have to type the package name every time we use it.
We can do this using the syntax:
```python
from [package_name] import [function_name] as [short_name]
``` 
This will allow us to use the function by typing the short name instead of the full name.
Sometimes, we do this just because we want our own name for the function.


The best way to find out how to use a package is to read the documentation.
To find the documentation, google the package name + 'documentation'.
This will give you an overview of the package and how to use it.

More powerful in a lot of ways, however, is the API reference.
API stands for Application Programming Interface.
you can find the API reference by googling the package name + 'API reference'.
This is a list of all the functions that are available in the package.
It will tell you what the function does, what arguments it takes and what it returns.

## How to read documentation

Here is the link to the numpy API reference:
https://numpy.org/doc/stable/reference/routines.math.html

In here, we can find a adding function.
https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add

The documentation reads as follows:


--- 
### numpy.add
```numpy.add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'add'>```

*Add arguments element-wise.*

  - **Parameters:**
    - **x1, x2array_like**
        - The arrays to be added. If x1.shape != x2.shape, they must be broadcastable to a common shape (which becomes the shape of the output).

    -  **out: tndarray, None, or tuple of ndarray and None, optional**
        - A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

    - **where: earray_like, optional**
        -  This condition is broadcast over the input. At locations where the condition is True, the out array will be set to the ufunc result. Elsewhere, the out array will retain its original value. Note that if an uninitialized out array is created via the default out=None, locations within it where the condition is False will remain uninitialized.

    -   ** **kwargs**
         -    For other keyword-only arguments, see the ufunc docs.

- **Returns:**
    - **add : ndarray or scalar**
        -  The sum of x1 and x2, element-wise. This is a scalar if both x1 and x2 are scalars.


--- 

How do we read the above?
Firstly, we can see that the function takes two arguments: x1 and x2.
These will be the first two things we put into the function when we use (call) it.

After that, we can see that there are a bunch of optional arguments. 
We know this because of the "=" sign.

Next, written in italics, we can see the description of the function.
This tells us what the function does.

After that, we can see the parameters.
These are the things that we need to pass to the function.
We can see that x1 and x2 are arrays.

Then, we have the keyword arguments.

Then, we have other keyword arguments "**kwargs".
This is not something we need to worry about for now. 
(roughly) All it's saying is that the function we're using is in-turn using some other functions that have their own keyword arguments.
We can find out what these are by looking at the 'inheritance' section of the documentation.
In this case, there is no inheritance information provided.


Finally, we have the return value. This tells us the type of what the function will return.

## A word on object types


In the last workshop we talked about object types built into python.
Now that we are working with libraries, it is worth bearing in mind that we may have lots of new object types.


In all this documentation, note the importance of the 'type' of variable/object that is used/returned.
Think of it like this:
You can't add a string to a number.

1 + 1 = 2

"1" + 1 = error

Similarly, 

[list_of_6_numbers] + [list_of_6_numbers] = [list_of_6_added_numbers] 

[list_of_6_numbers] + [Super_special_object_which_looks_like_a_list_but_isn't] = error

You will see this a lot more when we come to pandas dataframes. 


## Virtual Environments
As you can see, Libraries are great!
However, they are also constantly being updated.
When someone updates a library, they may change the way a function works.
When they do this, they may not check it against every other package in existence.
This means that sometimes, when you update a package, it will break another package.

Personally (and probably rather controversially), I think you should make an effort to keep your packages up to date and re-write your code when something breaks.
Practically however, this isn't always possible.

A work-around people use is to create a virtual environment.
A virtual environment is a copy of your python installation with all of the packages that you are using.
Often an enviroment manager will allow you use do version control on your packages.
i.e. you can choose numpy version 1.2.3 and pandas version 4.5.6 and it will install those versions and only those versions.

The two most popular environment managers are:
- anaconda
- venv
- poetry (very new and trendy)
  
Anaconda is very popular with scientists and can be used via a GUI (as well as a TUI).
venv is used with a TUI/command line interface, but is more lightweight (i.e. quicker to startup/use).

For this workshop series, we won't be using an environment manager, but will be instead working with the most up-to-date packages.
(Just be aware that a lot of data-scientists will argue that you should use a package manager.)


# Reading data from a file
There is only one built-in way to read data from a file in python.
This is using the open() function.
We need to pass the function the path to the file and the mode that we want to open the file in.
The mode can be: 'r' (read), 'w' (write), 'a' (append), 'r+' (read and write).
The path can be either a relative path or an absolute path.
In this case the file is in the same directory as our code.

```python
# Open and read a text file
with open('data.txt', 'r') as file:
    data = file.read()

print(data)
```
This will read the entire file into a string.

We won't really use this very much. 

Instead, we'll use the functions built into various packages.
Convenient functions from different packages are:

| File type | Package | Function |
| --- | --- | --- |
| .csv | pandas | pd.read_csv() |
| .xlsx | pandas | pd.read_excel() |
| .json | json | json.load() |
| pickle | pickle | pickle.load() |


## Using Pathlib
Pathlib is a package that allows us to work with file paths.
It can import a folder as a 'path' object.

```python
from pathlib import Path
```
```python
# Import a folder as a path object
path = Path('data')

# List all files in the folder
print(path.glob('*'))
```
glob() is a function that returns a list of all the files in a folder.
The argument is a wildcard. In this case, we are using the wildcard '*' which means 'anything'.

If we want to find all the files that end in .csv, we can use the wildcard '*.csv'

```python
# Import a folder as a path object
path = Path('data')

# List all files in the folder
print(path.glob('*.csv'))
```
If we have a folder called 'data' and a file called 'data.csv', we can use the wildcard 'data/*.csv' to find the file.

```python
# Import a folder as a path object
path = Path('./data')

# List all files in the folder
print(path.glob('*.csv'))
```

note that glob() returns a generator object. 
This means that it doesn't actually return a list of files.
It returns an object that can be iterated over to return a list of files.
This is useful if we have a lot of files in a folder as we don't have to load them all into memory at once.
However, it can be a little confusing to work with as it can only be iterated over once.
i.e. you can't call the object twice.

```python
# Import a folder as a path object
path = Path('./data')

# List all files in the folder that end in .csv
files = path.glob('*.csv')

# first iteration
for file in files:
    print(file)

# second iteration
for file in files:
    print(file)
#!! Results in an empty list
```python

To make it easier to work with, we can convert the generator object to a list.

```python
# Import a folder as a path object
path = Path('./data')

# List all files in the folder that end in .csv
files = [file for file in path.glob('*.csv')]
```
Pathlib also has some handy functions for working on path objects.
These include:
- .name (returns the name of the file)
- .stem (returns the name of the file without the extension)
- .suffix (returns the extension of the file)
- .parent (returns the parent folder of the file)
- .exists (returns True if the file exists)
- .is_dir (returns True if the path is a directory)
- .is_file (returns True if the path is a file)
  
  i.e.
```python
# Import a folder as a path object
path = Path('./data')

# List all files in the folder that end in .csv
filenames = [file.stem for file in path.glob('*.csv')]
```

# An introduction to Pandas
Pandas is a package that allows us to work with objects called **series** and **dataframes**.
A series is similar to a list, but is more powerful as we can use custom indexes. i.e. [0.0, 1.0, 2.0, 3.0] as oppoesed to [0, 1, 2, 3].
They are also more memory efficient than lists.
Dataframes are a way of storing data in a table.
i.e. it is 2 dimensional. 
We can name also name the rows. i.e. "y-data".

Pandas also has some really great tools for importing data from files.
i.e. pd.read_csv() and pd.read_excel().

Because this course focuses on data science we will jump right in and import some data, rather than constructing our own data tables. 

For an overview of pandas, see the documentation: (https://pandas.pydata.org/docs/user_guide/dsintro.html)


Firstly, lets look at a simple import of a csv file.

```txt
Name,Age,Location
John,25,New York
Alice,30,Los Angeles
Bob,22,Chicago
Eva,35,San Francisco
```

```python
import pandas as pd

# Provide the path to your CSV file
csv_path = 'path/to/test_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Display the DataFrame
print(df)
```


Now lets look at a slightly more complicated example.
```txt
# This is a complex CSV file with various features
# Some lines start with comments, and there are multiple header rows
# The data has missing values, and columns are separated by different delimiters

# Basic Information
Name|Age|Location
John|25|New York
Alice|30|Los Angeles
Bob|22|Chicago
Eva|35|San Francisco

# Additional Details
Salary;Department;Bonus
50000;IT;2000
60000;Marketing;1500
;Finance;1000

# Ratings
Overall Rating,5,4,3,2,1
John,4,5,3,4,5
Alice,5,4,4,5,5
Bob,3,3,2,4,4
Eva,4,5,4,3,5
```

In this case we need to read the documentation for pd.read_csv() to find out how to import the data.
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html


```Python
import pandas as pd

# Provide the path to your CSV file
csv_path = 'path/to/complex_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(
    csv_path,
    comment='#',           # Ignore lines starting with '#'
    skip_blank_lines=True,  # Skip blank lines
    delimiter='[;|]',       # Use regular expression for multiple delimiters
    header=[0, 4],          # Specify multiple header rows
    index_col=0             # Use the first column as the index
)

# Display the DataFrame
print(df)
```

## Putting together paths and dataframes - importing multiple files

So far we have imported a single file.
However, we often want to import multiple files.

Here are some examples of how we can do this.
Put the following files in a folder called 'data'.:

spec_1.txt
```txt
Wavelength,Intensity
400,0.2
410,0.5
420,0.8
430,1.2
440,1.5
```

spec_2.txt
```txt
Wavelength,Intensity
400,0.5
410,0.7
420,1.0
430,1.3
440,1.6
```

spec_3.txt
```txt
Wavelength,Intensity
400,0.8
410,1.0
420,1.5
430,1.8
440,2.0
```
And then to import your data:
```python
import pandas as pd
from pathlib import Path

# Import a folder as a path object
path = Path('./data')

files = {}
# make a dictionary where the key is the filename and the value is an dataframe-version of the csv file
For i in path.glob('*.txt'):
    files[i.stem] = pd.read_csv(file)

# you now have a dictionary of dataframes, to call a specific dataframe, use the key
print(files['spec_1'])
```

we can do the same thing with a dictionary comprehension

```python
import pandas as pd
from pathlib import Path

# Import a folder as a path object
path = Path('./data')

files = {i.stem: pd.read_csv(i) for i in path.glob('*.txt')}
```
| objective 5 | Import the data from the files in the data folder into a dictionary of dataframes.|
| --- | --- |

# Homework
Import some real data from a series of UV-vis files taken on a Perkin-Elmer Lambda 9 spectrometer.
This can be found [Here](./Homework%202/)

Extra task: can you normalise the data so that none of the values go above 1.


# Things to ask the AI

- What is an IDE?
- How do I choose my python interpreter in spyder/VScode?
- What is a linter and how do I install one in VScode?
- How do I use a for loop to iterate over a list?
- How do I use a for loop to iterate over a dictionary?
- How do I use a while loop?
- What are some examples of in-place operators and how do I use them?
- What are list and dictionary comprehensions and how do I use them?
- What is a function and how do I use it?
- How do I write a function?
- What is a Method in python and how do I use it?
- What is the difference between a function and a method?
- How do I import a function from another file?
- How do I import a package?
- How do I import a function from a package?
- Why do we write import x as y in python?
- How do I read the documentation for using its online API reference?
- How do I read a text file into python as a string?
- How do I read a csv file into python as a dataframe?
- How do I use Pathlib to find all the files in a folder?
- How do I use Pathlib to import all the csv files in a folder as a dictionary of dataframes?

