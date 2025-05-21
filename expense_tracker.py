# expense_tracker.py

import datetime

# List to store all expenses
expenses = []

# Function to add a new expense
def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, Bills): ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Enter description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded.\n")
        return
    
    print("\n--- All Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Date: {exp['date']}, Category: {exp['category']}, Amount: ${exp['amount']:.2f}, Description: {exp['description']}")
    print()

# Function to view total expenses by category
def total_by_category():
    if not expenses:
        print("\nNo expenses to summarize.\n")
        return

    category_totals = {}
    for exp in expenses:
        category_totals[exp['category']] = category_totals.get(exp['category'], 0) + exp['amount']
    
    print("\n--- Total by Category ---")
    for cat, total in category_totals.items():
        print(f"{cat}: ${total:.2f}")
    print()

# Function to delete an expense
def delete_expense():
    view_expenses()
    if not expenses:
        return

    try:
        entry_num = int(input("Enter the entry number to delete: "))
        if 1 <= entry_num <= len(expenses):
            deleted = expenses.pop(entry_num - 1)
            print(f"Deleted: {deleted['description']} (${deleted['amount']})")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main_menu():
    while True:
        print("========== Expense Tracker ==========")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the application
if __name__ == "__main__":
    main_menu()
