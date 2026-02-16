# Pandas Mastery: Practice Task Solutions

This document provides the solutions for all the practice tasks included in the Phase 2 and Phase 3 learning materials. Use these to check your work and understand the implementation details.

---

## Phase 2: Pandas Core

### 1. Data Loading & Initial Inspection

**Beginner Task:**
```python
import pandas as pd

# 1. Create beneficiary_data.csv
data = {
    'BeneficiaryID': [1, 2, 3, 4, 5],
    'Age': [25, 34, 28, 40, 30],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Location': ['Camp A', 'Village B', 'Camp A', 'Village C', 'Camp B'],
    'AssistanceType': ['Food', 'Shelter', 'Medical', 'Food', 'Shelter']
}
pd.DataFrame(data).to_csv('beneficiary_data.csv', index=False)

# 2. Load the CSV
df = pd.read_csv('beneficiary_data.csv')

# 3. Display first 3 and last 2 rows
print(df.head(3))
print(df.tail(2))
```

**Intermediate Task:**
```python
# 1. df.info()
df.info()

# 2. df.describe()
print(df.describe())
```

**Master Task:**
```python
import pandas as pd
import numpy as np

# 1. Create large CSV
num_rows = 100000
large_data = {
    'ProjectID': np.arange(1, num_rows + 1),
    'Region': np.random.choice(['East Africa', 'South Asia', 'West Africa', 'Latin America'], num_rows),
    'Status': np.random.choice(['Active', 'Completed', 'Pending'], num_rows),
    'Budget': np.random.randint(50000, 500000, num_rows)
}
pd.DataFrame(large_data).to_csv('large_ngo_projects.csv', index=False)

# 2. Load without optimization
df_unoptimized = pd.read_csv('large_ngo_projects.csv')
print(df_unoptimized.info(memory_usage='deep'))

# 3. Load with optimization
optimized_dtypes = {
    'ProjectID': 'int32',
    'Region': 'category',
    'Status': 'category',
    'Budget': 'int32'
}
df_optimized = pd.read_csv('large_ngo_projects.csv', dtype=optimized_dtypes)
print(df_optimized.info(memory_usage='deep'))

# 4. Read in chunks
chunk_size = 20000
for i, chunk in enumerate(pd.read_csv('large_ngo_projects.csv', chunksize=chunk_size, dtype=optimized_dtypes)):
    avg_budget = chunk['Budget'].mean()
    print(f"Chunk {i+1} Average Budget: {avg_budget:.2f}")
```

### 2. Handling Missing Values

**Beginner Task:**
```python
import pandas as pd
import numpy as np

# 1. Create project_updates.csv
data = {
    'UpdateID': [1, 2, 3, 4, 5, 6],
    'ProjectID': [101, 102, 101, 103, 102, 104],
    'Date': ['2023-01-20', '2023-02-05', '2023-03-15', '2023-04-10', '2023-05-25', '2023-06-05'],
    'Status': ['On Track', 'Completed', np.nan, 'Delayed', 'On Track', np.nan],
    'Notes': ['Initial report', 'Finalized', 'Needs review', np.nan, 'Mid-term update', np.nan]
}
pd.DataFrame(data).to_csv('project_updates.csv', index=False)

# 2. Load
df = pd.read_csv('project_updates.csv')

# 3. Count missing
print(df.isna().sum())

# 4. Drop rows
df_dropped = df.dropna()
print(f"Original shape: {df.shape}, New shape: {df_dropped.shape}")
```

**Intermediate Task:**
```python
# 2. Fill Status with mode
status_mode = df['Status'].mode()[0]
df['Status'] = df['Status'].fillna(status_mode)

# 3. Fill Notes with constant
df['Notes'] = df['Notes'].fillna("No update provided")

# 4. Verify
print(df.isna().sum())
```

**Master Task:**
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create health_data.csv
data = {
    'PatientID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [30, 45, 22, 60, 35, 50, 28, 42, 55, 65],
    'Weight': [70, 85, 60, 90, 75, 80, 65, 78, 88, 92],
    'Diagnosis': ['Flu', 'Malaria', 'Flu', 'Typhoid', 'Flu', 'Malaria', 'Flu', 'Typhoid', 'Malaria', 'Flu'],
    'Medication': ['A', 'B', np.nan, 'C', 'A', 'B', np.nan, 'C', 'B', np.nan]
}
df_health = pd.DataFrame(data)
df_health.loc[df_health['Diagnosis'] == 'Flu', 'Medication'] = np.nan
df_health.to_csv('health_data.csv', index=False)

# 3. Conditional Imputation
mean_weight_per_diag = df_health.groupby('Diagnosis')['Weight'].transform('mean')
df_health['Weight'] = df_health['Weight'].fillna(mean_weight_per_diag)

# 4. Heatmap
sns.heatmap(df_health.isna(), cbar=False)
plt.savefig('health_missing_heatmap.png')
```

### 3. String Cleaning & Type Conversion

**Beginner Task:**
```python
import pandas as pd

# 1. Create DataFrame
data = {
    'Item': ['   apple', 'BANANA ', 'orange', ' GRAPES  '],
    'Quantity': ['10', '5', '12', '8'],
    'Price': ['1.20', '0.75', '2.50', '3.00']
}
df = pd.DataFrame(data)

# 2. Clean Item
df['Item'] = df['Item'].str.lower().str.strip()

# 3. Convert types
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)

# 4. Verify
print(df.dtypes)
```

**Intermediate Task:**
```python
# 1. Create DataFrame
data = {
    'TransactionID': ['TRX-ABC-123', 'TXN_DEF_456', 'GHI789', 'TRX-JKL-010'],
    'Timestamp': ['2023-01-01 10:30:00', 'Jan 2, 23 11:00 AM', '03/03/2023 13:45', '2023-04-04 09:00:00']
}
df = pd.DataFrame(data)

# 2. Clean TransactionID
df['TransactionID_Num'] = df['TransactionID'].str.extract(r'(\d+)')

# 3. Convert Timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 4. Extract Month
df['TransactionMonth'] = df['Timestamp'].dt.month
```

**Master Task:**
```python
import pandas as pd
import numpy as np

# 1. Create large DataFrame
num_rows = 100000
countries = ['United States', 'USA', 'United States of America', '   united states', 'Canada']
data = {
    'Country': np.random.choice(countries, num_rows),
    'EventDate': pd.to_datetime(np.random.choice(pd.date_range('2020-01-01', '2023-12-31'), num_rows)),
    'ReportDate': pd.to_datetime(np.random.choice(pd.date_range('2020-01-01', '2023-12-31'), num_rows))
}
df = pd.DataFrame(data)

# 2. Custom function
def clean_country(name):
    name = str(name).lower().strip()
    if 'united states' in name or 'usa' in name:
        return 'United States'
    return name.title()

df['Country_Clean'] = df['Country'].apply(clean_country)

# 3. Category conversion
print(f"Before: {df['Country_Clean'].memory_usage(deep=True)}")
df['Country_Clean'] = df['Country_Clean'].astype('category')
print(f"After: {df['Country_Clean'].memory_usage(deep=True)}")

# 4. Lag and Day of Week
df['ReportingLagDays'] = (df['ReportDate'] - df['EventDate']).dt.days
df['DayOfWeekEvent'] = df['EventDate'].dt.day_name()
```

### 4. Sorting, Filtering & Selection

**Beginner Task:**
```python
import pandas as pd

# 1. Create beneficiary_records.csv
data = {
    'BeneficiaryID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Age': [25, 34, 28, 40, 30, 22, 45, 38],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Location': ['Camp A', 'Village B', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A', 'Village C'],
    'AssistanceReceived': ['Food', 'Shelter', 'Medical', 'Food', 'Shelter', 'Food', 'Medical', 'Shelter']
}
pd.DataFrame(data).to_csv('beneficiary_records.csv', index=False)

# 2. Load
df = pd.read_csv('beneficiary_records.csv')

# 3. Filter Food
print(df[df['AssistanceReceived'] == 'Food'])

# 4. Sort Age
print(df.sort_values('Age'))

# 5. Filter Female and Sort
print(df[df['Gender'] == 'Female'].sort_values('BeneficiaryID', ascending=False))
```

**Intermediate Task:**
```python
# 2. Complex Filter
print(df[((df['Gender'] == 'Male') & (df['Age'] < 30)) | ((df['Gender'] == 'Female') & (df['AssistanceReceived'] == 'Medical'))])

# 3. .loc selection
print(df.loc[df['AssistanceReceived'] == 'Shelter', ['BeneficiaryID', 'Location']])

# 4. .iloc selection
print(df.iloc[-5:, 1:])

# 5. isin()
print(df[df['Location'].isin(['Camp A', 'Village B'])])
```

**Master Task:**
```python
import pandas as pd
import numpy as np

# 1. Create large DataFrame
num_rows = 100000
data = {
    'TransactionID': np.arange(num_rows),
    'Amount': np.random.randint(10, 1000, num_rows),
    'Currency': np.random.choice(['USD', 'EUR', 'GBP'], num_rows),
    'Timestamp': pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2023-12-31'), num_rows)),
    'Processor': np.random.choice(['Stripe', 'PayPal', 'Square'], num_rows)
}
df = pd.DataFrame(data)

# 2. Median Amount
median_amt = df['Amount'].median()

# 3. Complex Boolean Indexing
weekend_mask = df['Timestamp'].dt.dayofweek >= 5
filtered = df[(df['Currency'] == 'USD') & (df['Amount'] > median_amt) & weekend_mask]

# 4. Query method
filtered_query = df.query("Currency == 'USD' and Amount > @median_amt and Timestamp.dt.dayofweek >= 5")

# 5. Index-based optimization
df_indexed = df.set_index('Processor')
print(df_indexed.loc['Stripe'])
```

---

## Phase 3: Pandas Analysis

### 1. Grouping & Aggregation

**Beginner Task:**
```python
import pandas as pd

# 1. Create aid_distribution.csv
data = {
    'Country': ['Kenya', 'Uganda', 'Kenya', 'Ethiopia', 'Uganda', 'Kenya', 'Ethiopia', 'Uganda'],
    'AidType': ['Food', 'Medical', 'Shelter', 'Food', 'Medical', 'Food', 'Shelter', 'Food'],
    'AmountUSD': [100000, 150000, 80000, 120000, 200000, 90000, 110000, 180000],
    'Year': [2022, 2022, 2023, 2022, 2023, 2023, 2023, 2022]
}
pd.DataFrame(data).to_csv('aid_distribution.csv', index=False)

# 2. Load
df = pd.read_csv('aid_distribution.csv')

# 3. Total per Country
print(df.groupby('Country')['AmountUSD'].sum())

# 4. Avg per AidType
print(df.groupby('AidType')['AmountUSD'].mean())

# 5. Count per Country and Year
print(df.groupby(['Country', 'Year'])['AidType'].count())
```

**Intermediate Task:**
```python
# 2. Named Aggregations
print(df.groupby('Country').agg(
    total_amt=('AmountUSD', 'sum'),
    avg_amt=('AmountUSD', 'mean'),
    unique_types=('AidType', 'nunique')
))

# 3. Min, Max, Median
print(df.groupby('AidType')['AmountUSD'].agg(['min', 'max', 'median']))

# 4. Year summary
print(df.groupby('Year').agg(
    total_amt=('AmountUSD', 'sum'),
    country_count=('Country', 'nunique')
))
```

**Master Task:**
```python
# 2. Custom Aggregation (CV)
def cv(x):
    return x.std() / x.mean()

print(df.groupby('Country')['AmountUSD'].agg(cv))

# 3. transform()
df['CountryAvgAmount'] = df.groupby('Country')['AmountUSD'].transform('mean')

# 4. filter() total > 500k
print(df.groupby('Country').filter(lambda x: x['AmountUSD'].sum() > 500000))

# 5. filter() AidType in >= 3 countries
print(df.groupby('AidType').filter(lambda x: x['Country'].nunique() >= 3))
```

### 2. Counting & Deduplication

**Beginner Task:**
```python
import pandas as pd

# 1. Create event_logs.csv
data = {
    'LogID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Timestamp': ['2023-01-01 10:00:00', '2023-01-01 10:05:00', '2023-01-01 10:00:00', '2023-01-02 11:00:00', '2023-01-01 10:05:00', '2023-01-03 12:00:00', '2023-01-02 11:00:00', '2023-01-04 13:00:00'],
    'EventType': ['Login', 'View Page', 'Login', 'Logout', 'View Page', 'Login', 'Logout', 'View Page'],
    'UserID': ['userA', 'userB', 'userA', 'userC', 'userB', 'userA', 'userC', 'userD']
}
pd.DataFrame(data).to_csv('event_logs.csv', index=False)

# 2. Load
df = pd.read_csv('event_logs.csv')

# 3. value_counts
print(df['EventType'].value_counts())

# 4. drop_duplicates
df_no_exact = df.drop_duplicates()

# 5. drop_duplicates subset
df_no_user_event = df.drop_duplicates(subset=['UserID', 'EventType'])
```

**Intermediate Task:**
```python
# 2. Normalized counts
print(df['EventType'].value_counts(normalize=True))

# 3. nunique
print(df['UserID'].nunique(), df['EventType'].nunique())

# 4. First record per UserID
print(df.drop_duplicates(subset=['UserID'], keep='first'))

# 5. Identify duplicates
print(df[df.duplicated(subset=['UserID'], keep=False)])
```

**Master Task:**
```python
from thefuzz import process, fuzz
import pandas as pd

# 1. Create partner_organizations.csv
data = {
    'OrgID': [1, 2, 3, 4, 5, 6, 7],
    'OrgName': ['Save the Children', 'Save The Children Intl.', 'Doctors Without Borders', 'Medecins Sans Frontieres', 'Save Childrn', 'Doctors W/O Borders', 'Save the Children'],
    'ContactPerson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'City': ['New York', 'NYC', 'Paris', 'Paris', 'New-York', 'London', 'New York']
}
df = pd.DataFrame(data)

# 4. Fuzzy Clean OrgName
canonical_orgs = ['Save the Children', 'Doctors Without Borders', 'Medecins Sans Frontieres']
def fuzzy_clean(name, choices):
    match, score = process.extractOne(name, choices, scorer=fuzz.token_sort_ratio)
    return match if score > 80 else name

df['OrgName_Clean'] = df['OrgName'].apply(lambda x: fuzzy_clean(x, canonical_orgs))

# 5. Fuzzy Clean City
canonical_cities = ['New York', 'Paris', 'London']
df['City_Clean'] = df['City'].apply(lambda x: fuzzy_clean(x, canonical_cities))

# 6. Consolidate
consolidated = df.groupby(['OrgName_Clean', 'City_Clean'])['ContactPerson'].apply(list).reset_index()
```

### 3. Creating Metrics & Binning

**Beginner Task:**
```python
import pandas as pd

# 1. Create health_records.csv
data = {
    'PatientID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'WeightKg': [70, 85, 60, 90, 75, 80, 65, 78, 88, 92],
    'HeightCm': [175, 180, 160, 185, 170, 178, 165, 172, 182, 190],
    'BloodPressureSystolic': [120, 135, 110, 150, 125, 140, 115, 130, 145, 160],
    'BloodPressureDiastolic': [80, 85, 70, 95, 82, 90, 75, 80, 92, 100]
}
df = pd.DataFrame(data)

# 3. BMI
df['BMI'] = df['WeightKg'] / (df['HeightCm']/100)**2

# 4. PulsePressure
df['PulsePressure'] = df['BloodPressureSystolic'] - df['BloodPressureDiastolic']

# 5. Bin BMI
bins = [0, 18.5, 25, 30, 100]
labels = ['Underweight', 'Normal', 'Overweight', 'Obese']
df['BMICategory'] = pd.cut(df['BMI'], bins=bins, labels=labels)
print(df['BMICategory'].value_counts())
```

**Intermediate Task:**
```python
import numpy as np

# 2. HypertensionRisk
df['HypertensionRisk'] = np.where((df['BloodPressureSystolic'] >= 140) | (df['BloodPressureDiastolic'] >= 90), 'High', 'Normal')

# 3. qcut Weight
df['WeightQuintile'] = pd.qcut(df['WeightKg'], q=5, labels=['Lightest', 'Lighter', 'Middle', 'Heavier', 'Heaviest'])

# 4. qcut PulsePressure
df['PPTertile'] = pd.qcut(df['PulsePressure'], q=3, labels=['Low PP', 'Medium PP', 'High PP'])
```

**Master Task:**
```python
import pandas as pd

# 1-3. Load Data
df_school = pd.read_csv('school_data.csv')
df_poverty = pd.read_csv('district_poverty.csv')

# 4. KPI: TotalDistrictFunding
df_school['SchoolFunding'] = df_school['FundingPerStudent'] * df_school['Enrollment']
district_funding = df_school.groupby('District')['SchoolFunding'].sum().reset_index()
df_kpi = pd.merge(district_funding, df_poverty, on='District')

# 5. Dynamic Binning TestScoreAverage
mean_score = df_school['TestScoreAverage'].mean()
std_score = df_school['TestScoreAverage'].std()
bins = [-np.inf, mean_score - 0.5*std_score, mean_score + 0.5*std_score, np.inf]
labels = ['Below Average', 'Average', 'Above Average']
df_school['ScoreCategory'] = pd.cut(df_school['TestScoreAverage'], bins=bins, labels=labels)

# 6. Weighted Average Funding
def weighted_avg(x):
    return (x['FundingPerStudent'] * x['Enrollment']).sum() / x['Enrollment'].sum()

print(df_school.groupby('District').apply(weighted_avg))
```
