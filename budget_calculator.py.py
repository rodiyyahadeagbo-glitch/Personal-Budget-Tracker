def user_info ():
    name = input("Enter your name:")
    print(f"Hello {name}! Let's calculate your monthly budget.\n")
    return name


def calc_MonthlyIncome():

    print("\n---MONTHLY INCOME---")
    Salary_Amount = float(input("Enter your monthly salary: "))
    print(f"${Salary_Amount:.2f}")
    side_income = float(input("Enter any side income: "))
    print(f"${side_income:.2f}")
    other_income = float(input("Enter any other income: "))
    print(f"${other_income:.2f}")


    Total_MonthlyIncome = Salary_Amount + side_income + other_income

    print(f"\nYour total monthly income ${Total_MonthlyIncome:.2f}\n")
    return Total_MonthlyIncome


def calc_MonthlyExpenses():

    print("\n--- MONTHLY EXPENSES---")
    Rent = float(input("Enter Rent/mortgage: "))
    print(f"${Rent:.2f}")
    utilities = float(input("Enter utilities (electricity, water , internet): "))
    print(f"${utilities:.2f}")
    food_expenses = float(input("Enter food expenses: "))
    print(f"${food_expenses:.2f}")
    transportation_costs = float(input("Enter transportation costs: "))
    print(f"${transportation_costs:.2f}")
    entertainment_budget = float(input("Enter Entertainment budget: "))
    print(f"${entertainment_budget:.2f}")
    Other_Expenses = float(input("Enter Other Expenses: "))
    print(f"${Other_Expenses:.2f}")

    Total_MonthlyExpenses = (Rent + utilities + food_expenses + transportation_costs + entertainment_budget + Other_Expenses)

    print(f"\nYour total monthly expenses ${Total_MonthlyExpenses:.2f}\n")
    return Total_MonthlyExpenses



print("=========================================================================")
print("PERSONAL BUDGET CALCULATOR")
print("=========================================================================")

name = user_info()

income = calc_MonthlyIncome()

expenses = calc_MonthlyExpenses()

print("=========================================================================")
print("BUDGET ANALYSIS")
print("=========================================================================\n")


print(f"Total Income: ${income}")
print(f"Total Expenses: ${expenses}")

Remaining_Money = income - expenses

print(f"Remaining Money: ${Remaining_Money}\n")

if Remaining_Money > 0:
    print("Great job! You're saving money!\n")

elif Remaining_Money == 0:
    print("Not bad! breaking even.\n")

elif Remaining_Money < 0:
    print("You are overspending!, be careful\n")

else:
    pass 


