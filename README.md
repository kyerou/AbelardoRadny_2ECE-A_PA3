# ECE2112 PA3

<b> PANDAS <b>

In this problem assignment, we were given a CSV file that contains a data frame of cars and their attributes. Our task was to narrow down the data frame to a specific condition needed.

# PROBLEM 1

The first task was to load the said CSV file
``` python
cars = pd.read_csv('cars.xls') #reads the cars.xls file into the python code
```

The next task was to get the first and last five rows of the data frame.

I used: 
```python
cars.head() #To get the first five rows of the dataframe
cars.tail() #To get the last five rows of the dataframe
```

# PROBLEM 2
``` python
odd = cars.iloc[:, ::2] #gets the every odd column of the data frame. the first : was the range of the entire data frame while the ::2 ranges of the column that skips one column
cars.loc[cars['Model']=='Mazda RX4'] #the code searches for the Mazda RX4 that was located in the model category
cars.loc[cars['Model']=='Camaro Z28', ['cyl']] #the code searches for the Camaro Z28 in the model category and output its cylinders using ['cyl']
cars.loc[[1,28,18],['Model','cyl','gear']] #searches for the cars by their index in the data frame and outputs their Model, cyl, and gear.
```
