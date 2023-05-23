#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder


# In[49]:


df=pd.read_csv(r"""C:\Users\sooja\Downloads\Untitled spreadsheet - Sheet1.csv""")


# In[50]:


df.info()


# In[51]:


df.drop(df.columns[[5]],axis = 1,inplace=True)


# In[ ]:





# In[53]:


df['orderdate'].astype(str)


# In[22]:


df.info()


# In[23]:


import seaborn as sns


# In[24]:


sns.boxplot(df['avg price'])


# In[25]:


sns.boxplot(df['ordercount'])


# In[55]:


df['orddate']=df['orderdate'].apply(lambda x: x.split(' ')[0])
df['Day']=df['orderdate'].apply(lambda x: x.split('-')[1]).astype(int)
df['Month']=df['orderdate'].apply(lambda x: x.split('-')[0]).astype(int)
df['Year']=df['orderdate'].apply(lambda x: x.split('-')[2]).astype(int)


# In[56]:


df['Day'].astype(int)


# In[57]:


df['Month'].astype(int)


# In[58]:


df['Year']


# In[59]:


enc=OrdinalEncoder()


# In[60]:


df['prod']=enc.fit_transform(df[['prod_name']]).astype(int)


# In[61]:


df1=df[['prod_id','avg price','prod','ordercount','Day','Month','Year']]


# In[76]:


x=df1.drop(df[['avg price','ordercount']],axis=1)
y=df1[['avg price','ordercount']]


# In[77]:


from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# In[78]:


X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size = 0.2, random_state = 2)


# In[79]:


model1=XGBRegressor()


# In[80]:


model1.fit(X_train,Y_train)


# In[81]:


train1=model1.predict(X_train)


# In[82]:


train1


# In[85]:


metrics.r2_score(Y_train,train1)


# In[ ]:




