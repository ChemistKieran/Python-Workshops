Workshop 4 [Wed 28FEB 1:30PM]

      Review of topics

An Introduction to GIT

- Git push/pull requests
- GIT IDE integration

A view to workshop 5 and beyond (discussed but not covered in detail)

- Using more packages
- Classes and Objects
- Threading and Multiprocessing
- Callbacks and Application Design
- Interfacing with hardware (I2C)
- Other 'diet' languages:
    - Markdown
    - HTML + css
    - LaTeX


# GIT

GIT is a version control system. It allows you to track changes to your code, and revert back to previous versions if you make a mistake.
It also allows you to collaborate with other people on the same code base.
If two people make changes to the same file, GIT will try to merge the changes together. If it can't, it will tell you that there is a conflict and you will have to manually merge the changes.

There are many implementations of GIT. The most common one is GitHub, which is a website that hosts your code and allows you to collaborate with other people.

To learn more about GitHub, you can read the documentation here: https://docs.github.com/en/github/getting-started-with-github


Github is usually used with a command line interface, but there are also GUIs available. GitHub is integrated into VSCode, so you can use it to push and pull changes to your code. 



# Threading example

Callbacks are a way of passing functions as arguments to other functions. This is useful for designing applications that need to run multiple functions at the same time.

For example, if you want to run a function that takes a long time to complete, you can pass a callback function to it so that it can run in the background while you do other things.

We will start with a very simple first example.
```python
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulate some time-consuming task
        print(f"Thread 1: {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)  # Simulate some time-consuming task
        print(f"Thread 2: {letter}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
```
Now lets try something a bit more complicated. Here we are runnig a matplotlib plot and exploiting the plt.pause() function to update the plot.

Meanwhile we are spinning up a thread and using it to generate a moving sine wave in the background. This is updating a global variable.

``` python
import threading
import time
import numpy as np
import matplotlib.pyplot as plt

# Global variables for shared data
x_data = np.arange(0, 10, 0.1)
y_data = np.zeros_like(x_data)


# Function to generate data in the background
def generate_data():
    global y_data
    counter = 0
    while True:
        y_data = np.sin(x_data + counter)  # Use counter to create a moving sine wave
        counter += 0.1  # Increment counter for the next iteration
        time.sleep(0.1)  # Simulate some time-consuming data generation

# Create and start the threads with daemon=True

data_thread = threading.Thread(target=generate_data, daemon=True)
data_thread.start()

try:
    while True:
        plt.clf()  # Clear the previous plot
        plt.plot(x_data, y_data, label='Data')
        plt.title('Updating Plot with Threading')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.pause(0.1)  # Pause to allow the plot to update
except KeyboardInterrupt:
    print('Plotting interrupted by user')
    plt.close()

```


Note that the above example uses try/except to catch a KeyboardInterrupt. This is because the plt.pause() function is blocking, so the program will not exit when you press Ctrl+C. Instead, you have to press Ctrl+C twice to exit the program.

we haven't covered try/except yet.
The way these work is that you put the code that you want to run in the try block, and then you put the code that you want to run if an exception is raised in the except block. This is not something you will interact with very often, but it is useful to know about.


# callbacks 

Callbacks are a way of passing functions as arguments to other functions. This is useful for designing applications that need to run multiple functions at the same time.

Here is a basic example of the use of a callback:
```python
def callback_function():
    print("Callback function called")

def main_function(callback):
    print("Main function called")
    callback()

main_function(callback_function)

```

We won't go into too much detail about how callbacks work, but it is important to understand the concept. If you want to learn more about callbacks, you can read the documentation here: https://docs.python.org/3/library/asyncio-task.html#asyncio.loop.call_soon 


# Classes and Objects

Clasees and objects are also not something we will cover in detail, but it is important to understand the concept. If you want to learn more about classes and objects, you can read the documentation here: https://docs.python.org/3/tutorial/classes.html

These are closely intertwined with a property called inheritance, which is a way of creating new classes from existing ones. It beccomes useful when you are carrying out several similar tasks but need to change one or two things about each task.
For instance, you have a piece of software that has several buttons on it. Each button does something different, but they all have the same basic functionality.

For basic data science you don't need to worry about classes and objects, but they are useful to know about if you want to do more advanced programming.

# Interfacing with hardware (e.g. I2C)

In every lab, you will have many different pieces of equipment that you need to interface with. For instance, a power supply. These are not intelligent machines, but we can still 'talk' to them. The most common way of doing this is through a protocol called I2C. (Roughly) you have your computer which is connected to your instrument via a wire. Along the wire your computer will send a signal, such as 'How many volts are you reading?' and the power supply will send back a signal, such as 'I am reading 5V'. Whats actually happening is that your computer is sending a series of 1s and 0s (or high and low voltages). These are bits and bytes and they can be literally translated to plane english. So in reality, your computer wil send "VOLTS?" and the power supply will send back "5V". 

Fortunately we dont have to manually translate bits and bytes as there are several libraries that do this for us. The most common one is called pyvisa. This is a python library that allows you to communicate with instruments using the I2C protocol. More information can be found here: https://pyvisa.readthedocs.io/en/latest/

# Other languages I find useful

## Markdown
This workshop is written in markdown. Similarly, Jupyter notebooks use markdown.
Wikipedia and GitHub readme files are also written in markdown.
It is a markup language that is designed to be easy to read and write. We don't code in it but it makes writing really effortless. 

some syntx examples:
```markdown
# This is a heading
## This is a subheading
### This is a sub-subheading

This is a paragraph. It is separated from the heading by a blank line.

This is a new paragraph.

This is a list:
- Item 1
- Item 2
- Item 3

This is a numbered list:
1. Item 1
1. Item 2
1. Item 3

This is a link to [Google](https://www.google.com)

This is a link to a local file [Workshop_4.md](Workshop_4.md)

This is an image:
![This is the alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png)

you can also use html tags:
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png" width="200">

```
# LaTeX
LaTeX is used for typesetting PDF documents. It is very useful for writing reports and papers. You will also see it's equation writing abilities borrowed by many other pieces of software. LaTeX could be a workshop in itself, but here are some examples of what it can do:

```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{siunitx}

\begin{document}

\section{Introduction}

This is a section.

\subsection{Subsection}

This is a subsection.

\subsubsection{Subsubsection}

This is a subsubsection.


\section{Equations}

This is an equation:
\begin{equation}
    \frac{d}{dx} \left( \int_{0}^{x} f(u) \, du\right)=f(x)

\end{equation}

\section{Tables}

This is a table:

\begin{table}[h]
    \centering
    \begin{tabular}{|c|c|c|}
        \hline
        \textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
        \hline
        1 & 2 & 3 \\
        \hline
        4 & 5 & 6 \\
        \hline
        7 & 8 & 9 \\
        \hline
    \end{tabular}
    \caption{This is a table}
    \label{tab:my_label}

\end{table}

\section{Figures}

This is a figure:

\begin{figure}[h]
    \centering
    \includegraphics[width=0.5\textwidth]{example-image-a}
    \caption{This is a figure}
    \label{fig:my_label}
\end{figure}


\section{Citations}

This is a citation \cite{einstein}.

\bibliographystyle{plain}

\bibliography{references}

\end{document}
```
# HTML + CSS
HTML is used to create web pages. CSS is used to style them. This one is a rabbit hole as there are soo many permutations which make syling pages easier or allow you to do various logic operations or to database various pieces of information.
Hoever the very basics are quite easy .

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>
    <style>
        body {
            background-color: lightblue;
        }
        h1 {
            color: white;
            text-align: center;
        }
        p {
            font-family: verdana;
            font-size: 20px;
        }
    </style>
</head>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>

</html>
```
```css
body {
    background-color: lightblue;
}
h1 {
    color: white;
    text-align: center;
}
p {
    font-family: verdana;
    font-size: 20px;
}
```
There are some great cheat-sheets online of you want to learn more. 
(just google html/css cheat sheet to see all of the availble options)