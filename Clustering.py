#!/usr/bin/env python
# coding: utf-8

# In[4]:


from utils import *
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import os

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pandas as pd
df = pd.read_excel('F:/Data/data for clustering-modified.xlsx')
df_patient = pd.read_excel('F:\Data/Hospital1.xlsx')
df_clusters = pd.read_excel('F:\Data/newkmeansresults.xlsx')


# In[25]:


# incl = ['Home', 'Away', 'Shops']    
# for k, g in df[df['D'].isin(incl)].groupby('D'):
#     g.to_csv(f'{k}.csv')  # '{}.csv'.format(k)
# https://stackoverflow.com/questions/50829206/save-pandas-groups-to-separate-csv-files

# cnames = list(df.columns.values)
# ci = cnames[8]
# c_id = cnames[0]

# print(ci)
# class_list = set(list(df[ci]))
# print(class_list)


# for k, g in df[df[ci].isin(class_list)].groupby(ci):
#     patient_list = g[c_id]
#     patient_ck = df_patient[df_patient['Patient ID'].isin(patient_list)]

#     patient_ck.to_csv(f'result/{numClusters}/csv/{k}.csv')  # '{}.csv'.format(k)
#     patient_ck.to_excel(f'result/{numClusters}/xlsx/{k}.xlsx')  # '{}.xlsx'.format(k)

cnames = list(df_clusters.columns.values)
cnames_main = list(df.columns.values)

c_cl = cnames[1]
c_id = cnames[0]
class_list = set(list(df_clusters[c_cl]))
# df_clusters
cnames
class_list

# for k, g in df[df[ci].isin(class_list)].groupby(c_cl):
#     patient_list = g[c_id]
#     patient_ck = df_patient[df_patient['Patient ID'].isin(patient_list)]

#     patient_ck.to_csv(f'result/{numClusters}/csv/{k}.csv')  # '{}.csv'.format(k)
#     patient_ck.to_excel(f'result/{numClusters}/xlsx/{k}.xlsx')  # '{}.xlsx'.format(k)
ci_m = cnames_main[0]
df[ci_m]

df_clusters_grp = df_clusters.groupby(by=c_cl)

# for k, g in df[df[ci_m].isin(class_list)].groupby(c_cl):
#     patient_list = g[c_id]
#     patient_ck = df_patient[df_patient['Patient ID'].isin(patient_list)]

#     patient_ck.to_csv(f'result/{numClusters}/csv/{k}.csv')  # '{}.csv'.format(k)
#     patient_ck.to_excel(f'result/{numClusters}/xlsx/{k}.xlsx')  # '{}.xlsx'.format(k)
# df_clusters_grp[0]
for k,g in df_clusters_grp:
    patient_list = g[c_id]
    patient_ck = df_patient[df_patient['Patient ID'].isin(patient_list)]
    patient_ck.to_csv(f'resultn/csv/{k}.csv')  # '{}.csv'.format(k)
    patient_ck.to_excel(f'resultn/xlsx/{k}.xlsx')  # '{}.xlsx'.format(k)


# In[3]:


df.head()

# df_patient.head()


# In[4]:


df.shape


# In[5]:


df.isna().sum()


# In[7]:


# fill nan value 
df = FillNa(df = df)

# make copy from df
copy_df = df.copy()
copy_df = copy_df.dropna()
copy_df = copy_df.reset_index(drop=True)


# In[8]:


# change column type
df , transition = TransitionType2(df = df)


# In[9]:


transition


# In[10]:


df.describe()


# In[11]:


df = df.dropna()
df = df.reset_index(drop=True)
df.shape


# In[12]:


df.hist(figsize=(10 , 10))
plt.show()


# In[13]:


fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df['1.AIS PREDOT CODE (کد شش رقمی قبل از اعشار) منعکس کننده آسیب‌های بیمار'] ,
            df['سن بیمار هنگام مصدومیت'] , color = 'Blue')
axs.set_xlabel('1.AIS PREDOT CODE (کد شش رقمی قبل از اعشار) منعکس کننده آسیب‌های بیمار')
axs.set_ylabel('سن بیمار هنگام مصدومیت')
plt.show()


# In[14]:


cnames = list(df.columns.values)
c_x = cnames[6]
c_y = cnames[2]
c_x,c_y

fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df[c_x] , df[c_y] , color = 'Blue')
axs.set_xlabel(c_x)
axs.set_ylabel(c_y)
plt.show()
# # df


# In[15]:


cnames = list(df.columns.values)
print(cnames)
c_x = cnames[5]
c_y = cnames[2]
c_x,c_y

fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df[c_x] , df[c_y] , color = 'Blue')
axs.set_xlabel(c_x)
axs.set_ylabel(c_y)
plt.show()


# 'جنسیت'/'ISS',

# In[16]:


cnames = list(df.columns.values)
print(cnames)
c_x = cnames[5]
c_y = cnames[1]
c_x,c_y

fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df[c_x] , df[c_y] , color = 'Blue')
axs.set_xlabel(c_x)
axs.set_ylabel(c_y)
plt.show()


# In[17]:


cnames = list(df.columns.values)
print(cnames)
c_x = cnames[5]
c_y = cnames[3]
c_x,c_y

fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df[c_x] , df[c_y] , color = 'Blue')
axs.set_xlabel(c_x)
axs.set_ylabel(c_y)
plt.show()


# In[18]:


cnames = list(df.columns.values)
print(cnames)
c_x = cnames[5]
c_y = cnames[4]
c_x,c_y

fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df[c_x] , df[c_y] , color = 'Blue')
axs.set_xlabel(c_x)
axs.set_ylabel(c_y)
plt.show()


# In[19]:


cnames = list(df.columns.values)
print(cnames)
c_x = cnames[6]
c_y = cnames[3]
c_x,c_y

fig, axs = plt.subplots(1,1 , figsize=(20 , 10))

axs.scatter(df[c_x] , df[c_y] , color = 'Blue')
axs.set_xlabel(c_x)
axs.set_ylabel(c_y)
plt.show()


# In[20]:


scaler , x = Normalization(df = df.drop(['شناسه بیمار'] , axis = 1))


# In[21]:


ElbowSilhouette(x = x)


# In[48]:


numClusters = 15

labels = kmeans(x = x , clusterNum = numClusters)
df['کلاس'] = labels
copy_df['کلاس'] = labels



path = "result/"+str(numClusters)

if not os.path.exists(path):
   os.makedirs(path+"/xlsx")
   os.makedirs(path+"/csv")
   print("The new directory is created!")


# In[42]:


df.groupby("کلاس").mean()


# In[45]:


ShowClass2(df = df , x = x)


# In[27]:


# df['کلاس'] = labels
# df[['شناسه بیمار' , 'کلاس']].to_csv('./Data/result.csv', index = False )  


# In[50]:


set(labels)


# In[51]:


# incl = ['Home', 'Away', 'Shops']    
# for k, g in df[df['D'].isin(incl)].groupby('D'):
#     g.to_csv(f'{k}.csv')  # '{}.csv'.format(k)
# https://stackoverflow.com/questions/50829206/save-pandas-groups-to-separate-csv-files

cnames = list(df.columns.values)
ci = cnames[8]
c_id = cnames[0]

print(ci)
class_list = set(list(df[ci]))
print(class_list)


for k, g in df[df[ci].isin(class_list)].groupby(ci):
    patient_list = g[c_id]
    patient_ck = df_patient[df_patient['Patient ID'].isin(patient_list)]

    patient_ck.to_csv(f'result/{numClusters}/csv/{k}.csv')  # '{}.csv'.format(k)
    patient_ck.to_excel(f'result/{numClusters}/xlsx/{k}.xlsx')  # '{}.xlsx'.format(k)



# In[20]:



Z = linkage(df, 'ward')
# Plot title
plt.title('Hierarchical Clustering Dendrogram')

# Plot axis labels
plt.xlabel('sample index')
plt.ylabel('distance (Ward)')

# Make the dendrogram
# dendrogram(Z, labels=df.index, leaf_rotation=90)
# # Control number of clusters in the plot + add horizontal line.
# dendrogram(Z, color_threshold=240)
# dendrogram(Z, truncate_mode = 'lastp', p=4 ) # -> you will have 4 leaf at the bottom of the plot
dendrogram(Z, truncate_mode = 'lastp', p=8 ,orientation="left", labels=df.index) # -> you will have 4 leaf at the bottom of the plot

# plt.axhline(y=240, c='grey', lw=1, linestyle='dashed')
 

# Show the graph
plt.show()

