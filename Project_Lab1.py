#!/usr/bin/env python
# coding: utf-8

# # Introduction (Unit I)

# ## 1.- Import data

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt


# In[2]:


#Load data from csv and store it in dataframe
data = pd.read_csv("HCV-Egy-Data.csv") #We can change this database

# We show the first 
data.head() # Return the first n rows.


# ## 2.- Data set description - "Hepatitis C Virus (HCV) for Egyptian patients" 

# Egyptian patients who underwent treatment dosages for HCV about 18 months. Discretization should be applied based on expert recommendations; there is an attached file shows how.
# 
# 
# 
# *Age: Age
# *Gender Gender
# *BMI Body Mass Index
# Fever Fever
# Nausea/Vomting Nausea/Vomting
# Headache Headache
# Diarrhea Diarrhea
# Fatigue & generalized bone ache Fatigue & generalized bone ache
# Jaundice Jaundice
# Epigastric pain Epigastric pain
# WBC White blood cell
# RBC red blood cells
# HGB Hemoglobin
# Plat Platelets
# AST 1 aspartate transaminase ratio
# ALT 1 alanine transaminase ratio 1 week
# ALT 4 alanine transaminase ratio 12 weeks
# ALT 12 alanine transaminase ratio 4 weeks
# ALT 24 alanine transaminase ratio 24 weeks
# ALT 36 alanine transaminase ratio 36 weeks
# ALT 48 alanine transaminase ratio 48 weeks
# ALT after 24 w alanine transaminase ratio 24 weeks
# RNA Base RNA Base
# RNA 4 RNA 4
# RNA 12 RNA 12
# RNA EOT RNA end-of-treatment
# RNA EF RNA Elongation Factor
# Baseline histological Grading Baseline histological Grading
# Baselinehistological staging Baselinehistological staging

# #### a) We indicate the type each variable is (numerical, categorical, etc.).

# In[3]:


data.dtypes


# #### b) Columns name

# In[4]:


data.columns


# In[ ]:





# #### c) Adding a categorical variable (from 'Baselinehistological staging')

# In[ ]:


category=pd.cut(data.Age,bins=[0,2,17,40,65,99],labels=['Baby','Child','Adult1', 'Adult2','Elderly'])
data.insert(8,'AgeCategory', category) # In the 8th position.
data.columns


# In[ ]:





# In[ ]:




