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

On Problem 2, we use the same CSV file to get cars that apply to the certain conditions 

The first task was to get the first 5 rows of the data frame with odd-numbered columns.
``` python
odd = cars.iloc #using iloc, locates the index in the dataframe.
iloc[:, ::2] #the setup for the brackets in iloc is [rows, column]. The : is meant for rang,e which is why I put it on the rows section, then on the second section, it's was used to skip the index by 2
```

For the second task, it was asked to search for a certain row that has a specific Model. The model asked was the Mazda RX4.
The code I used was the 'loc' code because it locates through a certain category for the specific variable within it
``` python
cars.loc[cars['Model'] =='Mazda RX4'] #the code looks for the Mazda RX4 in the Model Category
```

For third task it was asked to find the car with the model of the Camaro Z28 and output its cylinder or 'cyl'
I also used the 'loc' code to locate the specific model: 
``` python
cars.loc[cars['Model']=='Camaro Z28' #this locates the Camaro Z28 on the model category
```
To output the cylinder, I used:
``` python
['cyl']] #This indicate what would be output if you run the code.
```

All together:
``` python
cars.loc[cars['Model']=='Camaro Z28', ['cyl']]
```
cars.loc[[1,28,18],['Model','cyl','gear']] #searches for the cars by their index in the data frame and outputs their Model, cyl, and gear.
```
