#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PROBLEM 1: 

#Utilizing this import convention to be able to access the Pandas Library
import pandas as pd

#This function will load the cars.csv dataset and will be stored on variable cars
cars = pd.read_csv('cars.csv')

#Using print function to display the dataset from cars.csv 
print("The Original Table is \n")
cars


# In[4]:


print("The First Five rows in the Original Table is: \n")

#This function will display only the first five rows from the dataset stored in cars
cars.head()


# In[6]:


print("The Last Five rows in the Original Table is: \n")

#This will display the last five rows froms the dataset 'cars.csv'
cars.tail()

