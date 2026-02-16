# Phase 3: Pandas Analysis - Grouping & Aggregation

Grouping and aggregation are cornerstone techniques in data analysis, allowing you to summarize data by categories and derive meaningful insights. In the context of NGO data, this could mean understanding aid distribution by region, beneficiary demographics by project, or the average budget per assistance type. This section will guide you from basic grouping to advanced custom aggregations.

## 1.1 Beginner Level: Basic Grouping and Single Aggregation

At the beginner level, the focus is on understanding how to group data by one or more columns and apply a single aggregation function (like sum, mean, count) to the grouped data. This is the foundation for summarizing your datasets.

### Must-Know Methods:
*   `df.groupby()`: Used to group a DataFrame by one or more columns.
*   `.sum()`: Calculates the sum of values for each group.
*   `.mean()`: Calculates the average of values for each group.
*   `.count()`: Counts non-null observations for each group.

### Explanation and Examples:

Let's use a simulated NGO project dataset with information on regions, assistance types, and budgets.

```python
import pandas as pd

# Simulate creating a DataFrame for grouping and aggregation
data = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
    'AssistanceType': ['Food', 'Shelter', 'Food', 'Medical', 'Food', 'Shelter', 'Medical', 'Food'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000, 220000],
    'Beneficiaries': [1500, 2000, 1000, 1800, 2500, 1200, 1900, 2100]
}
df_projects = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_projects)

# 1. Group by 'Region' and calculate the total 'Budget' for each region
total_budget_by_region = df_projects.groupby('Region')['Budget'].sum()
print("\nTotal Budget by Region:")
print(total_budget_by_region)

# 2. Group by 'AssistanceType' and calculate the average 'Beneficiaries'
average_beneficiaries_by_type = df_projects.groupby('AssistanceType')['Beneficiaries'].mean()
print("\nAverage Beneficiaries by Assistance Type:")
print(average_beneficiaries_by_type)

# 3. Group by 'Region' and 'AssistanceType' and count the number of projects
project_count_by_region_type = df_projects.groupby(['Region', 'AssistanceType'])['ProjectID'].count()
print("\nProject Count by Region and Assistance Type:")
print(project_count_by_region_type)
```

`groupby()` creates a `DataFrameGroupBy` object, which you then apply an aggregation function to. The result is a Series (if grouping by one column and aggregating one column) or a DataFrame (if grouping by multiple columns or aggregating multiple columns). The `reset_index()` method can be used to convert the grouped output back into a DataFrame with columns for the grouped keys.

### Practice Task:

1.  Create a DataFrame named `aid_distribution.csv` with columns `Country`, `AidType`, `AmountUSD`, `Year`.
2.  Load `aid_distribution.csv`.
3.  Calculate the total `AmountUSD` distributed per `Country`.
4.  Find the average `AmountUSD` for each `AidType`.
5.  Count the number of aid projects (`AidType`) per `Country` and `Year`.

## 1.2 Intermediate Level: Multiple Aggregations with `.agg()`

At the intermediate level, you'll learn to apply multiple aggregation functions to one or more columns simultaneously using the powerful `.agg()` method. This allows for a more comprehensive summary of your grouped data.

### Must-Know Methods:
*   `.agg()`: Allows applying multiple aggregation functions to one or more columns.
*   Named aggregations: Provides a way to name the output columns of aggregated results, improving readability.

### Explanation and Examples:

Let's extend our NGO project dataset to perform multiple aggregations.

```python
import pandas as pd

data = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
    'AssistanceType': ['Food', 'Shelter', 'Food', 'Medical', 'Food', 'Shelter', 'Medical', 'Food'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000, 220000],
    'Beneficiaries': [1500, 2000, 1000, 1800, 2500, 1200, 1900, 2100]
}
df_projects = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df_projects)

# 1. Group by 'Region' and calculate total budget, average budget, and number of projects
regional_summary = df_projects.groupby('Region').agg(
    total_budget=('Budget', 'sum'),
    average_budget=('Budget', 'mean'),
    project_count=('ProjectID', 'count')
)
print("\nRegional Summary (using named aggregations):")
print(regional_summary)

# 2. Group by 'AssistanceType' and calculate min, max, and median beneficiaries
assistance_summary = df_projects.groupby('AssistanceType').agg(
    min_beneficiaries=('Beneficiaries', 'min'),
    max_beneficiaries=('Beneficiaries', 'max'),
    median_beneficiaries=('Beneficiaries', 'median')
)
print("\nAssistance Type Summary:")
print(assistance_summary)

# 3. Apply different aggregations to different columns
complex_summary = df_projects.groupby('Region').agg(
    total_budget=('Budget', 'sum'),
    avg_beneficiaries=('Beneficiaries', 'mean'),
    unique_assistance_types=('AssistanceType', lambda x: x.nunique()) # Custom aggregation
)
print("\nComplex Summary by Region:")
print(complex_summary)
```

The `.agg()` method is highly flexible. You can pass a list of functions to aggregate a single column, a dictionary to apply different functions to different columns, or use named aggregations (as shown above) for clearer output column names. Named aggregations are particularly useful for readability when performing multiple aggregations.

### Practice Task:

1.  Load `aid_distribution.csv` (from the beginner task) again.
2.  Group by `Country` and calculate the total `AmountUSD`, the average `AmountUSD`, and the number of unique `AidType`s for each country.
3.  Group by `AidType` and find the minimum, maximum, and median `AmountUSD` for each type of aid.
4.  Group by `Year` and calculate the total `AmountUSD` and the count of `Country`s that received aid in that year.

## 1.3 Master Level: Custom Aggregation Functions, `transform`, and `filter`

At the master level, you'll gain proficiency in writing and applying custom aggregation functions, and using `transform()` and `filter()` within `groupby()` operations. These advanced techniques allow for highly specific data manipulations and contextual calculations.

### Must-Know Concepts:
*   **Custom Aggregation Functions**: Defining your own functions to pass to `.agg()` for specialized calculations.
*   `df.groupby().transform()`: Applies a function to each group and returns a Series with the same index as the original DataFrame, effectively broadcasting the group-wise result back to the original rows.
*   `df.groupby().filter()`: Filters out entire groups based on a condition, returning a subset of the original DataFrame.

### Explanation and Examples:

Let's explore custom aggregations, `transform`, and `filter` with our NGO project data.

```python
import pandas as pd
import numpy as np

data = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'East Africa', 'West Africa'],
    'AssistanceType': ['Food', 'Shelter', 'Food', 'Medical', 'Food', 'Shelter', 'Medical', 'Food', 'Food', 'Medical'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000, 220000, 160000, 140000],
    'Beneficiaries': [1500, 2000, 1000, 1800, 2500, 1200, 1900, 2100, 1600, 1300]
}
df_projects = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df_projects)

# 1. Custom Aggregation Function: Calculate the range (max - min) of Budget per Region
def budget_range(series):
    return series.max() - series.min()

regional_budget_range = df_projects.groupby('Region')['Budget'].agg(budget_range)
print("\nBudget Range by Region (Custom Aggregation):")
print(regional_budget_range)

# 2. Using transform(): Calculate each project's budget as a percentage of its region's total budget
df_projects['RegionalBudgetShare'] = df_projects.groupby('Region')['Budget'].transform(lambda x: x / x.sum())
print("\nDataFrame with Regional Budget Share (using transform()):")
print(df_projects[['Region', 'Budget', 'RegionalBudgetShare']])

# 3. Using filter(): Select only regions that have more than 2 'Medical' assistance projects
filtered_regions_medical = df_projects.groupby('Region').filter(lambda x: (x['AssistanceType'] == 'Medical').sum() > 1)
print("\nRegions with more than 1 'Medical' assistance projects (using filter()):")
print(filtered_regions_medical)

# Another example of filter: Keep only groups where the average budget is above a certain threshold
threshold_budget = 170000
filtered_by_avg_budget = df_projects.groupby('Region').filter(lambda x: x['Budget'].mean() > threshold_budget)
print(f"\nRegions where average budget is > {threshold_budget} (using filter()):")
print(filtered_by_avg_budget)
```

Custom aggregation functions provide ultimate flexibility for specific calculations not available as built-in methods. `transform()` is incredibly useful for adding group-level statistics back to the original DataFrame, enabling comparisons of individual records against their group. `filter()` allows you to select entire groups based on a condition, which is different from filtering individual rows after aggregation. These methods are essential for complex analytical tasks.

### Practice Task:

1.  Load `aid_distribution.csv` (from the beginner task) again.
2.  Define a custom aggregation function that calculates the coefficient of variation (standard deviation / mean) for `AmountUSD`. Apply this function to `AmountUSD` grouped by `Country`.
3.  Using `transform()`, add a new column to the original DataFrame called `CountryAvgAmount` that contains the average `AmountUSD` for each `Country`.
4.  Using `filter()`, select only those `Country` groups where the total `AmountUSD` distributed is greater than 500,000 USD.
5.  Using `filter()`, select only those `AidType` groups that have projects in at least 3 different `Country`s.
