---
layout: post
title: Pandas - A primer. How I used it for my first project.
category: Tech
tags: [COde, Pandas, Python]
---

Here I am using [IPython](https://ipython.org/) to run [Pandas](http://pandas.pydata.org/).

If you are using windows I would suggest, you install [Anaconda](https://www.continuum.io/downloads).
It will install all the required libraries to get you started with pandas for your data analysis project.

### Import pandas
First and foremost you would need to import pandas into your script.

```python
import pandas as pd
```

### Read a comma separated file
Next you can load a data set saved as a comma separated file (.csv) using

```python
df = pd.read_csv('datafile.csv')
```

I prefer csv format as it is the vanilla format and if need arises you use a simple text editor to peruse it. 

Pandas uses data frame to store the data in memory, similar to R.

In this blog ```df``` will be used to denote the variable is a data frame.

### Display stats
Displays stats of the data.

```python
matdf.describe()
```

### Print all the column names
Prints all the variables in the data frame

```python
df.columns.values
```

### Display the start and end of the data frame
Displays the first and the last 'n' rows in a data frame respectively.
'n' equals 5 by default.

```python
matdf.head(n)<br>
matdf.tail(n)
```

### Concatenate two data frames
Concatenates 2 data frames along the requires axis.
When axis equals 0, more observations are added to the resulting data frame.
When axis equals 1, more variables (dimensions) are added to the resulting data frame.
A good explanation can be found [here](http://stackoverflow.com/questions/25773245/ambiguity-in-pandas-dataframe-numpy-array-axis-definition).

```python
df = pd.concat([df1, df2], axis=1)
```

### Unique values in a column
To display the unique values in a column.
Good to see different values of an ordinal variable.

```python
df.columnName.unique()
```

### To make a data frame from arrays
Simplest way to create a data frame

```python            
pd.DataFrame([[1.0,2.0],[3.0,4.0]], columns=['a', 'b'])
```

### Drop a column
To delete a column

```python
df.drop('columnName', axis = 1)
```

### Set a column as index
Allows you to label rows using an already present column.

```python
matdf = df.set_index('columnName')
```

### Select conditionally
loc command allows you to select rows (indices) from column2 and substitute them with value2, that equals a condition to the values in column1. 
Note: columnName1 and columnName2 can be the same column name.

```python
df.loc[df['columnName1'] == value1,'columnName2'] = value2
```

### Get a subset of data frame
Get a stat from a column for only those rows (indices) where the conditions are satisfied in one or more columns.

```python
df.columnName3[(df.columnName1 == value1) & 
               (df.columnName2 == value2 )].mean()
```

### Write a data frame to csv
After you preprocess the data you might want to save it to the disk.
to_csv function comes in handy to save a data frame as a csv file,

```python
matdf.to_csv('matYearCountry.csv')
```

Lastly,

### Run a IPython notebook in a IPython notebook

```python
%run ipynbName.ipynb'
```
