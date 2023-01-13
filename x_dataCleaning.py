import pandas as pd 
import numpy as np

#1) IMPORT Data set -------------------------1---------------------
data = pd.read_csv('./data-sets/car_fleet_sample.csv')

#2) IDENTIFY MISSING DATA -------------------2------------------------
# ISNULL is a powerful method used to help you FIND empty values in a table.


print(data) #OUTPUT- data in table format with Keys:Values 
print("--------------")

print(data.isnull()) #OUTPUT- data with Key:BooleanValue- if Value == UNDEFINED/NaN then Value=TRUE.   
print("--------------")
print(data.isnull().sum())#OUTPUT- returns all data columns and specifies which ones have UNDEFINED/NaN values
print("--------------")
# you have TWO choices when cleaning data 1) we DROP the Data 2) INPUT missing data

#3) DROP Data Columns ----------------------3------------------------------
removeColumns = ['vin'] #Specify columns to remove
data.drop(removeColumns, inplace =True, axis =1)#OUTPUT data without specified columns 
# 
# print(data)

#4 CUSTOM INPUT missing Data ---------------4-----------------------------
data['zeroSixty'] = data['zeroSixty'].fillna('Em9Ty')

print(data['zeroSixty'])
print("--------------")# 
# print(data)

#5 identify DUPLICATES ---------------------5------------------------------

print(data.duplicated()) #OUTPUT True/False
print("--------------")
#6 DROP_DUPLICATES() -----------------------6----------------------------

print(data.drop_duplicates())
print("--------------")
#) Detect outliers -------------------------7---------------------------
# this is data that is so far out that it is possibly a "misread"

print(data['year'].describe())
print("--------------")#now that we know what the outliers are we need to DECIDE what what the correct answer should be and address is manually. speak to the DATA set creator for more info on outlier.

#8) REPLACE outlier data --------------------8--------------------------
data.loc[2, 'year'] = 2012

print(data)
print("--------------")
# 9) Formatting Data/Values------------------9------------------
data['make'] = data['make'].str.lower()
data['model'] = data['model'].str.title()

print(data)
print("--------------")