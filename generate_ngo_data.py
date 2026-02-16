import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_ngo_data():
    # --- Phase 2: Data Loading & Initial Inspection ---
    # ngo_projects.csv (for 1.1 Beginner)
    data_projects = {
        'ProjectID': [101, 102, 103, 104, 105],
        'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia'],
        'StartDate': ['2023-01-15', '2023-02-01', '2023-03-10', '2023-04-05', '2023-05-20'],
        'EndDate': ['2023-06-30', '2023-07-15', '2023-08-20', '2023-09-10', '2023-10-30'],
        'Budget': [150000, 200000, 120000, 180000, 250000]
    }
    df_projects = pd.DataFrame(data_projects)
    df_projects.to_csv('ngo_projects.csv', index=False)

    # beneficiary_data.csv (for 1.1 Beginner practice)
    data_beneficiary_basic = {
        'BeneficiaryID': [1, 2, 3, 4, 5],
        'Age': [25, 34, 28, 40, 30],
        'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
        'Location': ['Camp A', 'Village B', 'Camp A', 'Village C', 'Camp B'],
        'AssistanceType': ['Food', 'Shelter', 'Medical', 'Food', 'Shelter']
    }
    df_beneficiary_basic = pd.DataFrame(data_beneficiary_basic)
    df_beneficiary_basic.to_csv('beneficiary_data.csv', index=False)

    # large_ngo_projects.csv (for 1.3 Master)
    num_rows_large = 100000
    large_data = {
        'ProjectID': np.arange(1, num_rows_large + 1),
        'Region': np.random.choice(['East Africa', 'South Asia', 'West Africa', 'Latin America'], num_rows_large),
        'Status': np.random.choice(['Active', 'Completed', 'Pending'], num_rows_large),
        'Budget': np.random.randint(50000, 500000, num_rows_large)
    }
    df_large_sample = pd.DataFrame(large_data)
    df_large_sample.to_csv('large_ngo_projects.csv', index=False)

    # --- Phase 2: Handling Missing Values ---
    # beneficiary_data_missing.csv (for 2.1 Beginner, 2.2 Intermediate, 2.3 Master)
    data_missing = {
        'BeneficiaryID': [1, 2, 3, 4, 5, 6, 7],
        'Age': [25, 34, np.nan, 45, 19, np.nan, 50],
        'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Location': ['Camp A', 'Village B', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A'],
        'AssistanceType': ['Food', 'Shelter', np.nan, 'Food', 'Medical', 'Shelter', 'Food']
    }
    df_missing = pd.DataFrame(data_missing)
    df_missing.to_csv('beneficiary_data_missing.csv', index=False)

    # project_updates.csv (for 2.1 Beginner, 2.2 Intermediate practice)
    data_project_updates = {
        'UpdateID': [1, 2, 3, 4, 5, 6],
        'ProjectID': [101, 102, 101, 103, 102, 104],
        'Date': ['2023-01-20', '2023-02-05', '2023-03-15', '2023-04-10', '2023-05-25', '2023-06-05'],
        'Status': ['On Track', 'Completed', np.nan, 'Delayed', 'On Track', np.nan],
        'Notes': ['Initial report', 'Finalized', 'Needs review', np.nan, 'Mid-term update', np.nan]
    }
    df_project_updates = pd.DataFrame(data_project_updates)
    df_project_updates.to_csv('project_updates.csv', index=False)

    # health_data.csv (for 2.3 Master practice)
    data_health = {
        'PatientID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Age': [30, 45, 22, 60, 35, 50, 28, 42, 55, 65],
        'Weight': [70, 85, 60, 90, 75, 80, 65, 78, 88, 92],
        'Diagnosis': ['Flu', 'Malaria', 'Flu', 'Typhoid', 'Flu', 'Malaria', 'Flu', 'Typhoid', 'Malaria', 'Flu'],
        'Medication': ['A', 'B', np.nan, 'C', 'A', 'B', np.nan, 'C', 'B', np.nan]
    }
    df_health = pd.DataFrame(data_health)
    # Intentionally create a pattern where Medication is often missing for 'Flu'
    df_health.loc[df_health['Diagnosis'] == 'Flu', 'Medication'] = np.nan
    df_health.to_csv('health_data.csv', index=False)

    # --- Phase 2: String Cleaning & Type Conversion ---
    # messy_data.csv (for 3.1 Beginner)
    data_messy = {
        'ProjectID': ['101', '102', '103 ', '104', '105'],
        'Region': ['East Africa ', 'south asia', 'WEST AFRICA', 'East Africa', 'South Asia'],
        'Status': ['Active', 'Completed ', 'Pending', 'active', 'Completed'],
        'Budget': ['150000', '200000', '120000', '180000', '250000'] # Loaded as string
    }
    df_messy = pd.DataFrame(data_messy)
    df_messy.to_csv('messy_data.csv', index=False)

    # item_data.csv (for 3.1 Beginner practice)
    data_item = {
        'Item': ['   apple', 'BANANA ', 'orange', ' GRAPES  '],
        'Quantity': ['10', '5', '12', '8'],
        'Price': ['1.20', '0.75', '2.50', '3.00']
    }
    df_item = pd.DataFrame(data_item)
    df_item.to_csv('item_data.csv', index=False)

    # advanced_messy_data.csv (for 3.2 Intermediate)
    data_advanced_messy = {
        'ProjectCode': ['NGO-101', 'PROJ_102', 'NGO-103', 'P-104', 'NGO-105'],
        'Description': ['Food distribution in area A', 'Shelter for displaced families', 'Medical aid for children', 'Water sanitation project', 'Education support'],
        'StartDate': ['2023/01/15', '02-01-2023', 'March 10, 2023', '2023-04-05', '2023-05-20'],
        'Beneficiaries': ['1,500', '2,000', '1,200', '1,800', '2,500'] # String with comma
    }
    df_advanced_messy = pd.DataFrame(data_advanced_messy)
    df_advanced_messy.to_csv('advanced_messy_data.csv', index=False)

    # transaction_data.csv (for 3.2 Intermediate practice)
    data_transaction = {
        'TransactionID': ['TRX-ABC-123', 'TXN_DEF_456', 'GHI789', 'TRX-JKL-010'],
        'Timestamp': ['2023-01-01 10:30:00', 'Jan 2, 23 11:00 AM', '03/03/2023 13:45', '2023-04-04 09:00:00'],
        'Amount': [100, 200, 150, 300]
    }
    df_transaction = pd.DataFrame(data_transaction)
    df_transaction.to_csv('transaction_data.csv', index=False)

    # large_country_data.csv (for 3.3 Master practice)
    num_rows_country = 100000
    countries = ['United States', 'USA', 'United States of America', '   united states', 'Canada', 'Mexico', 'UK', 'United Kingdom']
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]

    data_country = {
        'Country': np.random.choice(countries, num_rows_country),
        'EventDate': np.random.choice(date_range, num_rows_country),
        'ReportDate': np.random.choice(date_range, num_rows_country)
    }
    df_country = pd.DataFrame(data_country)
    df_country['ReportDate'] = df_country['EventDate'] + pd.to_timedelta(np.random.randint(1, 30, num_rows_country), unit='D')
    df_country.to_csv('large_country_data.csv', index=False)

    # --- Phase 2: Sorting, Filtering & Selection ---
    # ngo_projects_cleaned.csv (for 4.1 Beginner, 4.2 Intermediate, 4.3 Master)
    data_projects_cleaned = {
        'ProjectID': [101, 102, 103, 104, 105, 106, 107],
        'Region': ['East Africa', 'South Asia', 'West Africa', 'East Africa', 'South Asia', 'West Africa', 'East Africa'],
        'Budget': [150000, 200000, 120000, 180000, 250000, 130000, 190000],
        'Status': ['Active', 'Completed', 'Active', 'Completed', 'Active', 'Pending', 'Active'],
        'StartDate': ['2023-01-15', '2023-02-01', '2023-03-10', '2023-04-05', '2023-05-20', '2023-06-01', '2023-07-10']
    }
    df_projects_cleaned = pd.DataFrame(data_projects_cleaned)
    df_projects_cleaned.to_csv('ngo_projects_cleaned.csv', index=False)

    # beneficiary_records.csv (for 4.1 Beginner, 4.2 Intermediate practice)
    data_beneficiary_records = {
        'BeneficiaryID': [1, 2, 3, 4, 5, 6, 7, 8],
        'Age': [25, 34, 28, 40, 30, 22, 45, 38],
        'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'Location': ['Camp A', 'Village B', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A', 'Village C'],
        'AssistanceReceived': ['Food', 'Shelter', 'Medical', 'Food', 'Shelter', 'Food', 'Medical', 'Shelter']
    }
    df_beneficiary_records = pd.DataFrame(data_beneficiary_records)
    df_beneficiary_records.to_csv('beneficiary_records.csv', index=False)

    # --- Phase 3: Grouping & Aggregation ---
    # aid_distribution.csv (for 1.1 Beginner, 1.2 Intermediate, 1.3 Master practice)
    data_aid_distribution = {
        'Country': ['Kenya', 'Uganda', 'Kenya', 'Ethiopia', 'Uganda', 'Kenya', 'Ethiopia', 'Uganda'],
        'AidType': ['Food', 'Medical', 'Shelter', 'Food', 'Medical', 'Food', 'Shelter', 'Food'],
        'AmountUSD': [100000, 150000, 80000, 120000, 200000, 90000, 110000, 180000],
        'Year': [2022, 2022, 2023, 2022, 2023, 2023, 2023, 2022]
    }
    df_aid_distribution = pd.DataFrame(data_aid_distribution)
    df_aid_distribution.to_csv('aid_distribution.csv', index=False)

    # --- Phase 3: Counting & Deduplication ---
    # beneficiary_data_dedup.csv (for 2.1 Beginner, 2.2 Intermediate)
    data_beneficiary_dedup = {
        'BeneficiaryID': [1, 2, 3, 1, 4, 5, 2, 6],
        'Age': [25, 34, 28, 25, 40, 30, 34, 55],
        'Gender': ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'AssistanceType': ['Food', 'Shelter', 'Food', 'Food', 'Medical', 'Shelter', 'Shelter', 'Food'],
        'Location': ['Camp A', 'Village B', 'Camp A', 'Camp A', 'Village C', 'Camp B', 'Village B', 'Camp A']
    }
    df_beneficiary_dedup = pd.DataFrame(data_beneficiary_dedup)
    df_beneficiary_dedup.to_csv('beneficiary_data_dedup.csv', index=False)

    # event_logs.csv (for 2.1 Beginner, 2.2 Intermediate practice)
    data_event_logs = {
        'LogID': [1, 2, 3, 4, 5, 6, 7, 8],
        'Timestamp': ['2023-01-01 10:00:00', '2023-01-01 10:05:00', '2023-01-01 10:00:00', '2023-01-02 11:00:00', '2023-01-01 10:05:00', '2023-01-03 12:00:00', '2023-01-02 11:00:00', '2023-01-04 13:00:00'],
        'EventType': ['Login', 'View Page', 'Login', 'Logout', 'View Page', 'Login', 'Logout', 'View Page'],
        'UserID': ['userA', 'userB', 'userA', 'userC', 'userB', 'userA', 'userC', 'userD']
    }
    df_event_logs = pd.DataFrame(data_event_logs)
    df_event_logs.to_csv('event_logs.csv', index=False)

    # partner_organizations.csv (for 2.3 Master practice)
    data_partners = {
        'OrgID': [1, 2, 3, 4, 5, 6, 7],
        'OrgName': ['Save the Children', 'Save The Children Intl.', 'Doctors Without Borders', 'Medecins Sans Frontieres', 'Save Childrn', 'Doctors W/O Borders', 'Save the Children'],
        'ContactPerson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'City': ['New York', 'NYC', 'Paris', 'Paris', 'New-York', 'London', 'New York']
    }
    df_partners = pd.DataFrame(data_partners)
    df_partners.to_csv('partner_organizations.csv', index=False)

    # --- Phase 3: Creating Metrics & Binning ---
    # health_records.csv (for 3.1 Beginner, 3.2 Intermediate practice)
    data_health_records = {
        'PatientID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'WeightKg': [70, 85, 60, 90, 75, 80, 65, 78, 88, 92],
        'HeightCm': [175, 180, 160, 185, 170, 178, 165, 172, 182, 190],
        'BloodPressureSystolic': [120, 135, 110, 150, 125, 140, 115, 130, 145, 160],
        'BloodPressureDiastolic': [80, 85, 70, 95, 82, 90, 75, 80, 92, 100]
    }
    df_health_records = pd.DataFrame(data_health_records)
    df_health_records.to_csv('health_records.csv', index=False)

    # school_data.csv (for 3.3 Master practice)
    data_school = {
        'SchoolID': [1, 2, 3, 4, 5, 6, 7, 8],
        'District': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
        'Enrollment': [500, 700, 600, 800, 550, 720, 630, 850],
        'FundingPerStudent': [1000, 950, 1100, 900, 1050, 980, 1120, 920],
        'TestScoreAverage': [75, 80, 70, 85, 78, 82, 72, 88]
    }
    df_school = pd.DataFrame(data_school)
    df_school.to_csv('school_data.csv', index=False)

    # district_poverty.csv (for 3.3 Master practice)
    data_poverty = {
        'District': ['North', 'South', 'East', 'West'],
        'PovertyRate': [0.15, 0.10, 0.20, 0.08]
    }
    df_poverty = pd.DataFrame(data_poverty)
    df_poverty.to_csv('district_poverty.csv', index=False)

    print("All synthetic NGO datasets generated successfully.")

if __name__ == '__main__':
    generate_ngo_data()
