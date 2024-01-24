#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


df= sns.load_dataset("car_crashes")


# In[3]:


df


# In[4]:


df.abbrev.unique()


# In[5]:


df.head()


# In[6]:


sns.lineplot(x='alcohol', y='speeding', data=df, ci=None) #Confidence interval
plt.show()


# In[7]:


sns.lineplot(x='alcohol', y='speeding', data=df, hue='abbrev', ci=None)
plt.show()


# In[8]:


sns.scatterplot(x='alcohol',y='speeding',data=df, )
plt.title("Scatter plot")
plt.show()


# In[9]:


sns.scatterplot(x='alcohol',y='speeding',data=df, hue='abbrev')
plt.title("Scatter plot")
plt.show()


# In[10]:


df.head()


# In[11]:


sns.barplot(x='alcohol', y='speeding', data=df)
plt.show()


# In[12]:


sns.boxplot(x='alcohol',data=df)
plt.show()


# In[13]:


sns.boxplot(x='speeding', y='alcohol', data=df)
plt.show()


# In[14]:


sns.stripplot(x='alcohol', y='speeding', data=df)
plt.show()


# In[16]:


sns.histplot(x='alcohol', data=df)
plt.show()


# In[17]:


sns.histplot(x='alcohol', data=df,hue='abbrev', kde=True) # kernel density estimation 
plt.show()


# In[18]:


sns.distplot(df['alcohol'],color="g") # ,hist=False, kde=False
plt.show()


# In[19]:


sns.pairplot(data=df, hue='abbrev')
plt.show()


# In[20]:


#categorical plot
sns.catplot(x='alcohol',data=df,kind='violin')
plt.show()


# In[21]:


sns.catplot(x='alcohol',y='speeding',data=df, kind='swarm')
plt.show()


# In[22]:


#bar plot
sns.barplot(x='alcohol',y='speeding',data=df)
plt.show()


# In[23]:


#box plot
sns.boxplot(x='alcohol',y='speeding',data=df)
plt.show()


# In[24]:


#violnplot
sns.violinplot(x='alcohol', y='ins_premium', data=df)
plt.show()


# In[25]:


sns.stripplot(x='alcohol',y='speeding',data=df)
plt.show()


# In[26]:


#catplot
sns.catplot(x='alcohol',y='speeding',data=df)
plt.show()


# In[ ]:




