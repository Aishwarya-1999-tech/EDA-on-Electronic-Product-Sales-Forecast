#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as p
import seaborn as sns


# In[8]:


electronicdata=pd.read_csv("C:\\Users\\raghav\\Desktop\\Course\\Electronicsales.csv")


# In[9]:


electronicdata


# In[10]:


electronicdata.info()


# In[11]:


np.shape(electronicdata) 


# In[12]:


electronicdata.describe() 


# In[13]:


# Visualizing the [CUSTOMER DEMOGRAPHICS] customer age
p.figure(figsize=(4,4))
ax=sns.boxplot(data=electronicdata ,y="Age")
p.show()


# In[14]:


# ANALYSIS- THE ABOVE VISUALIZATION SHOWS THAT CUSTOMER LIES BETWEEN THE 
#            AGE GROUP OF 35-65


# In[15]:


#visualizing the customer gender
p.figure(figsize=(4,4))
ax=sns.countplot(data=electronicdata,x="Gender")
ax.bar_label(ax.containers[0])
p.show()


# In[16]:


# ANALYSIS- THE ABOVE VISUALIZATION SHOW MORE MALE CUSTOMER THEN FEMALE


# In[17]:


p.figure(figsize=(4,4))
ax=sns.countplot(x='Loyalty Member', data=electronicdata, palette='Set2')
p.title("Loyalty_Membership_Distribution")
p.xlabel('Loyalty Member')
p.ylabel('Count')
ax.bar_label(ax.containers[0])
p.show()


# In[18]:


# ANALYSIS- MOST OF THE CUSTOMERS ARE NOT LOYAL


# In[19]:


# PRODUCT PERFORMANCE ANALYSIS


# In[20]:


PRD=electronicdata.groupby("Product Type"),["Total Price"]
p.figure(figsize=(7,4))
ax=sns.barplot(x='Total Price', y='Product Type',data=electronicdata, palette='coolwarm')
p.title('Product performance Analysis')
p.xlabel('Total Sales(in USD)')
p.ylabel('Product Type')
ax.bar_label(ax.containers[0])
p.show()


# In[21]:


#ANALYSIS- VISUALIZATION SHOWS THAT SMARTPHONES,SMARTWATCH AND LAPTOP HAS MOST SALES


# In[22]:


prdrating=electronicdata.groupby("Product Type"),("Rating")
p.figure(figsize=(7,6))
sns.violinplot(x='Product Type', y='Rating',data=electronicdata)
p.title('Product Ratings as per product types')
p.xlabel('Product Type')
p.ylabel('Ratings')
p.show()


# In[23]:


#ANALYSIS


# In[24]:


# Order status Analysis
p.figure(figsize=(5,5))
ax=sns.countplot(x="Order Status",data=electronicdata)
ax.bar_label(ax.containers[0])
p.title=("Order Status Analysis")
p.show()


# In[25]:


#PAYMENT AND SHIPPING ANALYSIS


# In[26]:


payment_method_counts = electronicdata['Payment Method'].value_counts()
labels = payment_method_counts.index
sizes = payment_method_counts.values
colors = sns.color_palette('Set3')
p.figure(figsize=(4,4))
p.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
center_circle = p.Circle((0, 0), 0.70, color='white', fc='white', linewidth=1.25)
p.,p.gca().add_artist(center_circle)
p.title('Payment Method Distribution (Donut Chart)')
p.axis('equal')
p.show()


# In[ ]:


#ANALYSIS- Credit card is the most preferred payment Method


# In[28]:


labels=["Standard", "Express","Overnight"]
sizes=[50,40,30]
colors=["lightblue","lightgreen","lightpink"]
p.figure(figsize=(4,4))
p.pie(sizes,labels=labels,autopct='%1.1f%%',colors=colors,startangle=90)
p.axis("equal")
p.title("Shipping Type distribution (Piechart)")
p.show()


# In[ ]:


# ANALYSIS-Customers preferred standard shipping


# In[ ]:


#Sales Trend Analysis


# In[27]:


# Convert the 'Purchase Date' column to a datetime format
electronicdata['Purchase Date'] = pd.to_datetime(electronicdata['Purchase Date'], format='%d-%m-%Y')

# Group data by month and year, aggregating the total sales (Total Price)
electronicdata['Year-Month'] = electronicdata['Purchase Date'].dt.to_period('M')
monthly_sales = electronicdata.groupby('Year-Month')['Total Price'].sum().reset_index()

p.figure(figsize=(5,5))
p.plot(monthly_sales['Year-Month'].astype(str), monthly_sales['Total Price'], marker='o', linestyle='--', color='b')
p.xticks(rotation=90)
p.title('Total Sales Trend Over Time')
p.xlabel('Year-Month')
p.ylabel('Total Sales (in USD)')
p.grid(True)
p.tight_layout()

p.show()


# In[ ]:


electronicdata.groupby("Purchase Date"),["Total Price"]
p.figure(figsize=(10,10))
ax=sns.barplot(x='Purchase Date', y='Total Price',data=electronicdata, palette='coolwarm')
p.title('Yearly Sales Analysis')
p.xlabel('Yearly Sales')
p.ylabel('Total Sales')
ax.bar_label(ax.containers[0])
p.show()


# In[23]:


electronicdata["Year"]=electronicdata["Purchase Date"]
Yearlysales=electronicdata.groupby("Year")["Total Price"]
p.figure(figsize=(5,5))
sns.countplot(x='Year',data=electronicdata, palette='coolwarm')
p.title('Yearly Sales Analysis')
p.xlabel('Yearly Sales')
p.ylabel('Total Sales')

p.show() 


# In[ ]:




