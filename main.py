# Smart Budgeter - Phase 1 (Core Logic)
# Project for VITyarthi BYOP

def main():
    expenses = []
    budget_limit = 2000  # You can change this limit
    
    print("--- Welcome to Smart Budgeter ---")
    
    while True:
        print("\n1. Add Expense")
        print("2. View Total Spending")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            item = input("What did you buy? ")
            try:
                amount = float(input(f"How much did '{item}' cost? "))
                expenses.append({"item": item, "amount": amount})
                print(f"Successfully added {item}!")
            except ValueError:
                print("Error: Please enter a valid number for the price.")
                
        elif choice == '2':
            total = sum(e['amount'] for e in expenses)
            print(f"\nYour current total spending is: {total}")
            
            if total > budget_limit:
                print("⚠️ WARNING: You have exceeded your budget limit!")
            else:
                remaining = budget_limit - total
                print(f"You have {remaining} left in your budget.")
                
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
