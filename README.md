<b> PANDAS <b>


P1
``` python
import pandas as pd #importing pandas into the Python code as pd
cars = pd.read_csv('cars.xls') #reads the cars.xls file into the python code
cars.head() #gets the first 5 rows of the entire data frame
cars.tail() #gets the last 5 rows of the data frame
```

P2
``` python
odd = cars.iloc[:, ::2] #gets the every odd column of the data frame. the first : was the range of the entire data frame while the ::2 ranges of the column that skips one column
cars.loc[cars['Model']=='Mazda RX4'] #the code searches for the Mazda RX4 that was located in the model category
cars.loc[cars['Model']=='Camaro Z28', ['cyl']] #the code searches for the Camaro Z28 in the model category and output its cylinders using ['cyl']
cars.loc[[1,28,18],['Model','cyl','gear']] #searches for the cars by their index in the data frame and outputs their Model, cyl, and gear.
```
