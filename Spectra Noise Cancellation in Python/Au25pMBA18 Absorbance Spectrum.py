#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[16]:


data = pd.read_excel('C:/Users/Louis Althusser/Desktop/Nano Results/Nanooresults Mars/Spectrum Mars/Absorbance Spectrum.xlsx',index_col=0,sheet_name=5)
df = data.iloc[100:]


# In[17]:


df


# In[18]:


plt.rcParams["figure.figsize"] = [6, 5]
plt.rcParams["figure.dpi"] = 600


# In[23]:


df.plot()
plt.title('Absorbance Spectrum - Au$_2$$_5$pMBA$_1$$_8$ with 5μM PEI', fontsize=14)
plt.ylabel('Absorbance (a.u.)', fontsize=14)
plt.xlabel("Wavelength (nm)", fontsize=14)
plt.yticks(np.arange(1.2, step=0.2))
plt.xticks(np.arange(300,1000, step=100))
plt.xlim(350,900)


# In[7]:


x=df.index.values


# In[8]:


x=x[::-1]
x


# In[9]:


names = locals()
i=1
while i < 6:
 names['y' + str(i) ] = df.iloc[:,i-1].values
 i=i+1


# In[10]:


y1=y1[::-1]
y2=y2[::-1]
y3=y3[::-1]
y4=y4[::-1]
y5=y5[::-1]
y1,y2,y3,y4,y5


# In[13]:


from scipy import signal
y1_smooth = signal.savgol_filter(y1,99,5)  
y2_smooth = signal.savgol_filter(y2,99,5)
y3_smooth = signal.savgol_filter(y3,99,5)
y4_smooth = signal.savgol_filter(y4,99,5)
y5_smooth = signal.savgol_filter(y5,99,5)
plt.plot (x,y1_smooth, label ="Au$_2$$_5$pMBA$_1$$_8$")
plt.plot(x,y2_smooth,label='Au$_2$$_5$pMBA$_1$$_8$+PEI, t=0')
plt.plot(x,y3_smooth,label = 'Au$_2$$_5$pMBA$_1$$_8$+PEI, t=30min')
plt.plot(x,y4_smooth,label='Au$_2$$_5$pMBA$_1$$_8$+PEI, t=60min')
plt.plot(x,y5_smooth,label='Au$_2$$_5$pMBA$_1$$_8$+PEI, t=90min')
plt.title('Absorbance Spectrum - Au$_2$$_5$pMBA$_1$$_8$ with 5μM PEI', fontsize=14)
plt.ylabel('Absorbance (a.u.)',fontsize=14)
plt.xlabel('Wavelength (nm)',fontsize=14)
plt.yticks(np.arange(1.2, step=0.2))
plt.xticks(np.arange(300,1000, step=100))
plt.xlim(350,900)
plt.legend(fontsize=14)

import os
dir_path = r"C:\Users\Louis Althusser\Desktop\Nano Results\Nanooresults Mars\Spectrum Mars\New Graphs"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, "Absorbance Spectrum - Au$_2$$_5$pMBA$_1$$_8$ with 5μM PEI.png")
plt.savefig(file_path)


# In[ ]:




