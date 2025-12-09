# Discount Calculator
bill = float(input("Enter the total bill amount: $"))
discount_percent = float(input("Enter the discount percentage (e.g., 10 for 10%): "))

if bill < 0 or discount_percent < 0 or discount_percent > 100:
    print("Please enter valid amounts and a discount percentage between 0 and 100.")
else:
    discount_amount = (bill * discount_percent) / 100
    output = bill - discount_amount
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"After discount your net bill is: ${output:.2f}")

