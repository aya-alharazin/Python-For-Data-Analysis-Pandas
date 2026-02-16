# Phase 2: Pandas Core - Sorting, Filtering & Selection

Once data is loaded and cleaned, the next crucial step is to effectively manipulate it to extract relevant information. This involves sorting data to identify trends, filtering to focus on specific subsets, and selecting particular columns or rows for analysis. This section will guide you through these essential data manipulation techniques in Pandas.

## 4.1 Beginner Level: Basic Sorting and Simple Filtering

At the beginner level, the focus is on straightforward methods to order your data and select rows based on simple conditions. These are fundamental operations for initial data exploration.

### Must-Know Methods:
*   `df[df["column"] == value]`: Basic boolean indexing to filter rows where a column matches a specific value.
*   `df.sort_values()`: Sorts a DataFrame by one or more columns.

### Explanation and Examples:

Let's use a simulated NGO project dataset to demonstrate basic sorting and filtering. Imagine `ngo_projects_cleaned.csv` with columns like `ProjectID`, `Region`, `Budget`, `Status`, and `StartDate`.

```python
import pandas as pd

# Simulate creating a cleaned CSV file
data = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000],
    'Status': ['Active', 'Completed', 'Active', 'Completed', 'Active', 'Pending', 'Active'],
    'StartDate': ['2023-01-15', '2023-02-01', '2023-03-10', '2023-04-05', '2023-05-20', '2023-06-01', '2023-07-10']
}
df_projects = pd.DataFrame(data)
df_projects.to_csv('ngo_projects_cleaned.csv', index=False)

# Load the cleaned CSV file
df = pd.read_csv('ngo_projects_cleaned.csv')
print("\nOriginal DataFrame:")
print(df)

# 1. Filtering: Select projects in 'East Africa'
projects_east_africa = df[df['Region'] == 'East Africa']
print("\nProjects in East Africa:")
print(projects_east_africa)

# 2. Filtering: Select projects with 'Active' status
active_projects = df[df['Status'] == 'Active']
print("\nActive Projects:")
print(active_projects)

# 3. Sorting: Sort projects by 'Budget' in ascending order
df_sorted_budget = df.sort_values(by='Budget')
print("\nProjects sorted by Budget (ascending):")
print(df_sorted_budget)

# 4. Sorting: Sort projects by 'StartDate' in descending order
df_sorted_date_desc = df.sort_values(by='StartDate', ascending=False)
print("\nProjects sorted by StartDate (descending):")
print(df_sorted_date_desc)
```

Basic filtering uses boolean indexing, where you provide a Series of `True`/`False` values to select rows. `df.sort_values()` is straightforward; `by` specifies the column(s) to sort by, and `ascending=False` changes the sort order to descending.

### Practice Task:

1.  Create a DataFrame named `beneficiary_records.csv` with columns `BeneficiaryID`, `Age`, `Gender`, `Location`, `AssistanceReceived` (e.g., 'Food', 'Shelter', 'Medical').
2.  Load `beneficiary_records.csv`.
3.  Filter the DataFrame to show only beneficiaries who received 'Food' assistance.
4.  Sort the original DataFrame by `Age` in ascending order.
5.  Filter the DataFrame to show only female beneficiaries, then sort these by `BeneficiaryID` in descending order.

## 4.2 Intermediate Level: Advanced Filtering with `.loc`, `.iloc` and Multiple Conditions

At the intermediate level, we introduce more powerful and flexible methods for selecting data, including label-based (`.loc`) and integer-location based (`.iloc`) indexing, and combining multiple filtering conditions.

### Must-Know Methods:
*   `.loc[]`: Label-based indexer for selection by label or boolean array.
*   `.iloc[]`: Integer-location based indexer for selection by positional integer.
*   Combining conditions: Using `&` (AND), `|` (OR), `~` (NOT) for complex boolean filtering.
*   `isin()`: Checks whether each element in the DataFrame is contained in values.

### Explanation and Examples:

Continuing with our `ngo_projects_cleaned.csv` DataFrame, let's explore advanced filtering and selection.

```python
import pandas as pd

df = pd.read_csv('ngo_projects_cleaned.csv')
print("\nOriginal DataFrame:")
print(df)

# 1. Filtering with multiple conditions: Active projects in 'East Africa' with Budget > 150000
filtered_projects = df[(df['Status'] == 'Active') & (df['Region'] == 'East Africa') & (df['Budget'] > 150000)]
print("\nActive projects in East Africa with Budget > 150000:")
print(filtered_projects)

# 2. Using .loc[] for label-based selection
# Select rows where 'Region' is 'South Asia' and only 'ProjectID' and 'Budget' columns
south_asia_budget = df.loc[df['Region'] == 'South Asia', ['ProjectID', 'Budget']]
print("\nProjectID and Budget for South Asia projects (using .loc[]):")
print(south_asia_budget)

# 3. Using .iloc[] for integer-location based selection
# Select the first 3 rows and columns at index 0, 2, 3 (ProjectID, Budget, Status)
first_three_rows_specific_cols = df.iloc[0:3, [0, 2, 3]]
print("\nFirst 3 rows, specific columns (using .iloc[]):")
print(first_three_rows_specific_cols)

# 4. Using isin(): Select projects in 'East Africa' or 'West Africa'
regional_projects = df[df['Region'].isin(['East Africa', 'West Africa'])]
print("\nProjects in East Africa or West Africa (using isin()):")
print(regional_projects)
```

