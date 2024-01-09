# CISM Python Workshop Series 2024

## Workshop 1 Overview

### Getting Set Up
- Installing Python
- Using the interpreter
- Navigating without a graphical user interface



### Introduction to Python
- Data types
- control statements (1):
    - conditional statements: if/else/elif



# Introduction 

### Moore's Law

Moore's Law is the observation that the number of transistors on a microchip tends to double approximately every two years,

<img src='./Figures/moores_law.jpg' width=80%>

### Kieran's Law

Computers become twice as convoluted every two years.

<img src="./Figures/Kierans%20Law.svg" width=80%>


### Why is it called a PC? 

Personal computers arrived later than terminals, where multiple terminals were connected to a single computer mainframe.
Each user would log in with a username and password. 
This is a lay-over from the early days of computing. As you will see there are many of these! 

<img src="./Figures/terminal-user.svg" width=60%>



### What is a computer? 
- Really a computer is just a series of files which are mainly **data** and **instructions**. 
- We can use the terminal to navigate these files and send (some) instructions.

## How to use (windows) terminal
### installation
| OBJECTIVE 1: Install Windows Terminal |
|--|


If you don't already have windows terminal installed, you can install it from the Microsoft Store.
Alternatively you can launch the command prompt and use that .. or do the following to install windows terminal.

``` winget install Microsoft.WindowsTerminal ```

winget is a program which allows you to install programs from the command line.

### file naviagtion

1. **Change Directory (`cd`):**
   - `cd`: Change to the user's home directory.
   - `cd [directory]`: Change to the specified directory.
   - `cd ..`: Move up one level in the directory tree.
   - `cd \`: Change to the root directory.
   - `cd ~` : Change to the user's home directory (Unix-like environments).`
   - `cd [start of name]*`: auto-fills the rest of directory 
   - `cd '[name with spaces]'`: allows you to navigate to a directory with spaces in the name.
   
2. **List Contents (`dir` or `ls`):**
   - `dir`: List the files and directories in the current directory.
   - `ls`: Alternatively used in Unix-like environments to list directory contents.
   - `dir /w`: Display the files and directories in wide format.
   - `dir /p`: Display one page at a time.

3. **Create Directory (`mkdir`):**
   - `mkdir [directory]`: Create a new directory.

4. **Remove Directory (`rmdir`):**
   - `rmdir [directory]`: Remove an empty directory.
   - `rmdir /s /q [directory]`: Remove a directory and its contents (use with caution).

5. **Copy (`copy`) and Move (`move`):**
   - `copy [source] [destination]`: Copy a file.
   - `move [source] [destination]`: Move or rename a file or directory.

6. **Delete (`del`) and Remove (`remove-item`):**
   - `del [file]`: Delete a file.
   - `remove-item [file]`: PowerShell command to remove a file or directory.

7. **Path Variable (`%PATH%`):**
   - Echo `%PATH%`: Display the directories listed in the system's PATH variable.
   - on Powershell use `echo $env:PATH`    
  !!Important note, powershell and command prompt have slightly different syntax!! - we will be using command prompt as it looks prettier`
1. **Tab Completion:**
   - Use the Tab key to autocomplete commands and directory/file names.

8. **A note on full and relative File paths**
   - instead of writing "c:\Users\myusername\Documents\myfolder\myfile.txt" you can write "." for the current directory, ".." for the parent directory, 
   and "~" for the user's home directory.
   -  To use a specific folder you can write i.e. "./folder".
   -  Note  that windows and linux OS's use different slashes to denote directories. This can sometimes cause problems so just be aware. 

**To begin with, you only really need to know cd and ls**

## Running Programs (Part 1)
In order to run a program, you can type in the path of the program. 
(the path is the location of the program on your computer i.e. C:\Program Files\User\Path_to_file\program.exe)

**OR**

you can type the name of the program. i.e. 'python' or 'explorer' 

Some programs have a GUI (Graphical User Interface) and some have a TUI (Terminal user interface).
In this course you will see that a TUI is powerful as you can 'link' different programs together. 

Just because some programs don't have a GUI, doesn't mean you should think of them differently to e.g. word, chrome or excel. 


** winget ** is an example of a program which can be run from the terminal.
This program installs other programs from e.g. the windows store. 

We will use this to install python, if you don't already have it installed. 
(Read on before trying this)


## Passing arguments to programs (Part 1)
When we have a program with a TUI, there are no buttons at the top of the screen to browse through. 
We either have to look up some documentation for the program, or we can *usually* pass a help 'argument'.
This is just a command that we can pass to the program to get some help.

Try typing `winget --help` into the terminal.
(the two dashes '--' are called a flag and just suggest that the argument we are passing is ancillary in some way)


If you don't already have python installed, you can install it by typing `winget install python` into the terminal.


## Running Programs (Part 2)
If you have python installed, you can run it by typing `python` into the terminal.

While you do this, think **What am i actually doing when i type python into the terminal?**
What you're doing is looking up a list of 'environmental variables' on your computer.
These are variables which can be accessed from anywhere on your computer.

Normally a variable is added to your Path when you install a program.


## The Print Statement
Now that we have python up and running lets try something basic. 
Type `print('Hello World')` into the terminal and press enter.

This is your first example of a function which is built into python.
A function has two pars, the name of the command (outside the brackets) and the thing that it's operating on (inside the brackets).

The full list is here:
https://docs.python.org/3/library/functions.html
But in reality you will only use <10 of these. 

| OBJECTIVE 2: Print 'hello [name]' in python  |
|--|

Another useful function is `type()`. This tells you the type of the variable you pass to it. (you will see this below)
Similarly, `len()` tells you the length of the variable you pass to it.

```Python
## Declaring Variables
Rather than just printing a string, we can store it as a variable and then print it.
To store a variable, we just type the name of the variable, followed by an equals sign, followed by the value we want to store.
```Python
my_variable = 'Hello World'
print(my_variable)
print(type(my_variable))
print(len(my_variable))
```

## f-strings
A relatively new feature of python is the f-string.
This allows you to insert variables into a string.
For instance, if we have a variable called 'name' which contains the string 'your name', we can print it by typing `print(f'Hello {your name}')` into the terminal.

'''Python
name = 'Your name'
print(f'Hello {name}')
'''

### Comments
Comments are a way of adding notes to your code.
They are not executed by the interpreter, so you can write whatever you want in them.
They are denoted by a hash symbol (#) at the start of the line.
You can also create multi-line comments by using three quotes (""") at the start and end of the comment.
Also, the use of (') or (") is interchangeable.



# Data Types
There are only a few data types in python, but they are very powerful.
We will go through them one by one, but they are summarized in the code extract below.

```Python
# Integer
my_integer = 42
print(f"Integer: {my_integer} - {type(my_integer)}")

# Float
my_float = 3.14
print(f"Float: {my_float} - {type(my_float)}")

# String
my_string = "Hello, World!"
print(f"String: '{my_string}' - {type(my_string)}")

# Boolean
my_boolean = True
print(f"Boolean: {my_boolean} - {type(my_boolean)}")

# List
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list} - {type(my_list)}")

# Tuple
my_tuple = (6, 7, 8, 9, 10)
print(f"Tuple: {my_tuple} - {type(my_tuple)}")

# Dictionary
my_dict = {"key1": "value1", "key2": "value2"}
print(f"Dictionary: {my_dict} - {type(my_dict)}")

# Set
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set} - {type(my_set)}")

# NoneType
my_none = None
print(f"NoneType: {my_none} - {type(my_none)}")

# Complex
my_complex = 2 + 3j
print(f"Complex: {my_complex} - {type(my_complex)}")
```

 ### Descriptions
- **Integer:** Whole numbers
- **Float:** Decimal numbers (floating point number)
- **String:** Text
- **Boolean:** Binary choice (True/False) (name comes from Boolean algebra)
- **List:** Ordered collection
- **Tuple:** Immutable ordered collection
- **Dictionary:** Key-value pairs
- **Set:** Unordered collection of unique elements
- **NoneType:** Represents absence of a value
- **Complex:** Complex number with real and imaginary parts

### Strings 
Note that strings can be enclosed in single quotes (') or double quotes (").
Also note that you can have spaes in strings.
You can also join strings together using the + operator.


### Properties
- **Ordered vs Unordered:**
  - **Ordered:** Elements have a specific sequence or arrangement.
  - **Unordered:** Elements have no guaranteed sequence or arrangement.

- **Mutable vs Immutable:**
  - **Mutable:** Objects can be modified or changed after creation.
  - **Immutable:** Objects cannot be modified or changed after creation.

### Lists and Dictionaries
- lists - square brackets and separated by commas.
- Dictionaries - curly brackets and separated by commas. These have a key and a value. The key is the name of the element and the value is the value of the element.
- Lists are ordered, dictionaries are not.
- We can access elements of a list by using square brackets and the index of the element we want to access.
  but remember that python is zero indexed, so the first element is at index 0. 
  i.e. `my_list[0]` will return the first element of the list. Then, to access the second element we would use `my_list[1]` and so on.
- We can access elements of a dictionary by using square brackets and the key of the element we want to access.
  i.e. `my_dict['key1']` will return the value of the element with key 'key1'.
- We can add elements to a list by using the append function. i.e. `my_list.append(6)` will add the number 6 to the end of the list.
- We can add elements to a dictionary by using the square brackets and the key of the element we want to add. i.e. `my_dict['key3'] = 'value3'` will add a new element to the dictionary with key 'key3' and value 'value3'.
- Sets are rarely used so we won't cover them in detail here. Just be aware that they exist.

## Writing a python script
So far, we have been using the python interpreter.
However, if we want to write a lot of commands, this quickly becomes tedious.
Fortunately, we can write a python script, which is (to begin with) just a list of commands run sequentially.

Our python script is just like a text document, except we save it with the extension '.py' instead of '.txt'.
We can then run this script by typing `python [path to script]` into the terminal.
For instance, if we have a script called 'my_script.py' in the current directory, we can run it by typing `python my_script.py` into the terminal.

In order to write a script, we need a text editor. For now, we will use notepad.

| OBJECTIVE 3: Write a python script which stores and prints as many of the above data-types as you would like|
|--|

## Control Statements I
### Conditional Statements
- Conditional statements are used to control the flow of a program.
- The most common conditional statements are `if`, `else`, and `elif`.
- Conditional statements are used to execute code only if a certain condition is met.
- ** Note the syntax (below) if the statements. i.e. **"if [condition]: [code to be exectured]"**. The colon is important here**
- **Note that the code inside the conditional statement is indented.** This is very important as it tells the interpreter what to carry out **only if conditions are met**. Anything lines that are indented will not be read unless you meed a condition in the above (non-empty) line.
- The most common way to indent your code is with the tab key. However, you can also use spaces. Just be aware that you can't mix tabs and spaces.

### Evaluators
In order to set a condition, we also need to know some evaluators.
These are the symbols which we use to compare two values.
The most common evaluators are:
- **==** : equal to
- **!=** : not equal to
- **>** : greater than
- **<** : less than
- **>=** : greater than or equal to
- **<=** : less than or equal to
- **is** : object identity
- **is not** : negated object identity
- **in** : membership
- **not in** : negated membership
- **and** : logical and
- **or** : logical or
  
### with a boolean
```Python
is_it_raining = True

if is_it_raining == True:
    print("You should take an umbrella")
else:
    print("You don't need an umbrella")
```


### with a number
```Python
speed_of sound = 343 # m/s
velocity = 100 # m/s
mach_number = velocity / speed_of_sound # divide velocity by speed of sound to get mach number

if mach_number < 0.8:
    print("Subsonic")
elif mach_number > 1.2:
    print("Supersonic")
else:
    print("Transonic")
```
### with a string
```Python 
Staff_or_student = "Staff"

if Staff_or_student == "Staff":
    print("You may have a real email")
elif Staff_or_student == "Student":
    print("You may have an incoherent list of numbers")
else:
    print("You are neither a student nor a member of staff")
```

### exploiting a boolean
because a boolean is itself a condition, we can use it directly in an if statement.

```Python
is_it_raining = True

if is_it_raining:
    print("You should take an umbrella")
else:
    print("You don't need an umbrella")
```

### using if not
```python
is_it_raining = False

if not is_it_raining:
    print("You don't need an umbrella")
else:
    print("You should take an umbrella")
```

### With a list
```Python
my_list = [1, 2, 3, 4, 5]

if 1 in my_list:
    print("1 is in the list")
else:
    print("1 is not in the list")
```
### evaluating if it is present
```Python
my_list = []

if my_list:
    print("The list is not empty")
else:
    print("The list is empty")
```
### evaluating multiple conditions
```Python
my_list = [1, 2, 3, 4, 5]

if 1 in my_list and 2 in my_list:
    print("1 and 2 are in the list")
else:
    print("1 and 2 are not in the list")
```
# Homework
There was a command not covered in this workshop called input().
When working in the terminal, this command allows you to input a value into your program.


<img src='./Figures/text_adventure.svg' width=80%>

For a homework task I want you to write a miniature text-based adventure game.
Try to use as many of the data types and control statements as you can.

Here is an example of a text-based adventure game generated by ChatGPT:



```Python
print("Welcome to the Chemistry Lab Adventure!")
scientist_name = input("Enter your scientist name: ")

print(f"Hello, {scientist_name}! You are a scientist in a top-secret chemistry lab.")
print("Your mission is to conduct experiments and discover a groundbreaking formula.")
print("You enter the lab and see various equipment and chemicals.")

# First choice
choice1 = input("1. Check the lab equipment\n2. Mix chemicals\nEnter your choice (1 or 2): ")

if choice1 == "1":
    # Check the lab equipment
    print(f"You, {scientist_name}, decide to inspect the lab equipment.")
    print("You find an advanced spectrophotometer and a high-speed centrifuge.")
    print("What do you want to do?")
    print("1. Use the spectrophotometer\n2. Use the centrifuge")

    # Second choice
    choice2 = input("Enter your choice (1 or 2): ")

    if choice2 == "1":
        print(f"You, {scientist_name}, use the spectrophotometer to analyze a mysterious sample.")
        print("The results reveal a unique molecular structure.")
    else:
        print(f"You, {scientist_name}, use the centrifuge to separate a mixture.")
        print("You discover a new compound in the process.")

else:
    # Mix chemicals
    print(f"You, {scientist_name}, decide to mix chemicals.")
    print("You choose two random chemicals from the shelf and mix them.")
    print("What do you want to do?")
    print("1. Analyze the reaction\n2. Dispose of the mixture")

    # Second choice
    choice2 = input("Enter your choice (1 or 2): ")

    if choice2 == "1":
        print(f"You, {scientist_name}, analyze the reaction and identify a new compound.")
        print("The lab applauds your discovery.")
    else:
        print(f"You, {scientist_name}, dispose of the mixture safely.")
        print("No harm done, but you missed a potential breakthrough.")

# Outcome
print(f"Congratulations, {scientist_name}! You have made significant discoveries in the lab.")

```


# AI prompts for this workshop
- ``` How do I navigate file directories in windows terminal (i'm using [insert cmd or powershell])?```
- ``` How do I use [insert] command?```
- ``` How do I find out what my python path is?```
- ``` How do I use winget to install a program in windows terminal?```
- ``` How do I run the python interpreter in windows terminal?```
- ``` How to I create a python script that I can run from windows terminal?```
- ``` How do I use the print function in python?```
- ``` How do I use the f-string in python?```
- ``` What are the different data types in python?```
- ``` How do I use [insert] data type in python?```
- ```  what are soe common evaluators in python?```
- ``` How do I use the if statement in python?```
- ``` How do I use the else statement in python?```
- ``` How do I check whether a list is empty in python?```
