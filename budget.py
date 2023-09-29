import csv
import os

# Create a CSV file to store data if it doesn't exist
DATA_FILE = 'budget_data.csv'

def create_data_file_if_not_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Category', 'Amount'])

def get_budget_data():
    with open(DATA_FILE, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_budget_data(data):
    with open(DATA_FILE, 'w', newline='') as file:
        fieldnames = ['Type', 'Category', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_transaction(transaction_type, category, amount):
    budget_data = get_budget_data()
    budget_data.append({'Type': transaction_type, 'Category': category, 'Amount': amount})
    save_budget_data(budget_data)

def calculate_balance():
    budget_data = get_budget_data()
    income = sum(float(item['Amount']) for item in budget_data if item['Type'] == 'Income')
    expenses = sum(float(item['Amount']) for item in budget_data if item['Type'] == 'Expense')
    return income - expenses

def analyze_expenses():
    budget_data = get_budget_data()
    expense_categories = {}
    
    for item in budget_data:
        if item['Type'] == 'Expense':
            category = item['Category']
            amount = float(item['Amount'])
            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount
    
    print("\nExpense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount:.2f}")

def main():
    create_data_file_if_not_exists()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Balance")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            add_transaction('Income', category, amount)
            print("Income added successfully!")
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_transaction('Expense', category, amount)
            print("Expense added successfully!")
        elif choice == '3':
            balance = calculate_balance()
            print(f"Current Balance: ${balance:.2f}")
        elif choice == '4':
            analyze_expenses()
        elif choice == '5':
            print("Exiting Budget Tracker by Santhose. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
