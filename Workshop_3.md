# Workshop 3 [Wed 14FEB 1:30 PM]

## Working with Data
- Dataframes

- Operations on Dataframes
- Apply functions

## Data Visualization
- Matplotlib

## Data Analysis

- Peak Picking
- Curve Fitting

## A whistle-stop tour of other useful libraries
- OpenCV
- tkinter
- Sympy
- threading
- multiprocessing

# Data Visualisation

The most common way to visualise data in Python is with the Matplotlib library. This is a very powerful library that allows you to create a wide range of plots and graphs.

Matplotlib, however, is one of the most complex libraries to use in Python. (some of the syntax is very strange).
## Matplotlib

### Setting up a plot

The most basic plot is a line plot. To create a line plot you need to provide a list of x values and a list of y values.
From last weeks homework, we have some data that we can plot.

```python
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Import a folder as a path object
path = Path('./data')

files = {i.stem: pd.read_csv(i) for i in path.glob('*.txt')}

file = files['data1']
# Create a plot
plt.plot(file['x'], file['y'])
plt.show()
```

This way uses a lot of the default settings for the plot, but generally works.

What if we want to plot all of the data on the same plot?

```python
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Import a folder as a path object
path = Path('./data')

files = {i.stem: pd.read_csv(i) for i in path.glob('*.txt')}

# Create a plot
for file in files.values():
    plt.plot(file['x'], file['y'], label=file)
plt.show()
# add a legend
plt.legend()
```
If we want to plot the data on separate plots, we can use the `plt.subplots()` function.

```python
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Import a folder as a path object
path = Path('./data')

files = {i.stem: pd.read_csv(i) for i in path.glob('*.txt')}
# Create a plot
fig, axes = plt.subplots()
for file in files.values():
    axes.plot(file['x'], file['y'], label=file)
plt.show()
# add a legend
plt.legend()
```

Note in the above example, we have used the `plt.subplots()` function to create a figure and axes object. This is a more flexible way to create plots, as it allows you to create multiple plots on the same figure.

When we use matplotlib, we tend to use a lot of methods. 
plt.plot() creates two objects, a figure and an axes object.
The two different objects have different methods associated with them - so be aware of which object you are using. You will find you're ofent trying to do something with an axes object that only works on a figure object.


| objective 1 | Plot up the data from last week's homework |
|-------------|---------------------------------------------|


### Customising a plot

There are a lot of different ways to customise a plot. The most common ones are:

- Changing the axis limits
- Changing the axis labels
- Changing the plot title
- Changing the plot legend
- Changing the plot colours
- Changing the plot line style
- Changing the plot marker style
- Changing the plot marker size

documentation for plot styles can be found here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html


```python
```python
plt.plot(file['x'], file['y'], label=file, color='red', linestyle='--', marker='o', markersize=10)
```

You are also not limited to plotting lines. You can plot points, bars, histograms, and many other things.
you can find a full list of plot types here: https://matplotlib.org/stable/plot_types/index.html

| objective 2 | Customise the plot from objective 1 |
|-------------|-------------------------------------|

# Exporting the plot

Once you have created a plot, you will want to export it. There are many different ways to do this, but the most common way is to use the `plt.savefig()` function.

```python
plt.savefig('plot.png')
```
You may want to save it as an svg which is openable in inkscape. this is very similaer, but you need to add a line to make the text editable in inkscape.

```python   
rcParams['svg.fonttype'] = 'none'
plt.savefig('plot.svg')
```
If you have lots of plots or plots in a loop, you may want to save them with a different name each time. You can do this by using the `plt.savefig()` function with a variable name (using an f-string).

```python
for i in list_of_plots:
    plt.savefig(f'plot_{i}.png')
```



## Common DataFrame Operations in Pandas

1. **Viewing Data**: View the first n rows with `df.head(n)` and the last n rows with `df.tail(n)`.
    ```python
    df.head(5)
    df.tail(5)
    ```

2. **Selecting Data**: Select a single column by its name (`df['column_name']`), multiple columns (`df[['column1', 'column2']]`), or rows by their index (`df[5:10]`).
    ```python
    df['column_name']
    df[['column1', 'column2']]
    df[5:10]
    ```

3. **Filtering Data**: Filter rows based on a condition.
    ```python
    df[df['column_name'] > 50]
    ```

4. **Modifying Data**: Add new columns or modify existing ones.
    ```python
    df['new_column'] = df['column1'] + df['column2']
    ```

5. **Aggregating Data**: Perform operations like sum, average, max, min on a column or a set of columns.
    ```python
    df['column_name'].sum()
    df[['column1', 'column2']].mean()
    ```

6. **Grouping Data**: Group data based on values in one or more columns and then perform aggregate functions on the grouped data.
    ```python
    df.groupby('column_name').mean()
    ```

7. **Merging Data**: Merge two dataframes based on a common column.
    ```python
    pd.merge(df1, df2, on='common_column')
    ```

8. **Sorting Data**: Sort data by one or more columns.
    ```python
    df.sort_values(by='column_name')
    ```

9.  **Handling Missing Data**: Drop rows with missing data or fill them with a specific value.
    ```python
    df.dropna()
    df.fillna(value)
    ```

11. **Concatenating Data**: Concatenate two or more dataframes along a particular axis.
    ```python
    pd.concat([df1, df2])
    ```
This will concatenate `df1` and `df2` along the rows (axis=0). If you want to concatenate them along the columns, you can specify `axis=1`:

    ```python
    pd.concat([df1, df2], axis=1)
    ```
| objective 3 | Filter your data to a certain time range |
|-------------|------------------------------------------|


## Custom Datafram manipulations

### using df.apply()

The apply function allows you to apply a function to a dataframe. This is useful if you want to apply a function to each row or column of a dataframe.

```python
import pandas as pd
import numpy as np

