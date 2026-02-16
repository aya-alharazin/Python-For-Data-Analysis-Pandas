# Phase 3: Pandas Analysis - Creating Metrics & Binning

Creating new metrics and binning values are powerful techniques to transform raw data into meaningful insights. In humanitarian contexts, this could involve calculating aid per capita, determining the ratio of displaced to non-displaced populations, or categorizing beneficiaries into age groups. This section will guide you through the process of deriving new information from your data and segmenting continuous variables.

## 3.1 Beginner Level: Simple Column Arithmetic and Basic Binning

At the beginner level, the focus is on performing straightforward mathematical operations between columns to create new metrics and using basic methods to categorize numerical data into bins.

### Must-Know Methods:
*   Simple column arithmetic: `df["new_col"] = df["col1"] + df["col2"]` (or `-`, `*`, `/`).
*   `pd.cut()`: Discretizes a Series into bins based on specified edges.

### Explanation and Examples:

Let's use a simulated NGO project dataset with information on budget, beneficiaries, and duration.

```python
import pandas as pd

# Simulate creating a DataFrame
data = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000, 220000],
    'Beneficiaries': [1500, 2000, 1000, 1800, 2500, 1200, 1900, 2100],
    'DurationDays': [180, 240, 150, 200, 300, 160, 210, 270]
}
df_projects = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_projects)

# 1. Creating a new metric: 'CostPerBeneficiary'
df_projects['CostPerBeneficiary'] = df_projects['Budget'] / df_projects['Beneficiaries']
print("\nDataFrame with 'CostPerBeneficiary':")
print(df_projects[['ProjectID', 'Budget', 'Beneficiaries', 'CostPerBeneficiary']])

# 2. Creating a new metric: 'BudgetPerDay'
df_projects['BudgetPerDay'] = df_projects['Budget'] / df_projects['DurationDays']
print("\nDataFrame with 'BudgetPerDay':")
print(df_projects[['ProjectID', 'Budget', 'DurationDays', 'BudgetPerDay']])

# 3. Basic Binning: Categorize 'Beneficiaries' into groups
# Define the bin edges and labels
bins = [0, 1000, 2000, 3000]
labels = ['Small', 'Medium', 'Large']
df_projects['BeneficiaryGroup'] = pd.cut(df_projects['Beneficiaries'], bins=bins, labels=labels, right=True)
print("\nDataFrame with 'BeneficiaryGroup':")
print(df_projects[['ProjectID', 'Beneficiaries', 'BeneficiaryGroup']])
print("\nCounts of Beneficiary Groups:")
print(df_projects['BeneficiaryGroup'].value_counts())
```

Simple column arithmetic allows you to derive new quantitative insights directly from existing numerical columns. `pd.cut()` is a straightforward way to segment continuous numerical data into discrete categories. You define the boundaries (`bins`) and optionally provide descriptive `labels` for these categories. The `right=True` argument (default) means the bins include the rightmost edge, e.g., `(1000, 2000]`.

### Practice Task:

1.  Create a DataFrame named `health_records.csv` with columns `PatientID`, `WeightKg`, `HeightCm`, `BloodPressureSystolic`, `BloodPressureDiastolic`.
2.  Load `health_records.csv`.
3.  Create a new column `BMI` (Body Mass Index) using the formula: `WeightKg / (HeightCm/100)**2`.
4.  Create a new column `PulsePressure` by subtracting `BloodPressureDiastolic` from `BloodPressureSystolic`.
5.  Bin the `BMI` values into categories: 'Underweight' (BMI < 18.5), 'Normal' (18.5 <= BMI < 25), 'Overweight' (25 <= BMI < 30), 'Obese' (BMI >= 30). Display the counts for each category.

## 3.2 Intermediate Level: Advanced Metric Creation and Quantile-based Binning

At the intermediate level, we focus on creating more complex metrics that might involve conditional logic or aggregations, and using quantile-based binning to create groups with approximately equal numbers of observations.

### Must-Know Methods:
*   `np.where()`: Conditional logic for creating new columns.
*   `pd.qcut()`: Discretizes a Series into equal-sized bins based on quantiles.

