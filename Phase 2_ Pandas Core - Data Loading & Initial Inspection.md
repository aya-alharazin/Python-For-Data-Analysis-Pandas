# Phase 2: Pandas Core - Data Loading & Initial Inspection

This section will guide you through the fundamental steps of loading data into Pandas DataFrames and performing initial inspections to understand its structure and content. We will progress from basic operations to more advanced techniques for efficient data handling.

## 1.1 Beginner Level: Getting Started with Data

At the beginner level, the focus is on successfully importing data and getting a quick overview. This is crucial for any data analysis project, as it forms the foundation for all subsequent steps.

### Must-Know Methods:
*   `pd.read_csv()`: The primary function for reading comma-separated values (CSV) files into a DataFrame.
*   `df.head()`: Displays the first 5 rows of the DataFrame, useful for a quick peek at the data.
*   `df.tail()`: Displays the last 5 rows of the DataFrame, helpful for checking data integrity at the end of the file.

### Explanation and Examples:

To begin, we'll simulate loading a CSV file containing basic NGO project data. Imagine a file named `ngo_projects.csv` with columns like `ProjectID`, `Region`, `StartDate`, `EndDate`, and `Budget`.

```python
import pandas as pd

# Simulate creating a CSV file for demonstration
data = {
    'ProjectID': [101, 102, 103, 104, 105],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
    'StartDate': ['2023-01-15', '2023-02-01', '2023-03-10', '2023-04-05', '2023-05-20'],
    'EndDate': ['2023-06-30', '2023-07-15', '2023-08-20', '2023-09-10', '2023-10-30'],
    'Budget': [150000, 200000, 120000, 180000, 250000]
}
df_sample = pd.DataFrame(data)
df_sample.to_csv('ngo_projects.csv', index=False)

# 1. Loading a CSV file
df = pd.read_csv('ngo_projects.csv')
print("\nDataFrame loaded successfully:")

# 2. Inspecting the first few rows
print("\nFirst 5 rows (df.head()):")
print(df.head())

# 3. Inspecting the last few rows
print("\nLast 5 rows (df.tail()):")
print(df.tail())
```

### Practice Task:

1.  Create a new CSV file named `beneficiary_data.csv` with at least 5 rows and columns like `BeneficiaryID`, `Age`, `Gender`, `Location`, `AssistanceType`.
2.  Load this `beneficiary_data.csv` into a Pandas DataFrame.
3.  Display the first 3 rows and the last 2 rows of your new DataFrame.

## 1.2 Intermediate Level: Deeper Data Understanding

Moving beyond basic loading, the intermediate level focuses on gaining a more comprehensive understanding of your dataset's characteristics, including data types, non-null values, and summary statistics. This helps in identifying potential issues early on.

### Must-Know Methods:
*   `df.info()`: Provides a concise summary of a DataFrame, including data types, non-null values, and memory usage. Essential for checking data completeness and types.
*   `df.describe()`: Generates descriptive statistics of numerical columns, offering insights into central tendency, dispersion, and shape of the distribution.

### Explanation and Examples:

Continuing with our `ngo_projects.csv` DataFrame, we'll now use `info()` and `describe()` to get a deeper understanding.

```python
import pandas as pd

# Load the previously created CSV file
df = pd.read_csv('ngo_projects.csv')

# 1. Getting a concise summary of the DataFrame
print("\nDataFrame Information (df.info()):")
df.info()

# 2. Generating descriptive statistics for numerical columns
print("\nDescriptive Statistics (df.describe()):")
print(df.describe())
```

From `df.info()`, you can see the data types (e.g., `int64`, `object`) and the number of non-null entries for each column. This immediately tells us if there are missing values (if non-null count is less than total entries) or if a column is not in the expected data type (e.g., dates as `object` instead of `datetime`).

`df.describe()` provides statistics like `mean`, `std`, `min`, `max`, and quartiles for numerical columns. For instance, in the `Budget` column, you can quickly see the average budget, the range of budgets, and how they are distributed.

### Practice Task:

1.  Using your `beneficiary_data.csv` DataFrame from the beginner task, apply `df.info()` to check data types and non-null counts.
2.  Use `df.describe()` to get descriptive statistics for any numerical columns (e.g., `Age`). What insights can you gather from these outputs?

## 1.3 Master Level: Advanced Loading and Efficiency

At the master level, the focus shifts to optimizing data loading for large datasets and handling diverse data sources. This includes strategies for memory efficiency and reading data from non-CSV formats.

### Must-Know Concepts:
*   **Memory Optimization with `dtype`**: Specifying data types during `read_csv()` can significantly reduce memory usage, especially for columns with a limited range of values (e.g., `int8`, `category`).
*   **`chunksize` for Large Files**: Reading large files in chunks prevents memory overload, allowing processing of data larger than available RAM.
*   **Reading from other sources**: Understanding how to load data from databases (SQL), APIs, or other file formats (e.g., Excel, JSON).

### Explanation and Examples:

Let's explore memory optimization and chunking. For reading from SQL/APIs, the specific implementation depends on the database/API, but the principle is to use Pandas functions like `pd.read_sql()` or `requests` library combined with `pd.DataFrame()`.

```python
import pandas as pd
import numpy as np

# Simulate a larger CSV file for demonstration of memory optimization
large_data = {
    'ProjectID': np.arange(1, 100001),
    'Region': np.random.choice(['East Africa', 'South Asia', 'West Africa', 'Latin America'], 100000),
    'Status': np.random.choice(['Active', 'Completed', 'Pending'], 100000),
    'Budget': np.random.randint(50000, 500000, 100000)
}
df_large_sample = pd.DataFrame(large_data)
df_large_sample.to_csv('large_ngo_projects.csv', index=False)

# 1. Loading with optimized dtypes
# Before optimization, let's check memory usage
df_unoptimized = pd.read_csv('large_ngo_projects.csv')
print("\nMemory usage without optimization:")
print(df_unoptimized.info(memory_usage='deep'))

# Now, optimize dtypes. 'Region' and 'Status' can be 'category' for memory efficiency.
# 'ProjectID' can be 'int32' if max ID fits.
optimized_dtypes = {
    'ProjectID': 'int32',
    'Region': 'category',
    'Status': 'category',
    'Budget': 'int32'
}
df_optimized = pd.read_csv('large_ngo_projects.csv', dtype=optimized_dtypes)
print("\nMemory usage with optimization:")
print(df_optimized.info(memory_usage='deep'))

# 2. Reading large files in chunks
print("\nReading large_ngo_projects.csv in chunks of 10000 rows:")
chunk_size = 10000
for i, chunk in enumerate(pd.read_csv('large_ngo_projects.csv', chunksize=chunk_size, dtype=optimized_dtypes)):
    print(f"Processing chunk {i+1}, shape: {chunk.shape}")
    # Perform operations on each chunk, e.g., aggregation
    # total_budget_in_chunk = chunk['Budget'].sum()
    # print(f"Total budget in chunk {i+1}: {total_budget_in_chunk}")

# Example of reading from a simulated SQL database (conceptual)
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///my_ngo_db.db')
# df_sql = pd.read_sql('SELECT * FROM projects', engine)
# print("\nDataFrame loaded from SQL (conceptual):")
# print(df_sql.head())
```

Notice the significant reduction in memory usage when `dtype` is specified. For `chunksize`, this approach is ideal when you need to process data that doesn't fit into memory entirely, allowing you to perform operations iteratively.

### Practice Task:

1.  Create a very large CSV file (e.g., 100,000 rows or more) with diverse data types, similar to `large_ngo_projects.csv`.
2.  Load this file without specifying `dtype` and note its memory usage using `df.info(memory_usage='deep')`.
3.  Reload the same file, but this time, specify appropriate `dtype` for each column to optimize memory. Compare the memory usage.
4.  Implement reading this large file in chunks of 20,000 rows. For each chunk, calculate the average `Budget` and print it.
