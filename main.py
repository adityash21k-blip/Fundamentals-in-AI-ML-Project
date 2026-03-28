import json  # Library to save/load data from a file



def load_data():

    """Load expenses from a JSON file when the program starts."""
    try:
        with open("expenses_data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):

        # If file doesn't exist or is empty, start with an empty list
        return []

def save_data(expenses):

    """Save the current list of expenses to a JSON file."""

    with open("expenses_data.json", "w") as file:

        json.dump(expenses, file, indent=4)

    print("✅ Data saved successfully to 'expenses_data.json'.")


def main():
    expenses = load_data()  # Load previous data at startup

    budget_limit = 2000     # Monthly budget goal

    
    print("\n" + "="*30)
    print("💰 SMART BUDGETER v3.0 (Final)")

    print("="*30)
    
    while True:
        print("\n--- MAIN MENU ---")

        print("1. Add New Expense")

        print("2. View Summary & History")
        

        print("3. Exit & Save")

        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            item = input("Item name: ")
            try:
                amount = float(input(f"Cost of {item}: "))

                category = input("Category (Food/Travel/Bills): ").capitalize()

                expenses.append({
                    "item": item, 

                    "amount": amount, 

                    "category": category

                })
                print(f"Added {item}!")
            except ValueError:
                print("❌ Error: Invalid price. Use numbers only.")

                
        elif choice == '2':

            if not expenses:
                print("\nNo expenses found. Start by adding one!")

                continue
                
            total = sum(e['amount'] for e in expenses)

            print(f"\n--- EXPENSE HISTORY ---")
            for i, e in enumerate(expenses, 1):

                print(f"{i}. {e['item']} [{e['category']}] - ${e['amount']}")

            
            print(f"\nTOTAL SPENT: ${total}")

            print(f"BUDGET STATUS: {'⚠️ OVER BUDGET' if total > budget_limit else '✅ WITHIN BUDGET'}")

                
        elif choice == '3':
            save_data(expenses)  # CRITICAL: Save data before quitting

            print("Goodbye!")

            break

        else:

            print("Invalid choice. Try again.")


if __name__ == "__main__":

    main()