### Explanation and Examples:

Let's enhance our NGO project dataset by adding a `ProjectStatus` and `RiskScore` to create more nuanced metrics.

```python
import pandas as pd
import numpy as np

# Simulate creating a DataFrame with additional columns
data = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000, 220000],
    'Beneficiaries': [1500, 2000, 1000, 1800, 2500, 1200, 1900, 2100],
    'RiskScore': [5, 7, 3, 8, 6, 4, 9, 7],
    'ProjectStatus': ['Active', 'Completed', 'Active', 'Completed', 'Active', 'Pending', 'Active', 'Completed']
}
df_projects = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_projects)

# 1. Creating a conditional metric: 'HighRiskProject'
# A project is high risk if its RiskScore is above 7 AND it's still 'Active'
df_projects['HighRiskProject'] = np.where(
    (df_projects['RiskScore'] > 7) & (df_projects['ProjectStatus'] == 'Active'),
    True, False
)
print("\nDataFrame with 'HighRiskProject':")
print(df_projects[['ProjectID', 'RiskScore', 'ProjectStatus', 'HighRiskProject']])

# 2. Quantile-based Binning: Categorize 'Budget' into 4 equal-sized groups (quartiles)
df_projects['BudgetQuartile'] = pd.qcut(df_projects['Budget'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print("\nDataFrame with 'BudgetQuartile':")
print(df_projects[['ProjectID', 'Budget', 'BudgetQuartile']])
print("\nCounts of Budget Quartiles:")
print(df_projects['BudgetQuartile'].value_counts())

# 3. Quantile-based Binning: Categorize 'Beneficiaries' into 3 groups (tertiles)
df_projects['BeneficiaryTertile'] = pd.qcut(df_projects['Beneficiaries'], q=3, labels=['Low', 'Medium', 'High'])
print("\nDataFrame with 'BeneficiaryTertile':")
print(df_projects[['ProjectID', 'Beneficiaries', 'BeneficiaryTertile']])
print("\nCounts of Beneficiary Tertiles:")
print(df_projects['BeneficiaryTertile'].value_counts())
```

`np.where()` is a powerful function for applying conditional logic to create new columns, allowing you to define values based on whether a condition is met. `pd.qcut()` is particularly useful when you want to divide your data into groups that have roughly the same number of observations, rather than groups based on fixed numerical intervals. This is often preferred for creating balanced categories for analysis.

### Practice Task:

1.  Load `health_records.csv` (from the beginner task) again.
2.  Create a new column `HypertensionRisk` using `np.where()`. A patient has 'High' risk if `BloodPressureSystolic` >= 140 OR `BloodPressureDiastolic` >= 90, otherwise 'Normal'.
3.  Bin the `WeightKg` values into 5 equal-sized groups (quintiles) using `pd.qcut()`. Label these groups 'Lightest', 'Lighter', 'Middle', 'Heavier', 'Heaviest'. Display the counts for each group.
4.  Bin the `PulsePressure` values (calculated in the beginner task) into 3 equal-sized groups (tertiles). Label them 'Low PP', 'Medium PP', 'High PP'. Display the counts for each group.

## 3.3 Master Level: Complex KPI Calculation and Dynamic Binning Strategies

At the master level, the focus shifts to calculating sophisticated Key Performance Indicators (KPIs) that might involve merging with external data, and implementing dynamic binning strategies that adapt to the data's distribution or specific analytical needs.

### Must-Know Concepts:
*   **Complex KPI Calculation**: Deriving metrics that require multiple steps, potentially involving merging with external datasets (e.g., population data for aid per capita).
*   **Dynamic Binning**: Creating bins based on statistical properties of the data (e.g., standard deviations, custom percentiles) rather than fixed intervals or quantiles.
*   **Weighted Averages**: Calculating averages where each value contributes differently to the final mean.

### Explanation and Examples:

Let's imagine we need to calculate 'Aid per Capita' for different regions, which requires external population data. We'll also explore dynamic binning based on standard deviations.

```python
import pandas as pd
import numpy as np

# Simulate NGO project data
data_projects = {
    'ProjectID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
    'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000, 220000],
    'Beneficiaries': [1500, 2000, 1000, 1800, 2500, 1200, 1900, 2100]
}
df_projects = pd.DataFrame(data_projects)

# Simulate external population data
data_population = {
    'Region': ['East Africa', 'South Asia', 'West Africa', 'Latin America'],
    'Population': [10000000, 15000000, 8000000, 12000000]
}
df_population = pd.DataFrame(data_population)

print("\nOriginal Projects DataFrame:")
print(df_projects)
print("\nExternal Population DataFrame:")
print(df_population)

# 1. Complex KPI Calculation: 'Aid per Capita'
# First, calculate total budget per region from project data
regional_budget_summary = df_projects.groupby('Region')['Budget'].sum().reset_index()
regional_budget_summary.rename(columns={'Budget': 'TotalBudget'}, inplace=True)

# Merge with population data
df_merged = pd.merge(regional_budget_summary, df_population, on='Region', how='left')

# Calculate Aid per Capita
df_merged['AidPerCapita'] = df_merged['TotalBudget'] / df_merged['Population']
print("\nRegional Aid per Capita:")
print(df_merged)

# 2. Dynamic Binning: Categorize 'Budget' based on standard deviations from the mean
mean_budget = df_projects['Budget'].mean()
std_budget = df_projects['Budget'].std()

bins_dynamic = [
    df_projects['Budget'].min(),
    mean_budget - std_budget,
    mean_budget,
    mean_budget + std_budget,
    df_projects['Budget'].max()
]
labels_dynamic = ['Very Low', 'Low', 'Medium', 'High']

# Ensure bins are unique and sorted, pd.cut requires this
bins_dynamic = sorted(list(set(bins_dynamic)))

df_projects['BudgetCategory_Dynamic'] = pd.cut(df_projects['Budget'], bins=bins_dynamic, labels=labels_dynamic, include_lowest=True)
print("\nDataFrame with Dynamic Budget Categories:")
print(df_projects[['ProjectID', 'Budget', 'BudgetCategory_Dynamic']])
print("\nCounts of Dynamic Budget Categories:")
print(df_projects['BudgetCategory_Dynamic'].value_counts())

# 3. Weighted Average: Calculate weighted average CostPerBeneficiary by Budget
# First, ensure CostPerBeneficiary is calculated
df_projects['CostPerBeneficiary'] = df_projects['Budget'] / df_projects['Beneficiaries']

# Calculate weighted average CostPerBeneficiary per Region, weighted by Budget
weighted_avg_cost = df_projects.groupby('Region').apply(
    lambda x: (x['CostPerBeneficiary'] * x['Budget']).sum() / x['Budget'].sum()
).reset_index(name='WeightedAvgCostPerBeneficiary')
print("\nWeighted Average Cost Per Beneficiary by Region:")
print(weighted_avg_cost)
```

Calculating complex KPIs often involves data integration steps, such as merging different DataFrames. Dynamic binning allows for more flexible categorization that adapts to the specific distribution of your data, which can be particularly useful for identifying outliers or natural groupings. Weighted averages are crucial when different observations have varying levels of importance or contribution, ensuring that the average accurately reflects the underlying reality.

### Practice Task:

1.  Create a DataFrame named `school_data.csv` with columns `SchoolID`, `District`, `Enrollment`, `FundingPerStudent`, `TestScoreAverage`.
2.  Create an external DataFrame `district_poverty.csv` with columns `District`, `PovertyRate`.
3.  Load both DataFrames.
4.  Calculate a new KPI: `TotalDistrictFunding`. This requires merging `school_data` to sum `FundingPerStudent * Enrollment` per `District`, then merging with `district_poverty`.
5.  Implement dynamic binning for `TestScoreAverage`. Create 3 bins: 'Below Average' (scores below mean - 0.5 * std), 'Average' (scores between mean - 0.5 * std and mean + 0.5 * std), 'Above Average' (scores above mean + 0.5 * std). Display the counts for each category.
6.  Calculate the weighted average `FundingPerStudent` for each `District`, weighted by `Enrollment`.
