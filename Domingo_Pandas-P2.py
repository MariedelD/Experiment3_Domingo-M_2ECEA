#!/usr/bin/env python
# coding: utf-8

# In[6]:


#PROBLEM 2: 

#Utilizing this import convention to be able to access the Pandas Library
import pandas as pd

#This function will load the cars.csv dataset and will be stored on variable cars
cars = pd.read_csv('cars.csv')

#Using print function to display the dataset from cars.csv 
print("The Original Table is \n")
cars


# In[8]:


print("The First Five rows with Odd-Numbered Columns are: \n")

#This function First Five rows with Odd-Numbered Columns in the dataset
cars.loc[0:4, ::2]


# In[10]:


print ("The Row that contains the Model of Mazda RX4 is: \n")

#This function will locate at all rows from the cars Dataset where the value in the 'Model' column is equal to 'Mazda RX4
cars.loc[cars['Model'] == 'Mazda RX4']


# In[12]:


print("The number of Cylinders the car model 'Camaro Z28' have is: ")

#This function will locate at all rows from the cars Dataset where the value in the 'Model' column is equal to 'Mazda RX4 and will only display the Model name and the number of its cylinder
cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']]


# In[14]:


print("The number of cylinders and the gear type of the car model  ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have is: ")

#This code locates the 'Model', 'cyl', and 'gear' columns from the cars Dataset for rows where the 'Model' is 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L')|
         (cars['Model'] == 'Honda Civic') ,['Model','cyl','gear']]

