#!/usr/bin/env python
# coding: utf-8

# This notebook will be used to complete the coursera capstone project- BATTLE OF NEIGHRBOURHOODS. Till now I have linked my hardware to github and have learnt few git codes :)

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


print("Hello Capstone Project Course!")


# ### WEB SCRAPING USING PANDAS

# In[3]:


import pandas as pd


# In[4]:


webscrap = pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# In[5]:


type(webscrap)


# In[6]:


len(webscrap)


# In[7]:


#webscrap[0]
print("there are 3 tables, we require webscrap[0] i.e first table ")


# In[8]:


df= webscrap[0]


# In[9]:


df.shape


# In[10]:


df.head()


# deleting NOT ASSIGNED VALUED Rows

# In[11]:


df.drop(df[df['Borough']=='Not assigned'].index, inplace = True)


# In[12]:


df.head(20)


# In[13]:


df.loc[df['Neighborhood']=='Not assigned']


# In[14]:


df.head()


# In[15]:


df.index


# In[16]:


df.iloc[5].Neighborhood="Queen's Park"


# In[17]:


df.head(12)


# splitting into 2 dataframes dfa and dfb ;
# dfa -> postcode + neighbourhood;
# dfb -> postcode + borough;
# I work on them individually and then merge them 

# In[18]:


dfb=df[['Postcode','Borough']]
dfb.head()


# In[19]:


dfb = dfb.drop_duplicates( subset= 'Postcode', keep='first')


# In[20]:


dfb.head()


# In[21]:


dfb.set_index('Postcode', inplace= True)


# In[ ]:





# In[ ]:





# In[22]:


dfa=df[['Postcode','Neighborhood']]


# In[23]:


dfa.head()


# In[24]:


#t=df_try.groupby(df_try['Postcode']).sum(df_try['Neighborhood'])
dfa=dfa.groupby('Postcode').sum()


# In[25]:


dfa.head()


# merging dfa and dfb

# In[26]:


df_new = pd.merge(dfa, dfb,how='left', on='Postcode')


# In[27]:


df_new.head(10)


# In[28]:


df_new=df_new[['Borough','Neighborhood']]


# In[31]:


df_new.head()


# In[34]:


df_new.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




