
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


csv_path = "election_data_1.csv"
polldata = pd.read_csv(csv_path)
polldata.head()


# In[4]:


totalvotes = polldata["Voter ID"].nunique()
totalvotes


# In[5]:


candidate_votes = polldata["Candidate"].value_counts()
candidate_votes


# In[11]:


new_df = pd.DataFrame(candidate_votes)
new_df


# In[13]:


percentages = (candidate_votes / totalvotes)
percentages


# In[14]:


summary_table = pd.DataFrame({"Percentage" : (percentages*100), "Total Votes" : candidate_votes})
summary_table


# In[15]:


winner = summary_table["Total Votes"].idxmax()
winner


# In[17]:


print("Election Results")
print("----------------")
print(summary_table)
print("----------------")
print("Winner: " + str(winner))

