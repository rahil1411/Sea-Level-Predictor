#!/usr/bin/env python
# coding: utf-8

# In[172]:


import numpy as np
import pandas as pd 
import matplotlib as mp
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

#from scipy.stats import linregress
from scipy import stats


# In[173]:


df  = pd.read_csv('flat-ui__data-Sun Jun 16 2024.csv')


# In[174]:


df


# In[175]:


df.head()


# In[176]:


df = df.drop(df[df['Year']==2014].index)


# In[177]:


df


# In[178]:


df.describe()


# In[186]:


x = df['Year']
y = df['CSIRO Adjusted Sea Level']
plt.scatter(x,y,s = 10)
l = stats.linregress(x,y)
fit_line = (x*l.slope) + l.intercept 
plt.plot(x,fit_line, c = 'red')
plt.show()


# In[185]:


years_extended = np.arange(1880, 2050, 1)
x = df['Year']
y = df['CSIRO Adjusted Sea Level']
plt.figure(figsize = (100,50))
plt.scatter(x,y,s =500)
l = stats.linregress(x,y)
#fit_line = (x*l.slope) + l.intercept
#plt.plot(x,fit_line, c = 'red',lw=10)

plt.xticks(range(1880, 2051, 1))



line = [l.slope*x + l.intercept for x in years_extended]

plt.plot(years_extended, line, color = 'orange', label="Fitting Line", linewidth=10)
#plt.scatter(x, y, s = 5, marker = '.', label="Sample Point", color = 'dodgerblue')
plt.xticks(range(1880, 2051, 1))

plt.xlabel('Year')
plt.ylabel('Sea level(inches)')
plt.show()


# In[154]:


df


# In[187]:


data = df.drop(df[df['Year']<2000].index )


# In[188]:


data


# In[170]:


a = data['Year']
b = data['CSIRO Adjusted Sea Level']
plt.figure(figsize = (100,50))
plt.scatter(a,b,s =500)
l = stats.linregress(a,b)
#fit_line = (x*l.slope) + l.intercept
#plt.plot(x,fit_line, c = 'red',lw=10)

plt.xticks(range(2000,2051,1))



line = [l.slope*a + l.intercept for a in years_extended]

plt.plot(years_extended, line, color = 'orange', label="Fitting Line", linewidth=10)
#plt.scatter(x, y, s = 5, marker = '.', label="Sample Point", color = 'dodgerblue')
plt.xticks(range(2000, 2051, 1))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




