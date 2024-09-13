#!/usr/bin/env python
# coding: utf-8

# #### 1. Pick one of the datasets from the ChatBot session(s) of the **TUT demo** (or from your own ChatBot session if you wish) and use the code produced through the ChatBot interactions to import the data and confirm that the dataset has missing values<br>

# In[9]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# 2. Start a new ChatBot session with an initial prompt introducing the dataset you're using and request help to determine how many columns and rows of data a `pandas` DataFrame has, and then
#    1. use code provided in your ChatBot session to print out the number of rows and columns of the dataset; and,  
#    2. write your own general definitions of the meaning of "observations" and "variables" based on asking the ChatBot to explain these terms in the context of your dataset<br>
# 

# In[3]:


df.shape#question A


# Observation in coding refers to an exact data point you actually recorded from a certain experiment or a study. It produced the data in any statistical survey.
# Variable refers to the things you are supposed to collect from an experiment. For example to study how much money a people make a year. People are the observation and money is variable. #question B

# 3. Ask the ChatBot how you can provide simple summaries of the columns in the dataset and use the suggested code to provide these summaries for your dataset<br>

# In[12]:


df = pd.read_csv(url, encoding="ISO-8859-1")

# Get basic summary statistics for numeric columns
print("Summary Statistics for Numeric Columns:")
print(df.describe())

# Get information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Get value counts for categorical columns
print("\nValue Counts for Categorical Columns:")
for column in df.select_dtypes(include='object').columns:
    print(f'\nValue counts for {column}:')
    print(df[column].value_counts())


# 4. If the dataset you're using has (a) non-numeric variables and (b) missing values in numeric variables, explain (perhaps using help from a ChatBot if needed) the discrepancies between size of the dataset given by `df.shape` and what is reported by `df.describe()` with respect to (a) the number of columns it analyzes and (b) the values it reports in the "count" column<br>
# 

# In[16]:


# Get the shape of the DataFrame
print("DataFrame Shape:", df.shape)  # Output: (1000, 5)

# Get summary statistics
print("\nDescribe Output:")
print(df.describe())

# Check non-numeric columns
print("\nNon-Numeric Columns:")
print(df.select_dtypes(include='object').columns)

# Count of non-null values for each column
print("\nCount of Non-Null Values in Each Column:")
print(df.count())


#  5. Use your ChatBot session to help understand the difference between the following and then provide your own paraphrasing summarization of that difference
#     - an "attribute", such as `df.shape` which does not end with `()`
# - and a "method", such as `df.describe()` which does end with `()` 

# Attributes are more like the property of a certain object, it doesn't apply any additional movement on that object. However, the method would modify the object by using actions or calculations. 

#  6.The `df.describe()` method provides the 'count', 'mean', 'std', 'min', '25%', '50%', '75%', and 'max' summary statistics for each variable it analyzes. Give the definitions (perhaps using help from the ChatBot if needed) of each of these summary statistics<br>
# 

# Count: The valid rows in a column.
# Mean: The average value of data in a column.
# Std: The standard deviation of the values in a column.
# Min: The smallest value in a column.
# 25%: There are 25% of the values are lower than that value in a column.
# 50%: The middle value of the data so-called median.
# 75%:There are 75% of the values that are lower than that value in a colomn.
# Max: The biggest value in the column.
# 

# 7. Missing data can be considered "across rows" or "down columns".  Consider how `df.dropna()` or `del df['col']` should be applied to most efficiently use the available non-missing data in your dataset and briefly answer the following questions in your own words
# 
#     1. Provide an example of a "use case" in which using `df.dropna()` might be peferred over using `del df['col']`<br><br>
#     
#     2. Provide an example of "the opposite use case" in which using `del df['col']` might be preferred over using `df.dropna()` <br><br>
#     
#     3. Discuss why applying `del df['col']` before `df.dropna()` when both are used together could be important<br><br>
#     
#     4. Remove all missing data from one of the datasets you're considering using some combination of `del df['col']` and/or `df.dropna()` and give a justification for your approach, including a "before and after" report of the results of your approach for your dataset.<br><br>

# A: When you simply want to remove some rows with missing values, df.dropna()will be a better option than del df('col') because the second one will delete the entire column.

# B: In some cases delete the entire column will be more suitable to simplifie the entire column, then del df('col')would be a better option.

# C. It reduced the frame size and could avoid with accidentally deleted on relevant rows.
