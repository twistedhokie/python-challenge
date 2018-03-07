
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[184]:


bankfile = pd.read_csv("budget_data_1.csv")
bankfile2 = pd.read_csv("budget_data_2.csv")
bankfile


# In[29]:


totalmonths = bankfile["Date"].nunique()
totalmonths


# In[198]:


totalrev = bankfile["Revenue"].sum()
totalrev


# In[186]:


bankfile_copy = bankfile
bankfile


for i in range(1,len(bankfile)):
    print((bankfile.loc[i,"Revenue"] -bankfile.loc[i-1,"Revenue"]))
    bankfile.loc[i,"Change"] = bankfile.loc[i,"Revenue"] -bankfile.loc[i-1,"Revenue"]


# In[188]:


bankfile


# In[316]:


Max_Indx = bankfile["Change"].idxmax()
Max_Indx


# In[303]:


Max_Change = bankfile["Change"].max()
Max_Change


# In[317]:


Max_Date = bankfile["Date"][Max_Indx]
Max_Date


# In[309]:


Min_Indx = bankfile["Change"].idxmin()
Min_Indx


# In[310]:


Min_Change = bankfile["Change"].min()
Min_Change


# In[318]:


Min_Date = bankfile["Date"][Min_Indx]
Min_Date


# In[269]:


AvgChange = bankfile["Change"].mean()
AvgChange


# In[319]:


print("Financial Analysis")
print("------------------")
print("Total Months: " + str(totalmonths))
print("Total Revenue: " + str(totalrev))
print("Average Revenue Change: " + str(AvgChange))
print("Greatest Increase in Revenue: " + str(Max_Date) + " " + str(Max_Change))
print("Greatest Decrease in Revenue: " + str(Min_Date) + " " + str(Min_Change))

