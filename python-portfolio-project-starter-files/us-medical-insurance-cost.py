import pandas as pd

# Load the dataset
df = pd.read_csv('insurance.csv')

# 1) Calculate the average age of the patients in the database
average_age = df['age'].mean()
print(f"Average age of patients: {average_age:.2f}")

# 2) Analyze where the majority of individuals are from
region_counts = df['region'].value_counts()
most_common_region = region_counts.idxmax()
most_common_region_count = region_counts.max()
print(f"Most common region: {most_common_region} with {most_common_region_count} individuals")

# 3) Look at the cost difference between smokers vs non-smokers
average_cost_smokers = df[df['smoker'] == 'yes']['charges'].mean()
average_cost_non_smokers = df[df['smoker'] == 'no']['charges'].mean()
print(f"Average cost for smokers: ${average_cost_smokers:.2f}")
print(f"Average cost for non-smokers: ${average_cost_non_smokers:.2f}")

# 4) Figure out the average age for someone who has at least one child
average_age_with_children = df[df['children'] > 0]['age'].mean()
print(f"Average age of individuals with at least one child: {average_age_with_children:.2f}")
