class BudgetCategory():
    def __init__(self, category, budget):
        self.__category = category
        self.__initial_budget = budget
        self.__budget = budget
        self.__total_expenses = 0

     # Getter for budget
    def get_budget(self):
        return self.__budget

    # Getter for category
    def get_category(self):
        return self.__category

    # Setter for budget
    def set_budget(self, budget):
        if budget > 0:
            self.__budget = budget
        else:
            print("Try again. A budget must be a positive number.")
        

    # Setter for category
    def set_category(self, category):
        self.__category = category

   # Method to add an expense to the category and adjust the budget accordingly

    def add_expense(self, amount):
        if amount <= 0:
            print('Unable to add expense. Expense must be greater than $0')
        else:
            self.__total_expenses += amount
            self.__budget -= amount

    #Dispaly category summary
    def display_category_summary(self):
        print(f"Category: {self.__category} , Budget: {self.__initial_budget}")
        print(f"Total Expenses: {self.__total_expenses}, Revised Budget: {self.__budget}")


# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
