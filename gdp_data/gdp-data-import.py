
# coding: utf-8

# Importing the GDP csv file (of cleaned data)

# In[1]:

import csv


# In[9]:

with open('gdp-data-cleaned.csv',newline='') as csvfile:
    gdpreader=csv.reader(csvfile,delimiter=',',quotechar='|')
    for row in gdpreader:
        print(', '.join(row))


# first row is a header row,
# first column is country name,
# second column is country code. 
# 
# import these into a usable dataset structure

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



