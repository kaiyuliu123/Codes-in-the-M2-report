#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


data = pd.read_excel('C:/Users/Louis Althusser/Desktop/Nano Results/Nanooresults Mars/Spectrum Mars/Emission Spectrum.xlsx',index_col=0,sheet_name=4)
df = data


# In[3]:


df


# In[4]:


plt.rcParams["figure.figsize"] = [6, 5]
plt.rcParams["figure.dpi"] = 600


# In[5]:


df.plot()
plt.title('Emission Spectrum - Au$_2$$_5$pMBA$_1$$_8$ with 5μM PEI')
plt.ylabel('PL intensity')
plt.yticks(np.arange(4000,step=500))
plt.xticks(np.arange(880,1780, step=100))


# In[6]:


x=df.index.values


# In[7]:


names = locals()
i=1
while i < 6:
 names['y' + str(i) ] = df.iloc[:,i-1].values
 i=i+1


# In[13]:


from scipy import signal
y1_smooth = signal.savgol_filter(y1,29,3)  
y2_smooth = signal.savgol_filter(y2,29,3)
y3_smooth = signal.savgol_filter(y3,29,3)
y4_smooth = signal.savgol_filter(y4,29,3)
y5_smooth = signal.savgol_filter(y5,29,3)

plt.plot (x,y1_smooth, label ='Au$_2$$_5$pMBA$_1$$_8$')
plt.plot(x,y2_smooth,label='Au$_2$$_5$pMBA$_1$$_8$+PEI, t=0')
plt.plot(x,y3_smooth,label = 'Au$_2$$_5$pMBA$_1$$_8$+PEI, t=30min')
plt.plot(x,y4_smooth,label='Au$_2$$_5$pMBA$_1$$_8$+PEI, t=60min')
plt.plot(x,y5_smooth,label='Au$_2$$_5$pMBA$_1$$_8$+PEI, t=90min')

plt.title('Emission Spectrum - Au$_2$$_5$pMBA$_1$$_8$ with 5μM PEI',fontsize=14)
plt.ylabel('PL intensity (a.u.)',fontsize=14)
plt.xlabel('Wavelength (nm)',fontsize=14)
plt.yticks(np.arange(4000,step=500))
plt.xticks(np.arange(880,1580, step=100))
plt.xlim(880,1480)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=14)
line_colors = [line.get_color() for line in plt.gca().get_lines()]


import os
dir_path = r"C:\Users\Louis Althusser\Desktop\Nano Results\Nanooresults Mars\Spectrum Mars\New Graphs"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, "Emission Spectrum - Au$_2$$_5$pMBA$_1$$_8$ with 5μM PEI.png")
plt.savefig(file_path)


# In[12]:


x6 = np.arange(5)
y6 = np.array([1, 1.13, 1.86, 1.95, 2.10])
fig, ax2 = plt.subplots()
ax2.set_xticks(x6)
ax2.set_xticklabels([])
ax2.set_yticks(np.arange(0, 2.1, step=1))
ax2.set_ylim([0, 2.5])
ax2.set_ylabel('Fold Change',fontsize=14)
bar_width = 0.5
bars = ax2.bar(x6, y6, width=bar_width, color=line_colors, edgecolor='none')

for i, bar in enumerate(bars):
    value = y6[i]    
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+0.15, f'{value:.2f}', ha='center', va='top', fontsize=14)

plt.show()

import os
dir_path = r"C:\Users\Louis Althusser\Desktop\Nano Results\Nanooresults Mars\Spectrum Mars\New Graphs"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, "Bars - Au25pMBAT with 5μM PEI.png")
plt.savefig(file_path)


# In[ ]:




