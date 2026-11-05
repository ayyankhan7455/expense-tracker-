#A simple expense tracker project.

import csv
from pathlib import Path


FILE_NAME = Path(__file__).parent / "expenses.csv"




def add_expense(expenses, date, category, amount, note):
    """Check the details and add an expense to the list."""
    date = date.strip()
    category = category.strip()
    note = note.strip()


    if date == "" or category == "":
        raise ValueError("Date and category are required.")


    try:
        amount = float(amount)
    except (ValueError, TypeError):
        raise ValueError("Please enter a valid amount.") from None


    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")


    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note,
    }
    expenses.append(expense)




def calculate_total(expenses):
    #Calculate the total money spended.
    total = 0


    for expense in expenses:
        total += float(expense["amount"])


    return total




def show_expenses(expenses):
    #Print all expenses added.
    if len(expenses) == 0:
        print("No expenses have been added yet.")
        return


    for number, expense in enumerate(expenses, start=1):
        date = expense['date']
        category = expense['category']
        amount = float(expense['amount'])
        note = expense['note']
        print(f"{number}. {date} - {category} - Rs. {amount:.2f} - {note}")



def load_expenses():
    #Read old expenses from the CSV file if it exists.
    expenses = []


    if not FILE_NAME.exists():
        return expenses


    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)


        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)


    return expenses




def save_expenses(expenses):
    """Save expenses in a CSV file."""
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)




def main():
    #Show the menu and run the program.
    try:
        expenses = load_expenses()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Could not load expenses: {error}")
        return


    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Save and exit")


        choice = input("Choose an option: ").strip()


        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount in Rs.: ")
            note = input("Enter a note: ")


            try:
                add_expense(expenses, date, category, amount, note)
                print("Expense added.")
            except ValueError as error:
                print(f"Error: {error}")


        elif choice == "2":
            show_expenses(expenses)


        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total spending: Rs. {total:.2f}")


        elif choice == "4":
            try:
                save_expenses(expenses)
                print("Expenses saved. Goodbye!")
            except OSError as error:
                print(f"Could not save expenses: {error}")
            break


        else:
            print("Please choose 1, 2, 3, or 4.")




if __name__ == "__main__":
    main()
