# %%
import pandas as pd

# %%
cars = pd.read_csv('cars.xls')
cars

# %%
odd = cars.iloc[:, ::2]
odd.head()

# %%
cars.loc[cars['Model']=='Mazda RX4']

# %%
cars.loc[cars['Model']=='Camaro Z28', ['cyl']]

# %%
cars.loc[[1,28,18],['Model','cyl','gear']]


