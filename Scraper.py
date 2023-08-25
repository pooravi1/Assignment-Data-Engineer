#!/usr/bin/env python
# coding: utf-8

# # Scrape the website data using beautifulsoup

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[4]:


page = requests.get("https://ieg.worldbankgroup.org/data")
soup=BeautifulSoup(page.content)
soup = BeautifulSoup(page.content, 'html.parser')


# In[5]:


soup


# In[8]:


page = requests.get("https://www.chinabidding.com/en")
soup1=BeautifulSoup(page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
soup1


# In[14]:


page = requests.get("http://www.ggzy.gov.cn/")
soup2=BeautifulSoup(page.content)
soup2 = BeautifulSoup(page.content, 'html.parser')
soup2


# In[13]:


page = requests.get("http://en.chinabidding.mofcom.gov.cn/")
soup3=BeautifulSoup(page.content)
soup3 = BeautifulSoup(page.content, 'html.parser')
soup3


# In[15]:


page = requests.get("https://www.cpppc.org/en/PPPyd.jhtml")
soup4=BeautifulSoup(page.content)
soup4 = BeautifulSoup(page.content, 'html.parser')
soup4


# In[16]:


page = requests.get("https://www.cpppc.org:8082/inforpublic/homepage.html#/searchresult")
soup5=BeautifulSoup(page.content)
soup5 = BeautifulSoup(page.content, 'html.parser')
soup5


# In[17]:


page = requests.get("https://etenders.gov.in/eprocure/app")
soup6=BeautifulSoup(page.content)
soup6 = BeautifulSoup(page.content, 'html.parser')
soup6


# In[ ]:




