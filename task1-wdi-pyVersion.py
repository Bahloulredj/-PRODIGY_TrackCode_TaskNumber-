#!/usr/bin/env python
# coding: utf-8

# # cleansing data WDI

# In[82]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dataproj=pd.read_csv(r"C:\Users\amina\Desktop\projects_DATA_science\API_SP.POP.TOTL_DS2\API_SP.POP.TOTL_DS2.csv")


# In[83]:


dataproj.head()


# # checking the missing data with isna method
#        it returns a boolean values with 266 rows and 68 columns, this means that it has the same shape as our original data frame. Our data has a TRUE value which means we have a missing data. all of them are in the last columns (columns 68).
#        We can use the notna method which is exactly the reverse of isna Method. which means that it gives TRUE for the missing data.

# # Exploring the missing data with sum method
#     it returns the sum of the missing data of each columns.

# In[84]:


dataproj.isna().sum()


# # value_counts with argument "dropna"
#     by applying the value_counts method. This returns counts of the unique values within this column. By default, value_counts doesn't consider NaN, the missing value as a unique value. So to include missing value, we'll add the argument dropna=False. This setting won't dropna, which means it includes NaN as a unique value too.

# In[85]:


dataproj['1960'].value_counts()


# In[86]:


dataproj['1960'].value_counts(dropna=False)


# In[87]:


dataproj['1962'].value_counts(dropna=False)


# In[88]:


dataproj['Indicator Code'].value_counts(dropna=False)


# In[89]:


dataproj['Indicator Name'].value_counts(dropna=False)


# In[90]:


dataproj['Unnamed: 67'].value_counts(dropna=False)


# In[91]:


dataproj['Country Name'].value_counts()


# In[92]:


dataproj['Country Code'].value_counts()


# # checking the missing value by rows
#     all the rows contain one missing value. 266 values.

# In[93]:


num_missing_data_by_row=dataproj.isna().sum(axis=1)
num_missing_data_by_row>0


# In[94]:


(num_missing_data_by_row>0).sum()


# # examine the rows with a missing data
#     the result includes all the rows with sum missing value.

# In[97]:


num_missing_data_by_row>0


# In[98]:


num_missing_data_by_row>1


# In[99]:


df=dataproj.drop(['Unnamed: 67','Indicator Code','Indicator Name'], axis = 1)
df=df.dropna()
num_missing_data_by_row=df.isna().sum(axis=1)
num_missing_data_by_row>0


# In[100]:


df.info()


# In[102]:


df.to_csv(r"C:\Users\amina\Desktop\projects_DATA_science\API_SP.POP.TOTL_DS2\df.csv")


# In[103]:


df

