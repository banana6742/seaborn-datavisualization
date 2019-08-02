
# coding: utf-8

# # Matrix Plots
# Matrix plots allow you to plot data as color-encoded matrices and can also be used to indicate clusters within the data (later in the machine learning section we will learn how to formally cluster data).
# Let's begin by exploring seaborn's heatmap and clutermap:

# In[15]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib.inline', '')
#how to create heat maps


# In[2]:


flights = sns.load_dataset('flights')


# In[3]:


tips = sns.load_dataset('tips')


# In[5]:


tips.head()


# In[7]:


flights.head()


# ## Heatmap
# In order for a heatmap to work properly, your data should already be in a matrix form, the sns.heatmap function basically just colors it in for you. For example:
# 
# 

# In[17]:


tips.head()


# In[19]:


tc = tips.corr()
tc


# In[20]:


sns.heatmap(tc)


# In[21]:


sns.heatmap(tc,annot=True)


# In[23]:


sns.heatmap(tc,annot=True,cmap='coolwarm')


# In[25]:


#flight
flights.head()


# In[29]:


#i want flight data as pivot data
flights.pivot_table(index='month',columns='year',values='passengers')


# In[30]:


#i wiil use heat map for visualize the flight data
pvflights = flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(pvflights)


# In[34]:


#cmap is also kind of color 
# sns.heatmap(pvflights,cmap="magma")
sns.heatmap(pvflights,cmap="coolwarm")


# In[37]:


#sns.heatmap(pvfligths,camp='magma',linecolor='white')
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)

#camp = 'coolwarm'
#,linewidth=4,linecolor='blue'


# # second type of matrix map is cluster map
# clustermap
# 
# the dustermap uses hierarchal clustering to reduce a clustered version of the heat map.for examle

# In[39]:


sns.clustermap(pvflights)
#columns which are similar are near to each other both in x and y axisNotice now how the years and months are no longer in order, instead they are grouped by similarity in value (passenger count). That means we can begin to infer things from this plot, such as August and July being similar (makes sense, since they are both summer travel months)
# Notice now how the years and months are no longer in order, instead they are grouped by similarity in value (passenger count). That means we can begin to infer things from this plot, such as August and July being similar (makes sense, since they are both summer travel months)


# In[41]:


#More options to get the information a little  clearer like normalizaition
sns.clustermap(pvflights,cmap='coolwarm')
#sns.clustermap(pvflights,camp='coolwarms',standard_scale=1)


# In[43]:


sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)


# # Grids
# Grids are general types of plots that allow you to map plot types to rows and columns of a grid, this helps you create similar plots separated by features.
# 

# In[44]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

#dataset is about measurement of flowers of iris
iris=sns.load_dataset('iris')
iris.head()


# In[45]:


iris["species"].unique()


# In[54]:


sns.pairplot(iris)


# # PairGrid
# Pairgrid is a subplot grid for plot pairwise relationships in a dataset

# In[48]:


sns.PairGrid(iris)


# In[55]:


g = sns.PairGrid(iris)


# In[56]:


g = sns.PairGrid(iris)
g.map(plt.scatter)


# In[57]:


#Map to upper,lower, and diagnal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# # pairsplot
# pairplot is a simpler version of PairGrid(you'll use quite often)

# In[59]:


sns.pairplot(iris)


# In[60]:


sns.pairplot(iris,hue='species',palette='rainbow')


# ## Facet Grid
# FacetGrid is the general way to create grids of plots based off of a feature

# In[62]:


tips = sns.load_dataset('tips')
#same as subplots
#just pass column and row
tips.head()


# In[63]:


#just the Grid
g = sns.FacetGrid(tips,col="time",row="smoker")


# In[64]:


g = sns.FacetGrid(tips,col="time",row = "smoker")
g = g.map(plt.hist,"total_bill")


# In[68]:


g = sns.FacetGrid(tips, col="time",row="smoker",hue='sex')
#### g=sns.FacetGrid(tips,col="time",row="smoker",hue='sex')
# Notice how the arguments come after plt.scatter call
g = g.map(plt.scatter,"total_bill","tip").add_legend()


# # JointGrid
# JointGrid is the general version for jointplot() type grids, for a quick example:
# 

# In[70]:


g = sns.JointGrid(x= "total_bill",y='tip',data=tips)


# In[72]:


g = sns.JointGrid(x="total_bill",y="tip",data=tips)
g = g.plot(sns.regplot, sns.distplot)


# # Regression Plots
# Seaborn has many built-in capabilities for regression plots, however we won't really discuss regression until the machine learning section of the course, so we will only cover the **lmplot()** function for now.
# **lmplot** allows you to display linear models, but it also conveniently allows you to split up those plots based off of features, as well as coloring the hue based off of features.
# Let's explore how this works:

# In[77]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')
tips.head()


# In[88]:


sns.lmplot(x='total_bill',y='tip',hue='sex',data=tips,palette='coolwarm',markers=['o','v'])


# In[90]:


sns.lmplot(x='total_bill',y='tip',hue='sex',data=tips,palette='coolwarm',markers=['o','v'],scatter_kws={'s':100})


# # Using a Grid
# We can add more variable separtion columns and rows with the use of a grid.Just indicate this with the col or row argument

# In[91]:


#this is creating 2 columns of sex => male and female

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[94]:


#this is creating 2 columns and row of sex => male and female
sns.lmplot(x='total_bill',y='tip',row="sex",col='time',data=tips)


# In[97]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm')


# In[100]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',aspect=0.6,size=5)

