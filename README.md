***Expense Tracker – Python***

This is a simple command-line based Expense Tracker written in Python. It allows you to record, view, search, sort, and delete your daily expenses. All data is stored in a CSV file so it is easy to read and portable.

Features

1.Add Expense
You can add a new expense with the date, amount, category, and a note.

2.View All Expenses
Displays every expense saved in the CSV file.

3.Delete Expense
Lets you remove an entry by choosing its row number.

4.Search by Category
Shows all expenses that match a specific category.

5.Sort by Amount
Sorts all expenses from the lowest to highest amount spent.

6.Monthly Report
Calculates the total amount spent in a selected month.

7.Daily Average
Shows the average amount you spend per day based on your recorded entries.

**How it Works**

All data is stored inside a file named "expenses.csv".
If the file does not exist, the program creates it automatically with the correct table headers.
Each entry contains the following fields:

~date
~amount
~category
~note

*How to Run*

Save the code in a Python file, for example: expense_tracker.py

Open a terminal or command prompt

Run the program with:

python expense_tracker.py

You will then see a menu where you can choose different actions like adding or viewing expenses.

Project Structure

expense_tracker.py
expenses.csv (created automatically on first run)

Requirements

The program only uses built-in Python modules: csv and os
No installation of extra libraries is required.
