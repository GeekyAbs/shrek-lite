import argparse
import json
import os

CATEGORIES = [
    "Food",
    "Travel",
    "Rent",
    "Utilities",
    "Entertainment",
    "Health",
    "Shopping",
    "Other",
]
DATA_FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return data


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def _format_amount(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def cmd_add(amount):
    print("Select a category:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("Invalid choice, try again.")
    expenses = load_expenses()
    expenses.append({"expense": amount, "category": category})
    save_expenses(expenses)
    print(f"Added {_format_amount(amount)} to {category}.")


def cmd_total():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = sum(e["expense"] for e in expenses)
    by_cat = {}
    for e in expenses:
        by_cat[e["category"]] = by_cat.get(e["category"], 0) + e["expense"]
    print(f"Total: {_format_amount(total)}")
    print("By category:")
    for cat, amt in by_cat.items():
        print(f"  {cat}: {_format_amount(amt)}")


def main():
    parser = argparse.ArgumentParser(prog="shrek")
    sub = parser.add_subparsers(dest="command", required=True)
    add_p = sub.add_parser("add", help="Add an expense")
    add_p.add_argument("amount", type=float, help="Expense amount")
    sub.add_parser("total", help="Show total expenses")
    args = parser.parse_args()
    if args.command == "add":
        cmd_add(args.amount)
    elif args.command == "total":
        cmd_total()


if __name__ == "__main__":
    main()
