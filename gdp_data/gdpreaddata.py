
# coding: utf-8

# In[154]:

import numpy as np


# Importing the GDP csv file (of cleaned data)

# In[155]:

import csv


# In[156]:

def readgdp():

    row_number = 0
    years=[]
    data=[]
    country=[]
    country_code = []

    with open('gdp-data-cleaned.csv',newline='') as csvfile:
        gdpreader=csv.reader(csvfile,delimiter=',',quotechar='|')
        for row in gdpreader:
            data_row_list_num=[]
            if row_number==0: # header row gives years in data
                years=row[2:]
            if row_number>0: # splitting rows into countrynames, countrycodes, and gdp data
                data_row_list_str=row[2:]
                data_row=[float(i) for i in data_row_list_str]
                country_row=row[0]
                country_code_row=row[1]
                data.append(data_row)
                country.append(country_row)
                country_code.append(country_code_row)
            row_number=row_number+1
    #print(data_row[1])
    #print(years)
    #print(data)
    #print(data[1])
    #print(country)
    #print(country_code)
           
    data_2=np.array(data) # convert data from list of floats to a numpy array
    #print(data_2)
    #print(data_2[3,2])
    
    return data_2 
    return years 
    return country 
    return country_code


# 

# In[181]:

#country='GBR'
    
def gdpdata_for_country(country):
    
    row_number = 0
    years=[]
    data=[]
    country=[]
    country_code = []

    with open('gdp-data-cleaned.csv',newline='') as csvfile:
        gdpreader=csv.reader(csvfile,delimiter=',',quotechar='|')
        for row in gdpreader:
            data_row_list_num=[]
            if row_number==0: # header row gives years in data
                years=row[2:]
            if row_number>0: # splitting rows into countrynames, countrycodes, and gdp data
                data_row_list_str=row[2:]
                data_row=[float(i) for i in data_row_list_str]
                country_row=row[0]
                country_code_row=row[1]
                data.append(data_row)
                country.append(country_row)
                country_code.append(country_code_row)
            row_number=row_number+1
            
    data_2=np.array(data)
    
    for i in range (0, len(country_code)):
        if country == country_code[i]:
            save_con = i
            
    data_for_country=data_2[save_con]
    return(data_for_country)
#print(data_for_country)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



