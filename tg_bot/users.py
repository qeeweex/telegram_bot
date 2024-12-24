class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.income = [] 
        self.expenses = [] 

    def add_income(self, amount, description):
        self.income.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def get_balance(self):
        total_income = sum(item[0] for item in self.income)
        total_expenses = sum(item[0] for item in self.expenses)
        return total_income - total_expenses

    def get_income_report(self):
        report = ""
        for amount, description in self.income:
            report += f"{description}: {amount}\n"
        return report if report else "Нет доходов."

    def get_expense_report(self):
        report = ""
        for amount, description in self.expenses:
            report += f"{description}: {amount}\n"
        return report if report else "Нет расходов."