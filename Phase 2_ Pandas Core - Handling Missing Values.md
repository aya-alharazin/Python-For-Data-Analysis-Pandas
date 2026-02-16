# Phase 2: Pandas Core - Handling Missing Values

Missing values are a common challenge in real-world datasets, especially in humanitarian data which can be collected under difficult circumstances. Effectively handling these missing values is crucial for accurate analysis and reliable insights. This section will guide you through various strategies for identifying and managing missing data in Pandas.

## 2.1 Beginner Level: Identifying and Basic Removal

At the beginner level, the focus is on recognizing missing values and performing straightforward removal operations. This is often the first step in cleaning a dataset.

### Must-Know Methods:
*   `df.isna()`: Returns a boolean DataFrame indicating whether each element is `NaN` (Not a Number) or `None`.
*   `df.dropna()`: Removes rows or columns containing missing values.

### Explanation and Examples:

Let's use a simulated NGO dataset with some missing values to demonstrate these methods. Imagine `beneficiary_data.csv` now includes some missing `Age` or `AssistanceType` values.

```python
import pandas as pd
import numpy as np

# Simulate creating a CSV file with missing values
data = {
    'BeneficiaryID': [1, 2, 3, 4, 5, 6, 7],
    'Age': [25, 34, np.nan, 45, 19, np.nan, 50],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Location': ['Camp A', 'Village B', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A'],
    'AssistanceType': ['Food', 'Shelter', np.nan, 'Food', 'Medical', 'Shelter', 'Food']
}
df_missing = pd.DataFrame(data)
df_missing.to_csv('beneficiary_data_missing.csv', index=False)

# Load the CSV file
df = pd.read_csv('beneficiary_data_missing.csv')
print("\nOriginal DataFrame:")
print(df)

# 1. Identifying missing values
print("\nDataFrame indicating missing values (df.isna()):")
print(df.isna())

# You can also sum them up to get a count per column
print("\nCount of missing values per column:")
print(df.isna().sum())

# 2. Removing rows with any missing values
df_cleaned_rows = df.dropna()
print("\nDataFrame after dropping rows with any missing values (df.dropna()):")
print(df_cleaned_rows)

# 3. Removing columns with any missing values (use with caution!)
df_cleaned_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing values (df.dropna(axis=1)):")
print(df_cleaned_cols)
```

`df.isna()` is excellent for quickly seeing where missing values are located. `df.dropna()` is a straightforward way to remove incomplete records, but be aware that it can lead to significant data loss if many rows have missing values.

### Practice Task:

1.  Create a CSV file named `project_updates.csv` with columns like `UpdateID`, `ProjectID`, `Date`, `Status`, `Notes`. Intentionally leave some values missing in `Status` and `Notes`.
2.  Load `project_updates.csv` into a DataFrame.
3.  Identify and print the total count of missing values for each column.
4.  Create a new DataFrame by dropping all rows that have any missing values. Print the shape of the original and new DataFrames to see how many rows were removed.

## 2.2 Intermediate Level: Strategic Imputation

Instead of simply removing data, imputation involves filling in missing values with estimated or calculated values. This level focuses on common and effective imputation strategies.

### Must-Know Methods:
*   `df.fillna()`: Fills `NaN` values using a specified method (e.g., a constant, mean, median, or previous/next valid observation).
*   `method='ffill'` (forward fill): Propagates the last valid observation forward to next `NaN`.
*   `method='bfill'` (backward fill): Propagates the next valid observation backward to previous `NaN`.

### Explanation and Examples:

Using our `beneficiary_data_missing.csv` DataFrame, let's apply different `fillna()` strategies.

```python
import pandas as pd
import numpy as np

df = pd.read_csv('beneficiary_data_missing.csv')
print("\nOriginal DataFrame:")
print(df)

# 1. Filling missing 'Age' with the mean age
mean_age = df['Age'].mean()
df_filled_mean_age = df.copy()
df_filled_mean_age['Age'] = df_filled_mean_age['Age'].fillna(mean_age)
print(f"\nDataFrame after filling missing 'Age' with mean ({mean_age:.2f}):")
print(df_filled_mean_age)

# 2. Filling missing 'AssistanceType' with a constant value
df_filled_constant = df.copy()
df_filled_constant['AssistanceType'] = df_filled_constant['AssistanceType'].fillna('Unknown')
print("\nDataFrame after filling missing 'AssistanceType' with 'Unknown':")
print(df_filled_constant)

# 3. Forward fill for 'Age' (propagates last valid observation forward)
df_ffill = df.copy()
df_ffill['Age'] = df_ffill['Age'].fillna(method='ffill')
print("\nDataFrame after forward fill for 'Age':")
print(df_ffill)

# 4. Backward fill for 'AssistanceType' (propagates next valid observation backward)
df_bfill = df.copy()
df_bfill['AssistanceType'] = df_bfill['AssistanceType'].fillna(method='bfill')
print("\nDataFrame after backward fill for 'AssistanceType':")
print(df_bfill)
```