`.loc[]` is highly versatile for selecting data by labels (column names, index labels) and is generally preferred for its clarity when working with named data. `.iloc[]` is useful when you need to select by integer position, which can be handy in loops or when the exact position is known. Combining conditions with `&`, `|`, `~` allows for highly specific data subsets, and `isin()` provides a concise way to filter for multiple values in a column.

### Practice Task:

1.  Load `beneficiary_records.csv` (from the beginner task) again.
2.  Filter the DataFrame to find beneficiaries who are either 'Male' and `Age` is less than 30, OR 'Female' and `AssistanceReceived` is 'Medical'.
3.  Using `.loc[]`, select the `BeneficiaryID` and `Location` for all beneficiaries who received 'Shelter' assistance.
4.  Using `.iloc[]`, select the last 5 rows and all columns except the first one.
5.  Find all beneficiaries whose `Location` is either 'Camp A' or 'Village B' using `isin()`.

## 4.3 Master Level: Boolean Indexing with Complex Logic and Query Method

At the master level, the focus is on constructing highly complex and efficient boolean indexing strategies, leveraging Pandas' `query()` method for more readable filtering, and understanding how index-based optimizations can improve performance for very large datasets.

### Must-Know Concepts:
*   **Boolean Indexing with Complex Logic**: Creating sophisticated boolean masks using multiple conditions, often involving calculations or string methods.
*   **`df.query()`**: A method for filtering DataFrames using a string expression, which can be more readable than traditional boolean indexing for complex conditions.
*   **Index-based Optimization**: Understanding how setting an appropriate index can speed up selection and filtering operations, especially for frequently accessed columns.

### Explanation and Examples:

Let's consider a scenario where we need to find projects that are 'Active', have a `Budget` above the average budget, and started in the first half of the year. We'll also explore `query()` and index optimization.

```python
import pandas as pd

df = pd.read_csv('ngo_projects_cleaned.csv')
df['StartDate'] = pd.to_datetime(df['StartDate']) # Ensure StartDate is datetime
print("\nOriginal DataFrame:")
print(df)

# 1. Boolean Indexing with Complex Logic
# Find active projects with budget above average and started in first half of the year
average_budget = df['Budget'].mean()
print(f"\nAverage Budget: {average_budget:.2f}")

complex_filtered_projects = df[
    (df['Status'] == 'Active') &
    (df['Budget'] > average_budget) &
    (df['StartDate'].dt.month <= 6) # Started in months 1-6
]
print("\nProjects matching complex criteria:")
print(complex_filtered_projects)

# 2. Using df.query() for more readable filtering
# Same conditions as above, but using query()
query_string = "Status == 'Active' and Budget > @average_budget and StartDate.dt.month <= 6"
query_filtered_projects = df.query(query_string)
print("\nProjects matching complex criteria (using .query()):")
print(query_filtered_projects)

# 3. Index-based Optimization (conceptual example)
# For very large datasets, setting an index on frequently filtered columns can speed up operations.
# Let's set 'Region' as an index and then filter.

df_indexed = df.set_index('Region')
print("\nDataFrame with 'Region' as index:")
print(df_indexed)

# Now, filtering by index is often faster
indexed_east_africa = df_indexed.loc['East Africa']
print("\nProjects in East Africa (from indexed DataFrame):")
print(indexed_east_africa)

# Resetting index if needed
df_indexed = df_indexed.reset_index()
```

`df.query()` offers a more SQL-like syntax for filtering, which can significantly improve readability for complex conditions, especially when involving variables (prefixed with `@`). While not always necessary for smaller datasets, understanding index-based optimization is crucial for performance tuning on large-scale data. When a column is set as an index, Pandas can use optimized data structures for faster lookups.

### Practice Task:

1.  Create a large DataFrame (e.g., 100,000 rows) with columns `TransactionID`, `Amount`, `Currency`, `Timestamp`, `Processor`.
2.  Calculate the median `Amount` for transactions.
3.  Using complex boolean indexing, filter for transactions where the `Currency` is 'USD', the `Amount` is greater than the median `Amount`, and the `Timestamp` falls on a weekend.
4.  Repeat the previous filtering task using the `df.query()` method.
5.  Set `Processor` as the index of your DataFrame. Then, filter for all transactions processed by 'Stripe' using `.loc[]` on the indexed DataFrame. Compare this with filtering the non-indexed DataFrame (conceptually, as performance difference might not be visible on small data).
