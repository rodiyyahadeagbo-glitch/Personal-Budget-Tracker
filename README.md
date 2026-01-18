# Personal-Budget-Tracker
A financial tracking tool that calculates debt-to-income ratios and provides automated spending advice based on user input.

# Features
* **Income Aggregation:** Calculates total monthly earnings from salary, side hustles, and other sources.
* **Expense Tracking:** Breaks down costs across Rent, Utilities, Food, Transport, and Entertainment.
* **Financial Advisory:** Automatically determines if a user is overspending or breaking even by comparing total income vs. total expenses.

# Technical Highlights
* **Precision Formatting:** Utilizes Python's f-string formatting (`:.2f`) to display currency accurately to two decimal places.
* **Modular Logic:** Uses dedicated functions (`calc_MonthlyIncome` and `calc_MonthlyExpenses`) to keep code clean and organized.
* **Interactive CLI:** Provides a user-friendly command-line interface for data entry.

# Installation
1. Clone the repo: `git clone [your-link-here]`
2. Run the script: `python budget_calculator.py`