Choosing the right imputation method depends heavily on the nature of your data and the reason for missingness. For numerical data, mean or median imputation is common. For categorical data, a constant like 'Unknown' or the mode can be used. Forward or backward fill is useful for time-series or ordered data where the previous or next value is a reasonable estimate.

### Practice Task:

1.  Load `project_updates.csv` (from the beginner task) again.
2.  Fill any missing `Status` values with the most frequent status (mode).
3.  Fill any missing `Notes` values with the string "No update provided".
4.  Verify that there are no more missing values in these columns using `isna().sum()`.

## 2.3 Master Level: Conditional Imputation and Pattern Analysis

At the master level, handling missing values becomes more sophisticated, involving conditional imputation based on other columns and analyzing patterns of missingness to understand underlying issues. This often requires domain knowledge and careful consideration.

### Must-Know Concepts:
*   **Conditional Imputation**: Filling missing values based on the values of other columns (e.g., imputing age based on location or gender groups).
*   **Identifying Patterns in Missingness**: Using visualization or statistical tests to understand if missing data is random or systematic.

### Explanation and Examples:

Let's consider a scenario where `Age` might be missing more frequently for certain `Location`s or `Gender`s. We can impute `Age` based on the mean `Age` within each `Location` group.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reload the DataFrame with missing values
df = pd.read_csv('beneficiary_data_missing.csv')

print("\nOriginal DataFrame:")
print(df)

# 1. Conditional Imputation: Fill missing 'Age' based on the mean 'Age' per 'Location'
# Calculate mean age for each location
mean_age_per_location = df.groupby('Location')['Age'].transform('mean')

df_conditional_age = df.copy()
df_conditional_age['Age'] = df_conditional_age['Age'].fillna(mean_age_per_location)
print("\nDataFrame after conditional imputation of 'Age' by 'Location':")
print(df_conditional_age)

# 2. Identifying Patterns in Missingness (Visual Example)
# Let's create a more complex missing data pattern for demonstration
df_complex_missing = df.copy()
df_complex_missing.loc[df_complex_missing['Gender'] == 'Male', 'AssistanceType'] = np.nan
df_complex_missing.loc[df_complex_missing['Location'] == 'Camp B', 'Age'] = np.nan

print("\nDataFrame with complex missing patterns:")
print(df_complex_missing)

# Visualize missingness using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df_complex_missing.isna(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.savefig('missing_values_heatmap.png')
print("\nMissing values heatmap saved as 'missing_values_heatmap.png'")
# plt.show() # Uncomment to display plot if running locally

# Another way to check for patterns: group by a column and see missing counts
print("\nMissing 'Age' count by 'Gender':")
print(df_complex_missing.groupby('Gender')['Age'].apply(lambda x: x.isna().sum()))

print("\nMissing 'AssistanceType' count by 'Location':")
print(df_complex_missing.groupby('Location')['AssistanceType'].apply(lambda x: x.isna().sum()))
```

Conditional imputation is powerful because it leverages existing data relationships to make more informed estimates for missing values. For instance, if you know that the average age of beneficiaries differs significantly between various camps, imputing based on the camp's average is more accurate than using the overall average.

Visualizing missingness (e.g., with a heatmap) can reveal patterns that suggest systematic issues in data collection. For example, if a specific column is always missing when another column has a certain value, it indicates a non-random missing data mechanism that might need further investigation or a more tailored imputation strategy.

### Practice Task:

1.  Create a new DataFrame, `health_data.csv`, with columns like `PatientID`, `Age`, `Weight`, `Diagnosis`, `Medication`. Intentionally create a pattern where `Medication` is often missing for patients with a specific `Diagnosis` (e.g., 'Flu').
2.  Load `health_data.csv`.
3.  Perform conditional imputation: fill missing `Weight` values based on the mean `Weight` for each `Diagnosis` group.
4.  Generate a heatmap of missing values for `health_data.csv` and analyze if it reveals the intentional missing pattern you created. Explain your findings.
