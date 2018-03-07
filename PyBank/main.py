
# coding: utf-8

# In[1]:

# import systems
import os
import pandas as pd


# In[184]:

# Reas CSV
bankfile = pd.read_csv("budget_data_1.csv")



# In[29]:

# find total number of months in dataset
totalmonths = bankfile["Date"].nunique()
totalmonths


# In[198]:

# find total revenue amount
totalrev = bankfile["Revenue"].sum()
totalrev


# In[186]:

# find revenue change month over month
for i in range(1,len(bankfile)):
    print((bankfile.loc[i,"Revenue"] -bankfile.loc[i-1,"Revenue"]))
    bankfile.loc[i,"Change"] = bankfile.loc[i,"Revenue"] -bankfile.loc[i-1,"Revenue"]


# In[316]:

# find lication of largest revenue change
Max_Indx = bankfile["Change"].idxmax()
Max_Indx


# In[303]:

# find value of largest revenue change
Max_Change = bankfile["Change"].max()
Max_Change


# In[317]:

# find corresponding date for largest revenue change
Max_Date = bankfile["Date"][Max_Indx]
Max_Date


# In[309]:

# find location of smallest revenue change
Min_Indx = bankfile["Change"].idxmin()
Min_Indx


# In[310]:

# find value of smallest revenue change
Min_Change = bankfile["Change"].min()
Min_Change


# In[318]:

# find corresponding date for smallest revenue change
Min_Date = bankfile["Date"][Min_Indx]
Min_Date


# In[269]:

# find average revenue change
AvgChange = bankfile["Change"].mean()
AvgChange


# In[319]:

# print summary
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(totalmonths))
print("Total Revenue: " + str(totalrev))
print("Average Revenue Change: " + str(AvgChange))
print("Greatest Increase in Revenue: " + str(Max_Date) + " " + str(Max_Change))
print("Greatest Decrease in Revenue: " + str(Min_Date) + " " + str(Min_Change))

