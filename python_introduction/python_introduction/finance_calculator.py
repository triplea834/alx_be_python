# finance_calculator.py

# Step 1: Get user input for income and expenses
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

# Step 2: Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Step 3: Calculate projected annual savings with 5% interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Step 4: Output the results
print(f"Monthly savings: {monthly_savings}")
print(f"Projected annual savings after interest: {projected_savings}")
