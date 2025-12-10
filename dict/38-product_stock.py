# Update product stock in inventory system.

inventory = {
    "P001": {"name": "Laptop", "quantity": 100, "price": 500.00},
    "P002": {"name": "Mobile", "quantity": 110, "price": 450.00},
    "P003": {"name": "Desktop", "quantity": 120, "price": 500.00}
}

def update_stock(product_id, new_quantity):
    if product_id in inventory:
        # Update the quantity directly
        inventory[product_id]["quantity"] = new_quantity
        print(f"Updated '{inventory[product_id]['name']}' stock to {new_quantity}.")
    else:
        print(f"Product ID {product_id} not found in inventory.")

def add_stock(product_id, amount_to_add):
    if product_id in inventory:
        inventory[product_id]["quantity"] += amount_to_add
        print(f"Added {amount_to_add} units to '{inventory[product_id]['name']}'. New stock: {inventory[product_id]['quantity']}.")
    else:
        print(f"Product ID {product_id} not found in inventory.")

def remove_stock(product_id, amount_to_remove):
    if product_id in inventory:
        if inventory[product_id]["quantity"] >= amount_to_remove:
            inventory[product_id]["quantity"] -= amount_to_remove
            print(f"Removed {amount_to_remove} units from '{inventory[product_id]['name']}'. New stock: {inventory[product_id]['quantity']}.")
        else:
            print(f"Insufficient stock for '{inventory[product_id]['name']}'. Current stock: {inventory[product_id]['quantity']}.")
    else:
        print(f"Product ID {product_id} not found in inventory.")

# Demonstrate usage
print("Initial Inventory:")
print(inventory)

print("\n--- Updating stock ---")
# Example 1: Set a new quantity
update_stock("P001", 150)
# Example 2: Add to existing quantity
add_stock("P002", 20)
# Example 3: Remove from existing quantity
remove_stock("P003", 50)
# Example 4: Attempt to update a non-existent product
update_stock("P004", 50)

print("\nFinal Inventory:")
print(inventory)
