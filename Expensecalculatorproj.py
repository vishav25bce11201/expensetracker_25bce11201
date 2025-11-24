import csv
import os
from datetime import datetime

DATA_FILE = "expenses.csv"

# CREATING A NEW FILE

def setup_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "amount", "category", "note"])

def read_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    data = []
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data

#EXPENSES CATEGORY

def write_expenses(expenses):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "amount", "category", "note"])
        writer.writeheader()
        writer.writerows(expenses)

#ADDING EXPENSE
        
def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    amount = input("Amount: ")
    category = input("Enter Category: Food/Travel/Shopping/Other ")
    note = input("Note: ")

    new_row = {
        "date": date,
        "amount": amount,
        "category": category,
        "note": note}

    expenses = read_expenses()
    expenses.append(new_row)
    write_expenses(expenses)

    print("Expense added.")

#SHOW EXPENSES
    
def show_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found")
        return

    print("Your Expenses:")
    for e in expenses:
       print(e["date"], "₹"+e["amount"], e["category"], e["note"])
    print()

#DELETE EXPENSES

def delete_expense():
    expenses = read_expenses()

    if not expenses:
        print("Nothing to delete")
        return

    show_expenses()
    index = input("Enter row number to delete (starting from 1): ")

    try:
        index = int(index) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            write_expenses(expenses)
            print(f"Deleted entry: {removed}\n")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number")

#SEARCHING
        
def search_by_category():
    category = input("Enter category: ").strip().lower()
    expenses = read_expenses()
    found = [e for e in expenses if e["category"].lower() == category]

    if not found:
        print("No matching records")
        return

    print("Results:")
    for e in found:
        print(e["date"], "₹"+e["amount"], e["category"], e["note"])
    print()

#SORTING
    
def sort_by_amount():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found")
        return

    expenses.sort(key=lambda x: float(x["amount"]))
    print("Sorted by Amount:")
    for e in expenses:
        print(e["date"], "₹"+e["amount"], e["category"], e["note"])
    print()


def monthly_report():
    month = input("Enter month number (01-12): ")

    expenses = read_expenses()
    filtered = [e for e in expenses if e["date"][5:7] == month]

    if not filtered:
        print("No data for this month")
        return

    total = sum(float(e["amount"]) for e in filtered)

    print("Total for month",month,":₹",total)

#DAILY AVERAGE
    
def daily_average():
    expenses = read_expenses()

    if not expenses:
        print("No expenses available")
        return

    totals = {}
    for e in expenses:
        d = e["date"]
        totals[d] = totals.get(d, 0) + float(e["amount"])

    avg = sum(totals.values()) / len(totals)
    print(f"\nDaily Average Spending: ₹{avg:.2f}\n")

#MENU PAGE

def menu():
    setup_file()

    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Search by Category")
        print("5. Sort by Amount")
        print("6. Monthly Report")
        print("7. Daily Average")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            search_by_category()
        elif choice == "5":
            sort_by_amount()
        elif choice == "6":
            monthly_report()
        elif choice == "7":
            daily_average()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
