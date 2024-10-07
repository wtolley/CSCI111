# Class Activity Program: Financial Trend Analysis

# Provided monthly revenue data for two years (in thousands of dollars)
revenues = [
    20, 22, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    34, 36, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46
]

# Task 1: Split the Data into Quarters
# Each quarter is a sublist containing three months of revenue data
quarters = [revenues[i:i+3] for i in range(0, len(revenues), 3)]

print(quarters)

# Display the quarterly data
print("Quarterly Revenue Data:")
for i, quarter in enumerate(quarters):
    print(f"Q{i+1}: {quarter}")

# Task 2: Calculate Quarterly Growth
# Growth percentage from one quarter to the next, starting from the second quarter
growth_percentages = [
    ((sum(quarters[i]) - sum(quarters[i-1])) / sum(quarters[i-1])) * 100
    for i in range(1, len(quarters))
]

# Display growth percentages between quarters
print("\nQuarterly Growth Percentages:")
for i, growth in enumerate(growth_percentages):
    print(f"Growth from Q{i+1} to Q{i+2}: {growth:.2f}%")

# Task 3: Identify Best and Worst Quarters
highest_growth = max(growth_percentages)
lowest_growth = min(growth_percentages)

best_quarter_index = growth_percentages.index(highest_growth) + 1  # +1 to adjust for skipping Q1
worst_quarter_index = growth_percentages.index(lowest_growth) + 1

# Display the results
print(f"\nHighest Growth: Q{best_quarter_index + 1} ({highest_growth:.2f}%)")
print(f"Lowest Growth: Q{worst_quarter_index + 1} ({lowest_growth:.2f}%)")

# Output Summary
print("\nSummary:")
print(f"Quarters Data: {quarters}")
print(f"Growth Percentages: {growth_percentages}")
