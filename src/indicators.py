def will_pay_index(gender, age, monthly_income, monthly_expenses):
    
    if gender == "M" and age < 40 and monthly_income > monthly_expenses:
        return 1
    if gender == "M" and age > 40 and monthly_income < monthly_expenses:
        return 0
    if gender == "F" and age < 40 and monthly_income > monthly_expenses:
        return 1
    if gender == "F" and age > 40 and monthly_income < monthly_expenses:
        return 0
