import pandas as pd





#.LOC
df = ['column1','column2']

# Example 1: Select all rows and columns
df.loc[:, :]
# This selects every row and column in the dataframe

# Example 2: Select specific columns for all rows
df.loc[:, ['column1', 'column2']]
# Selects only 'column1' and 'column2' from all rows

# Example 3: Select rows based on a condition
df.loc[df['column'] > 10, :]
# Selects all rows where the values in 'column' are greater than 10

# Example 4: Select specific row and column
df.loc['row_label', 'column_label']
# Selects the value at the intersection of 'row_label' and 'column_label'

# Example 5: Select multiple rows using a list of labels
df.loc[['row_label1', 'row_label2'], :]
# Selects the rows 'row_label1' and 'row_label2', along with all columns

# Example 6: Combine conditions for row selection
df.loc[(df['column1'] > 10) & (df['column2'] == 'value'), :]
# Selects rows where 'column1' is greater than 10 and 'column2' is 'value'

# Example 7: Selecting a range of rows
df.loc['row_start':'row_end', :]
# Selects rows from 'row_start' to 'row_end' (inclusive), and all columns

# Example 8: Select specific rows and specific columns
df.loc[df['column'] > 10, ['column1', 'column2']]
# Selects 'column1' and 'column2' from rows where 'column' is greater than 10




# Grouping with .groupby()

# Example 1: Group by a single column and perform aggregation
df.groupby('column1').agg({'column2': 'mean'})
# Groups by 'column1' and calculates the mean of 'column2' for each group

# Example 2: Group by multiple columns and perform aggregation
df.groupby(['column1', 'column3']).agg({'column2': 'sum', 'column4': 'count'})
# Groups by both 'column1' and 'column3' and calculates the sum of 'column2' and the count of 'column4' for each group

# Example 3: Group by a single column and apply multiple aggregation functions
df.groupby('column1').agg({'column2': ['mean', 'max']})
# Groups by 'column1' and calculates both the mean and max of 'column2' for each group

# Example 4: Group by a single column and apply custom aggregation functions
custom_agg = lambda x: x.max() - x.min()
df.groupby('column1').agg({'column2': custom_agg})
# Groups by 'column1' and calculates the custom aggregation function for 'column2' for each group

# Example 5: Group by a single column and apply different aggregation functions to different columns
agg_dict = {'column2': 'mean', 'column3': 'sum'}
df.groupby('column1').agg(agg_dict)
# Groups by 'column1' and calculates the mean of 'column2' and the sum of 'column3' for each group

# Example 6: Group by a single column and apply aggregation to all numeric columns
df.groupby('column1').mean()
# Groups by 'column1' and calculates the mean for all numeric columns in each group

# Example 7: Group by a single column and apply aggregation to specific columns using .agg()
df.groupby('column1').agg({'column2': 'mean', 'column3': 'sum'})
# Groups by 'column1' and calculates the mean of 'column2' and the sum of 'column3' for each group

# Example 8: Group by multiple columns and apply aggregation to specific columns using .agg()
df.groupby(['column1', 'column3']).agg({'column2': 'mean', 'column4': 'max'})
# Groups by both 'column1' and 'column3' and calculates the mean of 'column2' and the max of 'column4' for each group
