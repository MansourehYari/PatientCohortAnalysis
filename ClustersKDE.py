#!/usr/bin/env python
# coding: utf-8

# In[8]:


# importing necessary libraries as the environment has been reset
import pandas as pd
import seaborn as sns
from datetime import timedelta
import matplotlib.pyplot as plt

# Function to convert time to hours
def time_to_hours(time_str):
    # Convert the time string to a datetime object
    time_value = pd.to_datetime(time_str, format='%H:%M:%S', errors='coerce')
    # Extract the hours as a fractional value if time_value is not NaT
    if pd.notnull(time_value):
        hours = time_value.hour + time_value.minute / 60 + time_value.second / 3600
    else:
        hours = pd.NaT
    return hours

# Paths of the uploaded Excel files
file_paths = [
    'dataset0.xlsx',
    'dataset1.xlsx',
    'dataset2.xlsx',
    'dataset3.xlsx',
    'dataset4.xlsx'
]

# Initialize a list to store the 'b-a' cluster hours data from each dataset
b_a_cluster_hours_list = []

# Process each file
for file_path in file_paths:
    # Load the dataset
    df_temp = pd.read_excel(file_path)
    
    # Convert the 'hour' column for 'b-a' cluster to hours
    b_a_hours = df_temp.iloc[:, 1].apply(time_to_hours)  # Assuming the 'hour' column for 'b-a' is the second column
    
    # Append to the list
    b_a_cluster_hours_list.append(b_a_hours)

# Now, we plot the KDE for the 'b-a' cluster from each dataset
plt.figure(figsize=(12, 8))

# Define a list of colors for the plots
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Plotting each dataset's 'b-a' cluster KDE
for i, (b_a_hours, color) in enumerate(zip(b_a_cluster_hours_list, colors)):
    sns.kdeplot(b_a_hours.dropna(), label=f'Dataset {i}', color=color)

# Add legend and labels
plt.legend(title='Dataset')
plt.xlabel('Time after admission (hours)')
plt.ylabel('Probability Density Function')

# Display the plot with a title
plt.title('KDE of b-a Cluster Across Different Datasets')
plt.show()


# In[7]:


# Since the environment was reset, we need to redefine the time_to_hours function and re-import pandas and seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to convert time to hours
def time_to_hours(time_str):
    # Convert the time string to a datetime object
    time_value = pd.to_datetime(time_str, format='%H:%M:%S', errors='coerce')
    # Extract the hours as a fractional value if time_value is not NaT
    if pd.notnull(time_value):
        hours = time_value.hour + time_value.minute / 60 + time_value.second / 3600
    else:
        hours = pd.NaT
    return hours

# Paths of the uploaded Excel files
file_paths = [
    'dataset0.xlsx',
    'dataset1.xlsx',
    'dataset2.xlsx',
    'dataset3.xlsx',
    'dataset4.xlsx'
]


# According to the provided image, the 'hour' columns for each cluster are in the following order:
cluster_hour_columns = {
    'b-a': 1,  # Column B
    'c-b': 4,  # Column D
    'd-b': 7,  # Column F
    'e-b': 10,  # Column H
    'f-b': 13   # Column J
}

# Initialize a dictionary to store the 'hour' data for each cluster from each dataset
cluster_data = {cluster: [] for cluster in cluster_hour_columns.keys()}

# Load and process the data for each cluster from each file
for cluster, hour_col in cluster_hour_columns.items():
    for file_path in file_paths:
        # Load the dataset
        df_temp = pd.read_excel(file_path)
        
        # Convert the 'hour' column for the cluster to hours
        cluster_hours = df_temp.iloc[:, hour_col].apply(time_to_hours)
        
        # Append the processed hours to the cluster's data list
        cluster_data[cluster].append(cluster_hours)

# Set up the figure for multiple subplots - one for each cluster
fig, axes = plt.subplots(nrows=len(cluster_hour_columns), ncols=1, figsize=(12, 20), sharex=True)

# Plotting each cluster's KDE on a separate subplot
for ax, (cluster, data_list) in zip(axes.flatten(), cluster_data.items()):
    for i, data in enumerate(data_list):
        sns.kdeplot(data.dropna(), label=f'Dataset {i}', ax=ax, fill=True)
    ax.set_title(f'KDE Plot for {cluster} Cluster')
    ax.set_xlabel('Hours after admission')
    ax.set_ylabel('Density')
    ax.legend()

# Adjust layout
plt.tight_layout()
plt.show()

