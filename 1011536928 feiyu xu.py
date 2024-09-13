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

# B: In some cases deleting the entire column will be more suitable to simplify the entire column, then del df('col')would be a better option. For example, in some data sets, some columns are irrelevant to contribute to the data system. Then deleting the entire column would be a better idea.

# C. It reduced the frame size and could avoid accidentally deleting relevant rows.

# D: Before: The data set has missing values in some rows and columns.
# After: The data set is simplified and has removed the irrelevant column.

#  8. Give brief explanations in your own words for any requested answers to the questions below
# 
# > This problem will guide you through exploring how to use a ChatBot to troubleshoot code using the "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" data set 
# > 
# > To initialially constrain the scope of the reponses from your ChatBot, start a new ChatBot session with the following slight variation on the initial prompting approach from "2" above
# > - "I am going to do some initial simple summary analyses on the titanic data set I've downloaded (https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv) which has some missing values, and I'd like to get your help understanding the code I'm using and the analysis it's performing"
#         
# 1. Use your ChatBot session to understand what `df.groupby("col1")["col2"].describe()` does and then demonstrate and explain this using a different example from the "titanic" data set other than what the ChatBot automatically provide for you
#     
# > If needed, you can help guide the ChatBot by showing it the code you've used to download the data **AND provide it with the names of the columns** using either a summary of the data with `df.describe()` or just `df.columns` as demonstrated [here](../CHATLOG/COP/00017_copilot_groupby.md)
#     
# 2. Assuming you've not yet removed missing values in the manner of question "7" above, `df.describe()` would have different values in the `count` value for different data columns depending on the missingness present in the original data.  Why do these capture something fundamentally different from the values in the `count` that result from doing something like `df.groupby("col1")["col2"].describe()`?
# 
# > Questions "4" and "6" above address how missing values are handled by `df.describe()` (which is reflected in the `count` output of this method); but, `count` in conjunction with `group_by` has another primary function that's more important than addressing missing values (although missing data could still play a role here).
# 
# 3. Intentionally introduce the following errors into your code and report your opinion as to whether it's easier to (a) work in a ChatBot session to fix the errors, or (b) use google to search for and fix errors: first share the errors you get in the ChatBot session and see if you can work with ChatBot to troubleshoot and fix the coding errors, and then see if you think a google search for the error provides the necessary toubleshooting help more quickly than ChatGPT<br><br>
#     
#     1. Forget to include `import pandas as pd` in your code 
#        <br> 
#        Use Kernel->Restart from the notebook menu to restart the jupyter notebook session unload imported libraries and start over so you can create this error
#        <br><br>
#        When python has an error, it sometimes provides a lot of "stack trace" output, but that's not usually very important for troubleshooting. For this problem for example, all you need to share with ChatGPT or search on google is `"NameError: name 'pd' is not defined"`<br><br>
# 
#     2. Mistype "titanic.csv" as "titanics.csv"
#        <br> 
#        If ChatBot troubleshooting is based on downloading the file, just replace the whole url with "titanics.csv" and try to troubleshoot the subsequent `FileNotFoundError: [Errno 2] No such file or directory: 'titanics.csv'` (assuming the file is indeed not present)
#        <br><br>
#        Explore introducing typos into a couple other parts of the url and note the slightly different errors this produces<br><br>
#       
#     3. Try to use a dataframe before it's been assigned into the variable
#        <br> 
#        You can simulate this by just misnaming the variable. For example, if you should write `df.groupby("col1")["col2"].describe()` based on how you loaded the data, then instead write `DF.groupby("col1")["col2"].describe()`
#        <br><br>
#        Make sure you've fixed your file name so that's not the error any more<br><br>
#         
#     4. Forget one of the parentheses somewhere the code
#        <br>
#        For example, if the code should be `pd.read_csv(url)` the change it to `pd.read_csv(url`<br><br>
#         
#     5. Mistype one of the names of the chained functions with the code 
#        <br>
#        For example, try something like `df.group_by("col1")["col2"].describe()` and `df.groupby("col1")["col2"].describle()`<br><br>
#         
#     6. Use a column name that's not in your data for the `groupby` and column selection 
#        <br>
#        For example, try capitalizing the columns for example replacing "sex" with "Sex" in `titanic_df.groupby("sex")["age"].describe()`, and then instead introducing the same error of "age"<br><br>
#         
#     7. Forget to put the column name as a string in quotes for the `groupby` and column selection, and see if the ChatBot and google are still as helpful as they were for the previous question
#        <br>
#        For example, something like `titanic_df.groupby(sex)["age"].describe()`, and then `titanic_df.groupby("sex")[age].describe()`
#         

# In[18]:


#1
import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'pclass' and describe 'age'
summary = df.groupby("pclass")["age"].describe()

print(summary)


# #2 df.describe() Provides an understanding of the missing part across the entire data set while df. group by ("col1")["col2"] would be more helpful if we want to focus on the messiness of a specific group.

# 8,3  For me, as a beginner in Python, it would be much easier and more direct to use ChatGPT as a tool to debug any of the problems the code has. As a beginner, it's hard to use Google Search to fix your problems because Google Search cannot respond to you with a fixed code but helps you to point out where the problem is. However, the ChatGPT pointed out the problem while responding with the debugged version of your code which I believe is more user-friendly.
