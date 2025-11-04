import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.columns = ["Date", "Category", "Type", "Amount"]
        self.data = self.load_data()

    def load_data(self):
        """Load existing CSV data if available, else create new DataFrame."""
        if os.path.exists(self.filename):
            try:
                return pd.read_csv(self.filename)
            except Exception as e:
                print("Error reading file:", e)
        return pd.DataFrame(columns=self.columns)

    def save_data(self):
        """Save data to CSV file."""
        self.data.to_csv(self.filename, index=False)
        print("✅ Data saved successfully!")

    def add_transaction(self, category, t_type, amount):
        """Add a new income or expense."""
        date = datetime.now().strftime("%Y-%m-%d")
        new_entry = pd.DataFrame([[date, category, t_type, amount]], columns=self.columns)
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        print("✅ Transaction added!")

    def show_summary(self):
        """Show total income, expense, and balance."""
        if self.data.empty:
            print("No data available yet.")
            return
        income = self.data[self.data["Type"] == "Income"]["Amount"].sum()
        expense = self.data[self.data["Type"] == "Expense"]["Amount"].sum()
        balance = income - expense
        print(f"\n💰 Total Income: {income}")
        print(f"💸 Total Expense: {expense}")
        print(f"🧾 Balance: {balance}")

    def analyze_expenses(self):
        """Generate insights with Pandas."""
        if self.data.empty:
            print("No data to analyze.")
            return

        df = self.data.copy()
        df["Date"] = pd.to_datetime(df["Date"])
        df["Month"] = df["Date"].dt.to_period("M")

        # Monthly expense totals
        monthly_expense = df[df["Type"] == "Expense"].groupby("Month")["Amount"].sum()
        print("\n📆 Monthly Expense Totals:")
        print(monthly_expense)

        # Highest spending category
        category_expense = df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum()
        if not category_expense.empty:
            top_category = category_expense.idxmax()
            print(f"\n🔥 Highest Spending Category: {top_category} ({category_expense[top_category]})")
        else:
            print("\nNo expense data found.")

        # Visualization
        self.plot_charts(category_expense, monthly_expense)

    def plot_charts(self, category_expense, monthly_expense):
        """Generate bar and line charts."""
        if not category_expense.empty:
            plt.figure(figsize=(7,4))
            category_expense.plot(kind="bar")
            plt.title("Category-wise Expenses")
            plt.xlabel("Category")
            plt.ylabel("Amount")
            plt.tight_layout()
            plt.show()

        if not monthly_expense.empty:
            plt.figure(figsize=(7,4))
            monthly_expense.plot(kind="line", marker='o')
            plt.title("Monthly Expense Trend")
            plt.xlabel("Month")
            plt.ylabel("Total Expense")
            plt.tight_layout()
            plt.show()


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1️⃣ Add Income")
        print("2️⃣ Add Expense")
        print("3️⃣ Show Summary")
        print("4️⃣ Analyze & Visualize")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            tracker.add_transaction(category, "Income", amount)

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_transaction(category, "Expense", amount)

        elif choice == "3":
            tracker.show_summary()

        elif choice == "4":
            tracker.analyze_expenses()

        elif choice == "5":
            tracker.save_data()
            print("👋 Exiting... Have a great day!")
            break

        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()