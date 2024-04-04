#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


os.chdir(r"C:\Users\Lenovo\OneDrive\Desktop\cardataset")


# In[4]:


df=pd.read_csv("Data_Analyst_Assignment_Dataset.csv")


# In[5]:


df


# In[6]:


df.shape


# In[8]:


df.info


# In[10]:


df.dtypes


# In[11]:


df.describe()


# In[12]:


df.isnull()


# In[14]:


df['Amount Pending']


# In[18]:


state_counts = df['State'].value_counts()


print("State Distribution:")
print(state_counts)



plt.figure(figsize=(10, 6))
state_counts.plot(kind='bar')
plt.title('State Distribution')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[20]:



plt.figure(figsize=(10, 6))
plt.hist(df['Tenure'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Tenure')
plt.xlabel('Tenure')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[21]:


plt.figure(figsize=(10, 6))
plt.hist(df['Interest Rate'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Interest Rates')
plt.xlabel('Interest Rate')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[24]:


print("Summary statistics of City:")
print(df['City'].describe())


city_counts = df['City'].value_counts()

# Display the city distribution
print("\nCity Distribution:")
print(city_counts)



plt.figure(figsize=(12, 6))
city_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 City Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[26]:


#df['city'].describe()
df['City'].describe()


# In[28]:


city_counts


# In[29]:


plt.figure(figsize=(12, 6))
city_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 City Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[30]:


bounce_counts = df['Bounce String'].value_counts()


print("Bounce Behavior Distribution:")
print(bounce_counts)



plt.figure(figsize=(8, 8))
bounce_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Bounce Behavior Distribution')
plt.ylabel('')
plt.show()


# In[31]:


df['Disbursed Amount'].describe()


# In[33]:


plt.figure(figsize=(10, 6))
plt.hist(df['Disbursed Amount'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Disbursed Amounts')
plt.xlabel('Disbursed Amount')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[36]:


unique_loan_numbers = df['Loan Number'].nunique()
total_entries = df.shape[0]
plt.figure(figsize=(10, 6))
df['Loan Number'].value_counts().plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Loan Numbers')
plt.xlabel('Loan Number')
plt.ylabel('Frequency')
plt.grid(True)


# In[37]:




df['Bounces_Last_6_Months'] = df['Bounce String'].apply(lambda x: x[:6].count('B') + x[:6].count('L'))


df['Bounced_Last_Month'] = df['Bounce String'].apply(lambda x: x[-1] == 'B' or x[-1] == 'L')


def assign_risk_label(row):
    if row['Bounced_Last_Month']:
        return 'Unknown risk'
    elif row['Bounces_Last_6_Months'] == 0:
        return 'Low risk'
    elif row['Bounces_Last_6_Months'] <= 2:
        return 'Medium risk'
    else:
        return 'High risk'

df['Risk_Label'] = df.apply(assign_risk_label, axis=1)


print(df[['Loan Number', 'Risk_Label']])


# In[45]:


max_tenure = df['Tenure'].max()
def tenure_status(row):
    if row['Tenure'] <= 3:
        return 'Early Tenure'
    elif row['Tenure'] >= max_tenure - 3:
        return 'Late Tenure'
    else:
        return 'Mid Tenure'

df['Tenure_Status'] = df.apply(tenure_status, axis=1)


print(df[['Loan Number', 'Tenure_Status']])


# In[46]:


df_sorted = df.sort_values(by='Amount Pending')


cohort_size = len(df_sorted) // 3


def assign_ticket_size_label(index):
    if index < cohort_size:
        return 'Low ticket size'
    elif index < 2 * cohort_size:
        return 'Medium ticket size'
    else:
        return 'High ticket size'


df_sorted['Ticket Size'] = df_sorted.index.map(assign_ticket_size_label)


print(df_sorted[['Loan Number', 'Amount Pending', 'Ticket Size']])


# In[48]:


def assign_spend_category(row):
    if row['Bounce String'].startswith('FEMI'):
        return 'Whatsapp bot'
    elif row['State'] in ['English', 'Hindi'] and row['Bounce String'] == 'Low' and row['Amount Pending'] in ['Low', 'Medium']:
        return 'Voice bot'
    else:
        return 'Human calling'


df['Spend Category'] = df.apply(assign_spend_category, axis=1)


print(df[['Loan Number', 'Spend Category']])


# In[ ]:




