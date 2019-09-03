#!/usr/bin/env python
# coding: utf-8

# In[24]:


from numpy import random


# In[25]:


import operator


# In[2]:


import numpy as np


# In[3]:


# uniform random numbers in [0,1]


# In[4]:


dataOne = random.rand(5,5)


# In[5]:


np.mean(dataOne)


# In[6]:


varOne = 25


# In[7]:


varTwo = 25.0


# In[9]:


varThree = varOne + varTwo


# In[10]:


print(varThree)


# In[11]:


varTwo = 'Hello'


# In[13]:


varThree = str(varOne) + varTwo


# In[14]:


print(varThree)


# In[15]:


listOne = [1,2,3,4]


# In[16]:


print(listOne[1:3])


# In[17]:


tel = {'jack': 4098, 'sape': 4139}


# In[18]:


tel['jack']


# In[21]:


growthhRatePercentageofUSAByYear = {'2006': 2.59, '2007': 1.97, '2008': -2.75, '2009': 0.18, '2010': 2.57, '2011': 1.61, '2012': 1.47, '2013': 2.61, '2014': 2.88, '2015': 1.90,'2016': 2.03, '2017': 2.80, '2018': 2.52}


# In[27]:


print "Max growth rate in last 15 years : ", max(growthhRatePercentageofUSAByYear.iteritems(), key=operator.itemgetter(1))[0]


# In[28]:


print "Min growth rate in last 15 years : ", min(growthhRatePercentageofUSAByYear.iteritems(), key=operator.itemgetter(1))[0]


# In[59]:


for k, v in growthhRatePercentageofUSAByYear.items():  print("Code : {0}, Value : {1}".format(k, v)) 


# In[65]:


[float(growthRates) for growthRates in growthhRatePercentageofUSAByYear.values()] 


# In[77]:


print "Avergage growth rate in last 15 years : ", np.mean(growthRates)


# In[ ]:




