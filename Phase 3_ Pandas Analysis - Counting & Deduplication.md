# Phase 3: Pandas Analysis - Counting & Deduplication

Counting and deduplication are critical steps in data analysis, especially when dealing with records of beneficiaries, projects, or transactions in NGO data. Accurate counts are essential for reporting, and removing duplicate entries ensures that analyses are not skewed by redundant information. This section will guide you through various methods for counting unique items and effectively managing duplicate records.

## 2.1 Beginner Level: Basic Value Counts and Exact Deduplication

At the beginner level, the focus is on understanding how to count the occurrences of unique values within a column and how to remove exact duplicate rows from a DataFrame. These are fundamental operations for data quality and summary.

### Must-Know Methods:
*   `df['column'].value_counts()`: Returns a Series containing counts of unique values in a column.
*   `df.drop_duplicates()`: Removes duplicate rows from the DataFrame.

### Explanation and Examples:

Let's use a simulated NGO beneficiary dataset where some beneficiaries might be listed multiple times or have repeated assistance types.

```python
import pandas as pd

# Simulate creating a DataFrame with duplicate entries and varied assistance types
data = {
    'BeneficiaryID': [1, 2, 3, 1, 4, 5, 2, 6],
    'Age': [25, 34, 28, 25, 40, 30, 34, 55],
    'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'AssistanceType': ['Food', 'Shelter', 'Food', 'Food', 'Medical', 'Shelter', 'Shelter', 'Food'],
    'Location': ['Camp A', 'Village B', 'Camp A', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A']
}
df_beneficiaries = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_beneficiaries)

# 1. Counting unique values in 'AssistanceType'
assistance_counts = df_beneficiaries['AssistanceType'].value_counts()
print("\nCounts of Assistance Types:")
print(assistance_counts)

# 2. Counting unique values in 'Location'
location_counts = df_beneficiaries['Location'].value_counts()
print("\nCounts of Locations:")
print(location_counts)

# 3. Dropping exact duplicate rows
df_deduplicated = df_beneficiaries.drop_duplicates()
print("\nDataFrame after dropping exact duplicates:")
print(df_deduplicated)

# 4. Dropping duplicates based on a subset of columns (e.g., 'BeneficiaryID' and 'AssistanceType')
# This means if a beneficiary received the same assistance type multiple times, only keep the first record
df_deduplicated_subset = df_beneficiaries.drop_duplicates(subset=['BeneficiaryID', 'AssistanceType'])
print("\nDataFrame after dropping duplicates based on BeneficiaryID and AssistanceType:")
print(df_deduplicated_subset)
```

`value_counts()` is incredibly useful for quickly understanding the distribution of categorical data. `drop_duplicates()` by default considers all columns to identify a duplicate row. By using the `subset` parameter, you can specify which columns to consider when identifying duplicates, which is often more practical for real-world data where some columns (like timestamps) might legitimately differ even for the same logical entity.

### Practice Task:

1.  Create a DataFrame named `event_logs.csv` with columns `LogID`, `Timestamp`, `EventType`, `UserID`. Include some rows that are exact duplicates and some where `UserID` and `EventType` are the same but `Timestamp` differs.
2.  Load `event_logs.csv`.
3.  Count the occurrences of each `EventType`.
4.  Remove all exact duplicate rows from the DataFrame.
5.  Remove duplicates based on `UserID` and `EventType`, keeping only the first occurrence for each unique combination.

## 2.2 Intermediate Level: Normalized Counts and Identifying Unique Entities

At the intermediate level, we move beyond simple counts to normalized frequencies and focus on accurately identifying unique entities within your dataset, which is crucial for metrics like 
total beneficiaries served.

### Must-Know Methods:
*   `df["column"].value_counts(normalize=True)`: Returns a Series containing the relative frequencies of unique values.
*   `df["column"].nunique()`: Returns the number of unique values in a Series.
*   `df.drop_duplicates(subset=..., keep=...)`: More advanced usage of `drop_duplicates` to control which duplicate to keep (`first`, `last`, `False`).

### Explanation and Examples:

Let's continue with our `df_beneficiaries` DataFrame to explore normalized counts and unique entity identification.

```python
import pandas as pd

data = {
    'BeneficiaryID': [1, 2, 3, 1, 4, 5, 2, 6],
    'Age': [25, 34, 28, 25, 40, 30, 34, 55],
    'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'AssistanceType': ['Food', 'Shelter', 'Food', 'Food', 'Medical', 'Shelter', 'Shelter', 'Food'],
    'Location': ['Camp A', 'Village B', 'Camp A', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A']
}
df_beneficiaries = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_beneficiaries)

# 1. Normalized counts of 'AssistanceType'
normalized_assistance_counts = df_beneficiaries['AssistanceType'].value_counts(normalize=True)
print("\nNormalized Counts of Assistance Types:")
print(normalized_assistance_counts)

# 2. Number of unique beneficiaries
unique_beneficiaries_count = df_beneficiaries['BeneficiaryID'].nunique()
print(f"\nNumber of unique beneficiaries: {unique_beneficiaries_count}")

# 3. Number of unique locations
unique_locations_count = df_beneficiaries['Location'].nunique()
print(f"Number of unique locations: {unique_locations_count}")

# 4. Deduplication logic: Keep the last record for each BeneficiaryID
# This might be useful if the last record is considered the most up-to-date
df_unique_beneficiaries_last = df_beneficiaries.drop_duplicates(subset=['BeneficiaryID'], keep='last')
print("\nDataFrame with unique beneficiaries (keeping last record):")
print(df_unique_beneficiaries_last)

# 5. Deduplication logic: Identify all duplicate BeneficiaryIDs
# This can be useful for auditing or further investigation
duplicate_beneficiary_ids = df_beneficiaries[df_beneficiaries.duplicated(subset=['BeneficiaryID'], keep=False)]
print("\nAll records for duplicate BeneficiaryIDs:")
print(duplicate_beneficiary_ids)
```

`value_counts(normalize=True)` is excellent for quickly seeing the proportion of each category. `nunique()` is a direct way to count distinct elements. The `keep` parameter in `drop_duplicates()` is crucial: `first` (default) keeps the first occurrence, `last` keeps the last, and `False` marks all occurrences of a duplicate as `True` in the boolean Series returned by `duplicated()`, allowing you to inspect all duplicate records.

### Practice Task:

1.  Load `event_logs.csv` (from the beginner task) again.
2.  Calculate the normalized frequency of each `EventType`.
3.  Determine the total number of unique `UserID`s and `EventType`s.
4.  Create a DataFrame that contains only the *first* record for each unique `UserID`.
5.  Identify and display all records for `UserID`s that appear more than once in the dataset.

## 2.3 Master Level: Fuzzy Matching for Deduplication and Identifying "Near-Duplicates"

At the master level, deduplication extends beyond exact matches to identifying and handling "near-duplicates" or records that are conceptually the same but have slight variations (e.g., typos, different spellings). This is particularly relevant in humanitarian data where data entry inconsistencies are common. This often involves fuzzy string matching techniques.

### Must-Know Concepts:
*   **Fuzzy Matching Libraries**: Using external libraries like `fuzzywuzzy` (or `thefuzz`) to compare string similarity.
*   **Identifying "Near-Duplicates"**: Developing strategies to group similar but not identical records.
*   **Consolidating Duplicate Information**: Merging information from near-duplicate records into a single, canonical record.

### Explanation and Examples:

For fuzzy matching, we'll need to install an external library. Let's simulate a scenario where `Location` names might have slight variations.

```python
import pandas as pd
import numpy as np

# First, install the fuzzywuzzy library (or thefuzz, its maintained fork)
# !pip install thefuzz
# !pip install python-Levenshtein # for faster processing

# We'll assume thefuzz is installed for the example
from thefuzz import fuzz
from thefuzz import process

# Simulate a DataFrame with near-duplicate location names
data = {
    'BeneficiaryID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Name': ['John Doe', 'Jane Smith', 'Peter Jones', 'Jon Doe', 'Sarah Lee', 'Jane Smyth', 'Peter Jonez', 'John Do'],
    'Location': ['Camp A', 'Village B', 'Camp Alpha', 'Camp A', 'Village Beta', 'Village B', 'Camp Alpha', 'Camp A '],
    'AssistanceType': ['Food', 'Shelter', 'Medical', 'Food', 'Shelter', 'Shelter', 'Medical', 'Food']
}
df_fuzzy = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df_fuzzy)

# 1. Identifying near-duplicate 'Location' names using fuzzy matching
# Let's define a threshold for similarity
similarity_threshold = 85

unique_locations = df_fuzzy['Location'].unique()
print(f"\nUnique locations before fuzzy matching: {unique_locations}")

# Create a mapping for similar locations to a canonical name
canonical_locations = {}
for loc in unique_locations:
    # Find the best match for the current location among the already processed canonical names
    # or itself if no good match is found
    best_match = process.extractOne(loc, list(canonical_locations.keys()) + [loc], scorer=fuzz.ratio)
    
    if best_match[1] >= similarity_threshold and best_match[0] in canonical_locations:
        canonical_locations[loc] = canonical_locations[best_match[0]]
    else:
        canonical_locations[loc] = loc # This location becomes a new canonical name

# Apply the canonical mapping to the DataFrame
df_fuzzy['Location_Clean'] = df_fuzzy['Location'].map(canonical_locations)
print("\nDataFrame after fuzzy matching and cleaning Location:")
print(df_fuzzy)
print("\nUnique locations after fuzzy matching: ")
print(df_fuzzy['Location_Clean'].unique())

# 2. Identifying near-duplicate 'Name' entries
# This is more complex as it requires comparing each name against all others.
# For demonstration, let's just find groups of similar names.

# A more robust approach for names would involve clustering or more advanced record linkage.
# For simplicity, let's group names that are very similar to a chosen canonical form.

# Example: Grouping 'John Doe', 'Jon Doe', 'John Do'
names_to_standardize = ['John Doe', 'Jon Doe', 'John Do']
standard_name = 'John Doe'

def standardize_name(name):
    for potential_match in names_to_standardize:
        if fuzz.ratio(name, potential_match) >= 90: # High similarity for names
            return standard_name
    return name

df_fuzzy['Name_Clean'] = df_fuzzy['Name'].apply(standardize_name)
print("\nDataFrame after fuzzy matching and cleaning Name:")
print(df_fuzzy)

# 3. Consolidating information from near-duplicate beneficiary records
# This is a conceptual step. After identifying near-duplicates (e.g., 'John Doe' and 'Jon Doe'),
# you would typically choose one record as the master and merge relevant information from others.
# For example, if 'Jon Doe' has an 'AssistanceType' that 'John Doe' doesn't, you might add it.

# This often involves creating a master ID for each cluster of near-duplicates and then aggregating.
# For instance, if BeneficiaryID 1 ('John Doe') and BeneficiaryID 4 ('Jon Doe') are near-duplicates,
# you might assign them a common 'MasterBeneficiaryID' and then group by it.

# Example: Assigning a master ID based on cleaned name (simplified)
# This is a very basic approach and would need refinement for real-world scenarios.
master_id_map = {}
current_master_id = 1
for name in df_fuzzy['Name_Clean'].unique():
    master_id_map[name] = current_master_id
    current_master_id += 1

df_fuzzy['MasterBeneficiaryID'] = df_fuzzy['Name_Clean'].map(master_id_map)
print("\nDataFrame with MasterBeneficiaryID (simplified):")
print(df_fuzzy)

# Now you can group by MasterBeneficiaryID to consolidate information
consolidated_data = df_fuzzy.groupby('MasterBeneficiaryID').agg(
    CanonicalName=('Name_Clean', 'first'),
    Locations=('Location_Clean', lambda x: list(x.unique())),
    AssistanceTypes=('AssistanceType', lambda x: list(x.unique())),
    TotalRecords=('BeneficiaryID', 'count')
).reset_index()
print("\nConsolidated Data by MasterBeneficiaryID:")
print(consolidated_data)
```

Fuzzy matching is a powerful technique for data cleaning, but it requires careful consideration of similarity thresholds and the specific context of your data. Libraries like `thefuzz` provide various algorithms (e.g., `fuzz.ratio`, `fuzz.partial_ratio`, `fuzz.token_sort_ratio`) to compare strings. Identifying near-duplicates often involves an iterative process of defining similarity, grouping, and then manually or programmatically consolidating the information. This is a complex area, and the examples provided are simplified introductions.

### Practice Task:

1.  Create a DataFrame named `partner_organizations.csv` with columns `OrgID`, `OrgName`, `ContactPerson`, `City`. Intentionally introduce variations in `OrgName` (e.g., 'Save the Children', 'Save The Children Intl.', 'Save Childrn') and `City` (e.g., 'New York', 'NYC', 'New-York').
2.  Load `partner_organizations.csv`.
3.  Install `thefuzz` library if not already installed.
4.  Using `thefuzz.process.extractOne`, create a new `OrgName_Clean` column by standardizing `OrgName` entries that are similar (e.g., score > 80) to a canonical form. You might need to manually define a list of canonical names or iteratively build them.
5.  Similarly, clean the `City` column to standardize city names.
6.  After cleaning, identify groups of records that are likely referring to the same organization based on `OrgName_Clean` and `City_Clean`. For each group, consolidate the `ContactPerson` information (e.g., list all contact persons associated with the consolidated organization).
