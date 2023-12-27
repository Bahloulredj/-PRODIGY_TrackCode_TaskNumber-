#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
tsk2=pd.read_csv(r"C:\Users\amina\Desktop\projects_DATA_science\titanic\train.csv")
tsk2.head()


# In[44]:


tsk2.info()


# In[45]:


tsk2.isnull().sum()


# In[46]:


tsk2['SibSp'].value_counts(dropna=False)


# In[47]:


tsk2['Cabin'].value_counts(dropna=False)


# In[48]:


tsk2['Embarked'].value_counts(dropna=False)


# In[49]:


tsk2['Parch'].value_counts(dropna=False)


# In[50]:


tsk2['Name'].value_counts(dropna=False)


# In[51]:


tsk2['PassengerId'].value_counts(dropna=False)


# In[52]:


tsk2.describe().T


# In[53]:


Tsk2=tsk2.drop(['Cabin'], axis=1)


# In[54]:


Tsk2.info()


# In[55]:


Tsk2['Age'].fillna(Tsk2['Age'].mean(), inplace = True)
Tsk2['Fare'].fillna(Tsk2['Fare'].mean(), inplace = True)
Tsk2['Embarked'].fillna(Tsk2['Embarked'].mode()[0], inplace = True)
Tsk2.info()


# In[56]:


Tsk2.isnull().sum()


# In[57]:


Tsk2.drop_duplicates()


# #  Exporting our new data to csv file under name Tsk2

# In[61]:


Tsk2.to_csv(r'C:\Users\amina\Desktop\projects_DATA_science\titanic\Tsk2.csv')

