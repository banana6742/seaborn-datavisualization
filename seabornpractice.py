
# coding: utf-8

# # Style and Color
# We've shown a few times how to control figure aetheics in seaborn, but let's now go over it formally:

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')


# # Styles
# you can set particular styles:

# In[4]:


sns.countplot(x='sex',data=tips)


# In[5]:


sns.set_style('white')
sns.countplot(x='sex',data=tips)


# In[9]:


sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')


# # Size and Aspect
# you can use matplotlib's **plt.figure(figsize=(width,height)) ** to change the size of most seaborn plots.
# You can control the size aspect ratio of most seaborn grid plots by passing in parameters;size,and aspect, for example

# In[11]:


#Non Grid Plot
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)


# In[19]:


#Grid Type Plot
sns.lmplot(x='total_bill',y='tip',size=4,aspect=2,data=tips)


# # Scale and Context
# The set_context() allows you to override defalut parameters

# In[53]:


sns.set_context('poster',font_scale=2)
sns.countplot(x='sex',data=tips,palette='coolwarm')


# # Exercise 1
# ** Follow along with these steps: **
# ** Create a figure object called fig using plt.figure() **
# ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**
# 
# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**
# ** Now plot (x,y) on both axes. And call your figure object to show it.**

# In[52]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
x = np.arange(0,100)
y = x*2
z = x**2
plt.xlabel('horizontal')
plt.ylabel('vertical')
plt.plot(x,y)

fig = plt.figure()


# In[51]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


# In[48]:


fig = plt.figure()
axes1 = fig.add_axes([0,0,1,1])
axes2 = fig.add_axes([0.2,0.5,.2,.2])

axes1.plot(x,y)
axes2.plot(x,y)

axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title')
plt.show()


# In[50]:


ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])


ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y' )

ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')

fig


# # Exercise 3
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**
# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

# In[74]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])


# In[75]:


ax.plot(x,z)
ax.set_xlabel('X')
ax.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_xlabel('X')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.set_xlim(20,22)
ax2.set_xlim(30,50)

fig


# # Exercise 4
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

# In[96]:


fig, axes = plt.subplots(1,2)  


# In[90]:


axes[0].plot(x,y,color="blue")


# # ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**
# ** See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.**

# In[93]:


fig, (ax1,ax2) = plt.subplots(1,2)

ax1.plot(x,y)
ax2.plot(x,z) 


# In[97]:


axes[0].plot(x,y,color="blue",lw=3,ls='--')
axes[1].plot(x,z,color="red",lw=3,ls='-')
fig


# In[108]:


fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue",lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red",lw=3,ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')


# In[110]:




