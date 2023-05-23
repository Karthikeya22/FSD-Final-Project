#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
import warnings
warnings.filterwarnings("ignore")


# In[36]:


df=pd.read_csv(r"""C:\Users\sooja\Downloads\Untitled spreadsheet - Sheet1.csv""")


# In[37]:


df


# In[38]:


df.drop(df.columns[[5]],axis = 1,inplace=True)


# In[39]:


df.info()


# In[40]:


bool_series = pd.isnull(df["avg price"])


# In[41]:


bool_series


# In[42]:


df['orderdate']=pd.to_datetime(df['orderdate'])


# In[43]:


import seaborn as sns


# In[44]:


sns.boxplot(df['avg price'])


# In[45]:


sns.boxplot(df['ordercount'])


# In[46]:


filter1=df['ordercount']<50000
df.where(filter1,inplace=True)


# In[47]:


sns.boxplot(df['ordercount'])


# In[48]:


enc=OrdinalEncoder()


# In[49]:


df['prod']=enc.fit_transform(df[['prod_name']]).astype(int)


# In[ ]:





# In[50]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import statsmodels.graphics.tsaplots as sm


# In[51]:


df.set_index('orderdate',inplace=True)


# In[52]:


df['pricediff']=df['avg price']-df['avg price'].shift(1)


# In[ ]:





# In[53]:


df['ordercountdif']=df['ordercount']-df['ordercount'].shift(1)


# In[ ]:





# In[54]:


fig=plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig=sm.plot_acf(df['pricediff'].dropna(),lags=40,ax=ax1)

ax2=fig.add_subplot(212)
fig=sm.plot_pacf(df['pricediff'].dropna(),lags=40,ax=ax1)


# In[55]:


fig=plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig=sm.plot_acf(df['ordercountdif'].dropna(),lags=40,ax=ax1)

ax2=fig.add_subplot(212)
fig=sm.plot_pacf(df['ordercountdif'].dropna(),lags=40,ax=ax1)


# In[56]:


from statsmodels.tsa.arima_model import ARIMA


# In[57]:


model=ARIMA(df['avg price'],order=(1,1,0))
model_fit=model.fit()


# In[58]:


model_fit.summary()


# In[59]:


df.info()


# In[60]:


df['priceforecast']=model_fit.predict(start=753,end=897)


# In[61]:


df['priceforecast'].plot(figsize=(12,6))


# In[62]:


df['priceforecast']


# In[63]:


model1=ARIMA(df['ordercount'],order=(1,1,1))
model_fit1=model.fit()


# In[64]:


model_fit1.summary()


# In[65]:


df['dforecast']=model_fit.predict(start=753,end=897)


# In[66]:


df['dforecast'].plot(figsize=(12,6))


# In[67]:


df['dforecast']


# In[ ]:





# In[ ]:





# In[ ]:




