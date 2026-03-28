# Smart Budgeter - Phase 2 (Enhanced Logic & Validation)
# Project for VITyarthi BYOP

def main():
    expenses = []
    # Set a monthly budget limit
    try:
        limit_input = input("Enter your monthly budget limit (default is 2000): ")
        budget_limit = float(limit_input) if limit_input else 2000.0
    except ValueError:
        print("Invalid input. Using default limit of 2000.")
        budget_limit = 2000.0
    
    print(f"\n--- Welcome to Smart Budgeter (Goal: {budget_limit}) ---")
    
    while True:
        print("\n--- MENU ---")
        print("1. Add Expense")
        print("2. View Summary & Budget Status")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ")
        
        if choice == '1':
            item = input("What did you buy? ")
            
            # Step 4: Adding "Try-Except" for robust error handling
            try:
                amount = float(input(f"How much did '{item}' cost? "))
                category = input("Category (e.g., Food, Travel, Rent): ").capitalize()
                
                expenses.append({
                    "item": item, 
                    "amount": amount, 
                    "category": category
                })
                print(f"✅ Success: Added {item} to {category}!")
                
            except ValueError:
                print("❌ Error: Please enter a numeric value for the price (e.g., 50.50).")
                
        elif choice == '2':
            if not expenses:
                print("\nNo expenses recorded yet.")
                continue
                
            total = sum(e['amount'] for e in expenses)
            print(f"\n--- EXPENSE SUMMARY ---")
            for e in expenses:
                print(f"- {e['item']} ({e['category']}): {e['amount']}")
            
            print(f"\nTOTAL SPENT: {total}")
            
            # Step 4: Budget Calculation Logic
            if total > budget_limit:
                over_by = total - budget_limit
                print(f"⚠️ ALERT: You are OVER budget by {over_by}!")
            else:
                remaining = budget_limit - total
                print(f"💰 You have {remaining} remaining in your budget.")
                
        elif choice == '3':
            print("Saving session... Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()