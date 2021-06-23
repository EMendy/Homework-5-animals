#!/usr/bin/env python
# coding: utf-8

# # Homework 5, Part 2: Answer questions with pandas
# 
# **Use the Excel file to answer the following questions.** This is a little more typical of what your data exploration will look like with pandas.

# ## 0) Setup
# 
# Import pandas **with the correct name** .

# In[1]:


import pandas as pd


# ## 1) Reading in an Excel file
# 
# Use pandas to read in the `richpeople.xlsx` Excel file, saving it as a variable with the name we'll always use for a dataframe.
# 
# > **TIP:** You will use `read_excel` instead of `read_csv`, *but you'll also need to install a new library*. You might need to restart your kernel afterward!

# In[2]:


get_ipython().system('pip install openpyxl')


# In[4]:


df = pd.read_excel('richpeople.xlsx')


# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# In[5]:


df


# In[6]:


df.shape[0]


# In[7]:


df.shape[1]


# ## 3) Who are the top 10 richest billionaires? Use the `networthusbillion` column.

# In[13]:


df.sort_values(by='networthusbillion', ascending=False).head(10)


# ## 4) How many male billionaires are there compared to the number of female billionares? What percent is that? Do they have a different average wealth?
# 
# > **TIP:** The last part uses `groupby`, but the count/percent part does not.
# > **TIP:** When I say "average," you can pick what kind of average you use.

# In[14]:


rich_ladies = (df.gender == 'female')


# In[15]:


rich_guys = (df.gender == 'male')


# In[27]:


print(df[rich_guys].name.count())
print(df[rich_ladies].name.count())
print(((df[rich_guys].name.count())/(df[rich_ladies].name.count())*100).round(2))


# In[32]:


df[rich_ladies].networthusbillion.mean().round(3)


# In[31]:


df[rich_guys].networthusbillion.mean().round(3)


# In[34]:


# I am not sure what needs the groupby, so I'll need to check what I messed up on this one. 


# ## 5) What is the most common source/type of wealth? Is it different between males and females?
# 
# > **TIP:** You know how to `groupby` and you know how to count how many times a value is in a column. Can you put them together???
# > **TIP:** Use percentages for this, it makes it a lot more readable.

# In[35]:


df[rich_ladies].sourceofwealth.mode()


# In[36]:


df[rich_guys].sourceofwealth.mode()


# In[37]:


#again, not sure why the tip is used in this case.  It appears that the use of the variable I created worked, but I might have gotten this wrong.


# ## 6) What companies have the most billionaires? Graph the top 5 as a horizontal bar graph.
# 
# > **TIP:** First find the answer to the question, then just try to throw `.plot()` on the end
# >
# > **TIP:** You can use `.head()` on *anything*, not just your basic `df`
# >
# > **TIP:** You might feel like you should use `groupby`, but don't! There's an easier way to count.
# >
# > **TIP:** Make the largest bar be at the top of the graph
# >
# > **TIP:** If your chart seems... weird, think about where in the process you're sorting vs using `head`

# In[38]:


#df.groupby(by='sourceofwealth')
df.sourceofwealth.value_counts()


# In[39]:


df.sourceofwealth.value_counts().head()


# In[43]:


df.sourceofwealth.value_counts().head().sort_values().plot(kind='barh')


# ## 7) How much money do these billionaires have in total?

# In[49]:


# I assume this is about ALL of the billionaires? 

df.networthusbillion.sum().round(3)


# ## 8) What are the top 10 countries with the most money held by billionaires?
# 
# I am **not** asking which country has the most billionaires - this is **total amount of money per country.**
# 
# > **TIP:** Think about it in steps - "I want them organized by country," "I want their net worth," "I want to add it all up," and "I want 10 of them." Just chain it all together.

# In[52]:


df.groupby(by='citizenship').networthusbillion.sum().sort_values(ascending = False).head(10)


# ## 9) How old is an average billionaire? How old are self-made billionaires  vs. non self-made billionaires? 

# In[54]:


#Is this asking the average age of a billionaire? 
df.age.mean().round(2)


# In[55]:


df[df.selfmade == 'self-made'].age.mean().round(2)


# In[56]:


df[df.selfmade == 'inherited'].age.mean().round(2)


# ## 10) Who are the youngest billionaires? Who are the oldest? Make a graph of the distribution of ages.
# 
# > **TIP:** You use `.plot()` to graph values in a column independently, but `.hist()` to draw a [histogram](https://www.mathsisfun.com/data/histograms.html) of the distribution of their values

# In[63]:


df.age.sort_values().count()


# In[68]:


df.age.sort_values().dropna().tail()


# In[69]:


df.age.sort_values().dropna().head()


# In[76]:


df.age.sort_values().dropna().plot.hist(x ='age')


# ## 11) Make a scatterplot of net worth compared to age

# In[79]:


df.plot.scatter(x ='age', y = 'networthusbillion')


# In[80]:


# what happends to NA values when you plot like this? 


# ## 13) Make a bar graph of the wealth of the top 10 richest billionaires
# 
# > **TIP:** When you make your plot, you'll need to set the `x` and `y` or else your chart will look _crazy_
# >
# > **TIP:** x and y might be the opposite of what you expect them to be

# In[85]:


df.networthusbillion.sort_values(ascending = False).head(10).plot(kind='barh', x = 'Net Worth Billions', y = 'index')


# In[ ]:




