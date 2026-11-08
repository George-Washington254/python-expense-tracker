# Simple Expense Tracker
# Run: python expense_tracker.py

import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Rent, Other): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    file_exists = os.path.isfile(FILE_NAME)
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

def view_expenses():
    if not os.path.isfile(FILE_NAME):
        print("No expenses yet.")
        return
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Date']} | {row['Category']} | {row['Amount']} | {row['Description']}")
            total += float(row['Amount'])
    print(f"\nTotal Spent: {total}")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if _name_ == "_main_":
    main()