# generate a random dataframe
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))

def add_one(x):
    return x + 1
    
result = df.apply(add_one)
```
In the above example, we have created a function that adds one to a number. We then use a list comprehension to apply this function to each value in the column 'A'.

### applying to one column
```python
df['A'] = df['A'].apply(add_one)
```

| objective 4 | Apply a function to a dataframe |
|-------------|---------------------------------|


## Peak Picking

Peak picking is a common task in data analysis. It is used to find the peaks in a dataset. This is useful for finding the maximum value in a dataset, or for finding the peaks in a spectrum.

There are many different ways to do peak picking. We will use scipy's `find_peaks` function.

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.signal as signal

# generate a random dataframe with two peaks

x = np.linspace(0, 10, 1000)
y = np.sin(x) + np.sin(2*x)

df = pd.DataFrame({'x': x, 'y': y})

# find the peaks
peaks, _ = signal.find_peaks(df['y'], height=1)

# plot the data
plt.plot(df['x'], df['y'])

# plot the peaks
plt.plot(df['x'][peaks], df['y'][peaks], 'x')

plt.show()
```

## Curve Fitting

Curve fitting is a common task in data analysis. It is used to find the best fit for a set of data points.

There are many different ways to do curve fitting. We will use scipy's `curve_fit` function.

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# generate a random dataframe with an exponential decay

x = np.linspace(0, 10, 1000)
y = np.exp(-x)

df = pd.DataFrame({'x': x, 'y': y})

# add some noise to the y data
df['y'] = df['y'] + np.random.normal(0, 0.1, len(df['y']))


# define the function to fit
def func(x, a, b):
    return a * np.exp(-b * x)

# fit the data
popt, pcov = curve_fit(func, df['x'], df['y'])

# plot the data
plt.plot(df['x'], df['y'])

# plot the fit
plt.plot(df['x'], func(df['x'], *popt), 'r-')

plt.show()
```
Once again, it is worth looking through the documentation for the `curve_fit` function to see what options are available.
This can be found here: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html


| objective 5 | either peak pick or curve fit your data |
|-------------|-----------------------------------------|

# A tour of other useful libraries

## OpenCV

OpenCV is a library for computer vision. It is used for image processing, object detection, and many other things.

## tkinter

tkinter is a library for creating graphical user interfaces. It has a simplistic syntax, allowing you to arrange widgets in a grid layout or a pack layout which optimises the space available on the screen.

## Sympy

Sympy is a library for symbolic mathematics. It allows you to perform symbolic calculations, such as solving equations, finding derivatives et.
It's really nice for drawing matrices and other mathematical objects.
It's particularly useful when used with Jupyter notebooks.

## threading

Threading is a library for creating threads. It allows you to run multiple tasks at the same time, which can be useful for GUI applications as you can run the GUI on one thread and calculations on another thread.

## multiprocessing

Multiprocessing allows you to split your code into multiple processes. This can be useful for running multiple calculations at the same time, or for running calculations on multiple cores. For insance (roughly), if you have a list of 100 items you want to perform a calculation on, you can split the list into 4 lists of 25 items and run the calculation on each list in parallel. This will be faster than running the calculation on each item in the list sequentially.

# GIT

GIT is a version control system. It allows you to track changes to your code, and revert back to previous versions if you make a mistake.
It also allows you to collaborate with other people on the same code base.
If two people make changes to the same file, GIT will try to merge the changes together. If it can't, it will tell you that there is a conflict and you will have to manually merge the changes.

There are many implementations of GIT. The most common one is GitHub, which is a website that hosts your code and allows you to collaborate with other people.

To learn more about GitHub, you can read the documentation here: https://docs.github.com/en/github/getting-started-with-github


Github is usually used with a command line interface, but there are also GUIs available. GitHub is integrated into VSCode, so you can use it to push and pull changes to your code. 

# Homework
Find a dataset from your day-to-day work and plot it up. Also conduct some basic analysis on the data. This could be peak picking, curve fitting. Output the data in a useful format.