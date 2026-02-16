# Phase 2: Pandas Core - String Cleaning & Type Conversion

Clean and consistent string data is vital for accurate analysis, especially when dealing with textual information like region names, assistance types, or beneficiary statuses. Similarly, ensuring columns have the correct data types (e.g., dates as datetime objects, numbers as integers or floats) is fundamental for performing appropriate operations and calculations. This section will cover techniques for cleaning string data and converting column types.

## 3.1 Beginner Level: Basic String Operations and Type Casting

At the beginner level, the focus is on common string manipulations to standardize text and straightforward type conversions to ensure data is in a usable format.

### Must-Know Methods:
*   `.str.lower()`: Converts all characters in a string Series to lowercase.
*   `.str.strip()`: Removes leading and trailing whitespace from strings.
*   `astype()`: Converts a Series to a specified data type.

### Explanation and Examples:

Let's use a simulated NGO dataset where `Region` names might have inconsistent casing or extra spaces, and `ProjectID` might be loaded as a string.

```python
import pandas as pd

# Simulate creating a DataFrame with messy strings and incorrect types
data = {
    'ProjectID': ['101', '102', '103 ', '104', '105'],
    'Region': ['East Africa ', 'south asia', 'WEST AFRICA', 'East Africa', 'South Asia'],
    'Status': ['Active', 'Completed ', 'Pending', 'active', 'Completed'],
    'Budget': ['150000', '200000', '120000', '180000', '250000'] # Loaded as string
}
df_messy = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_messy)
print("\nOriginal DataFrame dtypes:")
print(df_messy.dtypes)

# 1. Cleaning 'Region' column: convert to lowercase and strip whitespace
df_cleaned = df_messy.copy()
df_cleaned['Region'] = df_cleaned['Region'].str.lower().str.strip()
print("\nDataFrame after cleaning 'Region' column:")
print(df_cleaned)

# 2. Cleaning 'Status' column: strip whitespace and then convert to title case for consistency
df_cleaned['Status'] = df_cleaned['Status'].str.strip().str.title()
print("\nDataFrame after cleaning 'Status' column:")
print(df_cleaned)

# 3. Converting 'ProjectID' to integer type
df_cleaned['ProjectID'] = df_cleaned['ProjectID'].astype(int)

# 4. Converting 'Budget' to integer type
df_cleaned['Budget'] = df_cleaned['Budget'].astype(int)
print("\nDataFrame after type conversion:")
print(df_cleaned)
print("\nCleaned DataFrame dtypes:")
print(df_cleaned.dtypes)
```

Using `.str.lower()` and `.str.strip()` in combination is a very common pattern for standardizing categorical string data. `astype()` is straightforward for converting to numerical types (like `int`, `float`) or boolean. It's important to ensure that the data can actually be converted; for example, trying to convert a string like 'N/A' to an integer will raise an error.

### Practice Task:

1.  Create a DataFrame with columns `Item`, `Quantity`, `Price`. `Item` should have inconsistent casing and leading/trailing spaces (e.g., '   apple', 'BANANA ', 'orange'). `Quantity` and `Price` should be strings that represent numbers (e.g., '10', '2.50').
2.  Clean the `Item` column by converting all entries to lowercase and removing whitespace.
3.  Convert `Quantity` to integer and `Price` to float.
4.  Verify the data types after conversion.

## 3.2 Intermediate Level: Advanced String Manipulation and Date Handling

At the intermediate level, we delve into more complex string operations, including using regular expressions for pattern-based cleaning, and handling date/time data which often comes in various string formats.

### Must-Know Methods:
*   `.str.replace()`: Replaces occurrences of a pattern in strings.
*   `.str.contains()`: Tests if string or regex pattern is contained within each string of the Series/Index.
*   `.str.extract()`: Extracts groups from the first match of regex `pat` as a DataFrame.
*   `pd.to_datetime()`: Converts argument to datetime. Essential for working with dates.

### Explanation and Examples:

Consider a scenario where `ProjectID` might contain prefixes, or `StartDate` is in a non-standard format.

```python
import pandas as pd

# Simulate a DataFrame with more complex string issues and date strings
data = {
    'ProjectCode': ['NGO-101', 'PROJ_102', 'NGO-103', 'P-104', 'NGO-105'],
    'Description': ['Food distribution in area A', 'Shelter for displaced families', 'Medical aid for children', 'Water sanitation project', 'Education support'],
    'StartDate': ['2023/01/15', '02-01-2023', 'March 10, 2023', '2023-04-05', '2023-05-20'],
    'Beneficiaries': ['1,500', '2,000', '1,200', '1,800', '2,500'] # String with comma
}
df_advanced_messy = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_advanced_messy)
print("\nOriginal DataFrame dtypes:")
print(df_advanced_messy.dtypes)

# 1. Cleaning 'ProjectCode': remove prefixes like 'NGO-', 'PROJ_', 'P-'
df_cleaned_adv = df_advanced_messy.copy()
df_cleaned_adv['ProjectCode'] = df_cleaned_adv['ProjectCode'].str.replace(r'^(NGO-|PROJ_|P-)', '', regex=True)
print("\nDataFrame after cleaning 'ProjectCode':")
print(df_cleaned_adv)

# 2. Extracting numbers from 'Description' if they exist (e.g., 'area A' -> 'A')
# This is a simple example; regex can be much more complex
df_cleaned_adv['AreaCode'] = df_cleaned_adv['Description'].str.extract(r'area ([A-Z])')
print("\nDataFrame after extracting AreaCode:")
print(df_cleaned_adv)

# 3. Converting 'StartDate' to datetime objects
# Pandas is smart enough to infer many formats, but 'format' can be specified for robustness
df_cleaned_adv['StartDate'] = pd.to_datetime(df_cleaned_adv['StartDate'])
print("\nDataFrame after converting 'StartDate' to datetime:")
print(df_cleaned_adv)
print("\nCleaned DataFrame dtypes:")
print(df_cleaned_adv.dtypes)

# 4. Cleaning 'Beneficiaries' column (remove comma and convert to int)
df_cleaned_adv['Beneficiaries'] = df_cleaned_adv['Beneficiaries'].str.replace(',', '').astype(int)
print("\nDataFrame after cleaning and converting 'Beneficiaries':")
print(df_cleaned_adv)
print("\nCleaned DataFrame dtypes:")
print(df_cleaned_adv.dtypes)
```

Regular expressions (`regex=True` in `.str.replace()`, `.str.extract()`) are incredibly powerful for pattern-based string manipulation. `pd.to_datetime()` is a cornerstone for time-series analysis; it can parse a wide variety of date formats, and the `errors='coerce'` argument is useful for turning unparseable dates into `NaT` (Not a Time) rather than raising an error.

### Practice Task:

1.  Create a DataFrame with a `TransactionID` column (e.g., 'TRX-ABC-123', 'TXN_DEF_456', 'GHI789') and a `Timestamp` column with mixed date/time string formats (e.g., '2023-01-01 10:30:00', 'Jan 2, 23 11:00 AM', '03/03/2023 13:45').
2.  Clean the `TransactionID` column to extract only the numeric part (e.g., '123', '456', '789').
3.  Convert the `Timestamp` column to actual datetime objects.
4.  Add a new column `TransactionMonth` that extracts just the month from the `Timestamp`.

## 3.3 Master Level: Custom Vectorized Operations and Memory Efficiency with Categories

At the master level, the focus is on writing highly efficient custom string cleaning functions and leveraging Pandas' categorical data type for significant memory savings and performance improvements, especially with large datasets containing repetitive string values.

### Must-Know Concepts:
*   **Custom Vectorized Functions**: Applying custom logic to string Series using `.apply()` or more efficiently, by combining existing `.str` methods.
*   **Categorical Data Type**: Converting string columns with a limited number of unique values to the `category` dtype to reduce memory footprint and speed up operations.
*   **Complex Date-Time Arithmetic**: Performing advanced calculations with datetime objects (e.g., calculating duration, identifying specific days of the week).

### Explanation and Examples:

Let's consider a large dataset of `AssistanceType` strings that are repetitive, and we need to perform some custom cleaning that isn't directly available in `.str` methods, or calculate project durations.

```python
import pandas as pd
import numpy as np

# Simulate a large DataFrame with repetitive strings and date columns
num_rows = 100000
data = {
    'AssistanceType': np.random.choice(['Food Distribution', 'Shelter Support', 'Medical Aid', 'Education Support', 'Food Distribution '], num_rows),
    'Region': np.random.choice(['East Africa', 'South Asia', 'West Africa', 'East Africa '], num_rows),
    'ProjectStartDate': pd.to_datetime(np.random.choice(pd.date_range('2020-01-01', '2023-12-31'), num_rows)),
    'ProjectEndDate': pd.to_datetime(np.random.choice(pd.date_range('2024-01-01', '2025-12-31'), num_rows))
}
df_master = pd.DataFrame(data)

# Introduce some custom messy strings for demonstration
df_master.loc[df_master.index % 100 == 0, 'AssistanceType'] = 'food distribution (emergency)'
df_master.loc[df_master.index % 101 == 0, 'Region'] = 'south-asia'

print("\nOriginal DataFrame info (before category conversion):")
df_master.info(memory_usage='deep')

# 1. Custom Vectorized Cleaning for 'AssistanceType'
# Goal: Standardize 'Food Distribution' variations
def clean_assistance_type(text):
    text = str(text).lower().strip()
    if 'food' in text:
        return 'Food Distribution'
    elif 'shelter' in text:
        return 'Shelter Support'
    elif 'medical' in text:
        return 'Medical Aid'
    elif 'education' in text:
        return 'Education Support'
    return 'Other'

df_master['AssistanceType_Clean'] = df_master['AssistanceType'].apply(clean_assistance_type)
print("\nUnique AssistanceType_Clean values:")
print(df_master['AssistanceType_Clean'].value_counts())

# 2. Converting 'Region' and 'AssistanceType_Clean' to 'category' dtype
# First, clean 'Region' with basic methods
df_master['Region'] = df_master['Region'].str.lower().str.strip().str.replace('-', ' ').str.title()

df_master['Region'] = df_master['Region'].astype('category')
df_master['AssistanceType_Clean'] = df_master['AssistanceType_Clean'].astype('category')

print("\nDataFrame info (after category conversion):")
df_master.info(memory_usage='deep')

# 3. Complex Date-Time Arithmetic: Calculate Project Duration in Days
df_master['ProjectDurationDays'] = (df_master['ProjectEndDate'] - df_master['ProjectStartDate']).dt.days
print("\nDataFrame with ProjectDurationDays:")
print(df_master[['ProjectStartDate', 'ProjectEndDate', 'ProjectDurationDays']].head())

# Example: Find projects starting on a Monday
df_master['StartsOnMonday'] = df_master['ProjectStartDate'].dt.day_name() == 'Monday'
print("\nProjects starting on Monday (first 5):")
print(df_master[df_master['StartsOnMonday']].head())
```

Notice the significant memory reduction after converting string columns to `category` dtype, especially for columns with many repeated values. Custom functions applied with `.apply()` allow for highly specific cleaning logic. For datetime objects, the `.dt` accessor provides a wealth of methods for extracting components (year, month, day, day of week) and performing calculations.

### Practice Task:

1.  Create a large DataFrame (e.g., 100,000 rows) with a `Country` column containing repetitive country names, some with variations (e.g., 'United States', 'USA', 'United States of America', '   united states'). Also include `EventDate` and `ReportDate` columns as datetime objects.
2.  Implement a custom function to standardize the `Country` names (e.g., all variations of 'United States' should become 'United States'). Apply this function to create a new `Country_Clean` column.
3.  Convert the `Country_Clean` column to the `category` data type and observe the memory usage before and after.
4.  Calculate the `ReportingLagDays` (difference between `ReportDate` and `EventDate`) and the `DayOfWeekEvent` (the day of the week the event occurred) for each record.
