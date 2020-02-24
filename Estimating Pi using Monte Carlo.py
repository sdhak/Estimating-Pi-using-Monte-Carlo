#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


def sim_pi(total_sim):
    np.random.seed(0) #creating a random seed to save the previous random numbers generated
    x_new = [] #creating an empty list for x values
    y_new = [] #creating an empty list for y values
    circle = [] #creating an empty list to save the values that fall inside the circle

    radius = 0.5
    cir_plot = plt.Circle((0.5, 0.5), 0.5, color = 'r', fill = False) #plotting a circle 
    sq_plot = plt.Rectangle((0,0), 1, 1, color = 'b', fill = False) #plotting a rectangle
    fig = plt.gcf()
    ax = fig.gca(adjustable='box')
    ax.set_aspect('equal')
    ax.add_artist(cir_plot)
    ax.add_artist(sq_plot)


    dots = 0

    for i in np.arange(total_sim):
        x = np.random.rand(1,1)
        y = np.random.rand(1,1)
        x_new = np.append(x_new, x)
        y_new = np.append(y_new, y)
    
        if (x - 0.5)**2 + (y - 0.5)**2 < radius**2:
            circle = np.append(circle, "red")
            dots +=1
        else:
            circle = np.append(circle, "blue")

    plot = plt.scatter(x_new, y_new, s = 1.5, color = circle)


    pi_val = (dots / total_sim)*4
    diff = round(abs(pi_val-3.14159),4)
    print ("This simulation gives a pi value of", str(pi_val) + 
           ". The difference between the known pi value of", str(3.14) + 
           " and our simulated value is", str(diff) + ".")


# In[10]:


#simulations: 10, 500, 1000, 5000, 10,000, 50,000, 80,000,..
#..100,000, 200,000
sim_pi(10)


# In[11]:


sim_pi(500)


# In[12]:


sim_pi(1000)


# In[13]:


sim_pi(5000)


# In[14]:


sim_pi(10000)


# In[15]:


sim_pi(50000)


# In[16]:


sim_pi(80000)


# In[17]:


sim_pi(100000)


# In[18]:


sim_pi(200000)


# In[19]:


#creating a line chart to show the change of the accuracy 
#of the value of π calculated when the number of points is increased.

data = {'Simulations':  ['Sim_10', 'Sim_500', 'Sim_1K', 'Sim_5K', 'Sim_10K',
                        'Sim_50K', 'Sim_80K', 'Sim_100K', 'Sim_200K'],
        'Estimated Pi Value': [3.2, 3.064, 3.052, 3.14, 3.1228, 3.13856,
                               3.13955, 3.1422, 3.13812],
        }

pi_values = pd.DataFrame (data, columns = ['Simulations','Estimated Pi Value'])
print(pi_values);

plot0 = pi_values.plot(x ='Simulations', y='Estimated Pi Value', kind = 'line')
plot0.set_ylabel('Estimated Pi Values')
plt.xticks(rotation=45)


# In[ ]:





# In[ ]:




