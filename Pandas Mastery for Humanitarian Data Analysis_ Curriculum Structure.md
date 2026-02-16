# Pandas Mastery for Humanitarian Data Analysis: Curriculum Structure

This curriculum is designed to take a beginner to a master level in Pandas, specifically tailored for NGO and humanitarian data contexts.

## Phase 2: Pandas Core (Data Wrangling)

### 1. Data Loading & Initial Inspection
*   **Beginner:** `pd.read_csv()`, `df.head()`, `df.tail()`.
*   **Intermediate:** Handling delimiters, encoding, and `df.info()`, `df.describe()`.
*   **Master:** Memory optimization during loading (`dtype`, `chunksize`), reading from SQL/APIs.

### 2. Handling Missing Values
*   **Beginner:** `isna()`, `dropna()`.
*   **Intermediate:** `fillna()` with constants, forward/backward fill.
*   **Master:** Conditional imputation based on group statistics, identifying patterns in missingness.

### 3. String Cleaning & Type Conversion
*   **Beginner:** `.str.lower()`, `.str.strip()`, `astype()`.
*   **Intermediate:** Regex-based cleaning (`.str.replace()`, `.str.extract()`), handling date formats.
*   **Master:** Custom vectorised functions, complex date-time arithmetic, category types for memory efficiency.

### 4. Sorting, Filtering & Selection
*   **Beginner:** `df[df['col'] > x]`, `sort_values()`.
*   **Intermediate:** `.loc[]`, `.iloc[]`, multiple conditions, `isin()`.
*   **Master:** Boolean indexing with complex logic, query method, index-based optimization.

---

## Phase 3: Pandas Analysis (Insights & Metrics)

### 1. Grouping & Aggregation
*   **Beginner:** `groupby().sum()`, `groupby().mean()`.
*   **Intermediate:** `.agg()` with multiple functions, named aggregations.
*   **Master:** Custom aggregation functions, transform, and filter operations within groups.

### 2. Counting & Deduplication
*   **Beginner:** `value_counts()`, `drop_duplicates()`.
*   **Intermediate:** `nunique()`, `value_counts(normalize=True)`.
*   **Master:** Fuzzy matching for deduplication, identifying "near-duplicates" in beneficiary data.

### 3. Creating Metrics & Binning
*   **Beginner:** Simple column arithmetic (e.g., `df['a'] / df['b']`).
*   **Intermediate:** `pd.cut()`, `pd.qcut()` for demographic binning.
*   **Master:** Complex KPI calculation (e.g., aid per capita with external population data merging), weighted averages.

### 4. Data Merging & Reshaping
*   **Beginner:** `pd.concat()`.
*   **Intermediate:** `pd.merge()` (left, right, inner, outer).
*   **Master:** `pivot_table()`, `melt()`, multi-index handling.
