
# Tax Bracket Calculator
# Write a function tax_bracket(income: float) -> str that returns the tax bracket label:

# "Low" for income < 30,000
# "Middle" for 30,000 ≤ income < 100,000
# "High" for income ≥ 100,000

def tax_bracket(income: float):

    if income < 30000:
        return "Low"
    elif income >= 30000 and income < 100000:
        return "Middle"
    else:
        return "High"
income = float(input("Enter your income: "))
result = tax_bracket(income)
print(result)

# Loan Eligibility
# Implement eligible_for_loan(age: int, credit_score: int, debt_to_income: float) -> bool that returns True only if:

# Age is at least 21,
# Credit score is 650 or higher, and
# Debt‑to‑income ratio is below 0.4.

def eligible_for_loan(age: int, credit_score: int, debt_to_income: float) -> bool:
    if Age >= 21 and credit_score >= 650 and debt_to_income < 0.4:
        return True
    else:
        return False

Age = int(input("enter a Age = "))
credit_score = int(input("Enter a credit score = "))
debt_to_income = float(input("Enter debt income ratio = "))

approval = eligible_for_loan(Age,credit_score,debt_to_income)
print(approval)


# Discount Determination
# Create apply_discount(purchase_total: float, is_member: bool) -> float that applies:

# 20% discount if the customer is a member and the total exceeds $200,
# 10% discount if the total exceeds $200 but the customer is not a member,
# 5% discount for members on any purchase under $200,
# No discount otherwise.
# Return the final amount after discount.

def apply_discount(purchase_total: float, is_member: bool) -> float:

    if is_member and purchase_total > 200:
        discount = 20
    elif purchase_total > 200:
        discount = 10
    elif is_member and purchase_total < 200:
        discount = 5
    else:
        discount = 0

    final_amount = purchase_total - (purchase_total * discount / 100)
    return final_amount

purchase_total = float(input("Enter purchase amount: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

result = apply_discount(purchase_total, is_member)

print("Final amount:", result)


# Temperature Advisory
# Write weather_advice(temp_c: float) -> str returning advice based on temperature:

# "Wear a coat" if temp ≤ 0°C,
# "Light jacket" if 0 < temp ≤ 15°C,
# "T‑shirt" if 15 < temp ≤ 25°C,
# "Stay hydrated" if temp > 25°C.

def weather_advice(temp_c: float) -> str:

    if temp_c <= 0:
        return "Wear a coat"
    elif temp_c <= 15:
        return "Light jacket"
    elif temp_c <= 25:
        return "T-shirt"
    else:
        return "Stay hydrated"

temp_c = float(input("Enter temperature: "))
result = weather_advice(temp_c)
print(result)
