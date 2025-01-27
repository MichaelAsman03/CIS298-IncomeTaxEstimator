# Function to calculate taxes owed in each bracket
def calculate_taxes_by_bracket(agi):
    brackets = [
        (10275, 0.10),    # 10% for income up to $10,275
        (41775, 0.12),    # 12% for income up to $41,775
        (89075, 0.22),    # 22% for income up to $89,075
        (170050, 0.24),   # 24% for income up to $170,050
        (215950, 0.32),   # 32% for income up to $215,950
        (539900, 0.35),   # 35% for income up to $539,900
        (float('inf'), 0.37)  # 37% for income above $539,900
    ]
    taxes_owed_per_bracket = []
    total_taxes = 0
    previous_limit = 0

    for limit, rate in brackets:
        if agi > previous_limit:
            taxable_amount = min(agi, limit) - previous_limit
            taxes = taxable_amount * rate
            taxes_owed_per_bracket.append((rate, taxes))
            total_taxes += taxes
            previous_limit = limit
        else:
            taxes_owed_per_bracket.append((rate, 0.0))

    return taxes_owed_per_bracket, total_taxes

# Display a welcome message
print("Welcome to the Income Tax Estimator!")


# Get income from the user
gross_income = 0
while True:
    income = input("Enter an income amount (done or stop): ")
    if income.lower() == 'done':
        break
    gross_income += float(income)

# Get deductions from the user
total_deductions = 0
while True:
    deduction = input("Enter a deduction amount (done or stop): ")
    if deduction.lower() == 'done':
        break
    total_deductions += float(deduction)

# Apply standard deduction if necessary
standard_deduction = 14600
if total_deductions < standard_deduction:
    total_deductions = standard_deduction

# Calculate AGI and taxes
adjusted_gross_income = gross_income - total_deductions
taxes_by_bracket, total_taxes_owed = calculate_taxes_by_bracket(adjusted_gross_income)

# Display the results
print("\n--- Tax Calculator Results ---")
print(f"Gross Income : ${gross_income:,.2f}")
print(f"Total Deductions : ${total_deductions:,.2f}")
print(f"Adjusted Gross Income : ${adjusted_gross_income:,.2f}")

for rate, taxes in taxes_by_bracket:
    print(f"Taxes Owed at {int(rate * 100)}% bracket : ${taxes:,.2f}")

print(f"Total Taxes Owed : ${total_taxes_owed:,.2f}")
print(f"Taxes Owed as percentage of gross income: {total_taxes_owed / gross_income * 100:.2f}%")
print(f"Taxes Owed as percentage of adjusted gross income: {total_taxes_owed / adjusted_gross_income * 100:.2f}%")
