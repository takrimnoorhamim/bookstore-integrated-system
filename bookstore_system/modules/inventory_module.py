import json
import os

LOW_STOCK_THRESHOLD = 5
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'inventory.json')

def load_inventory():
    """Load the inventory dictionary from the JSON database file."""
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def save_inventory(inventory):
    """Save the updated inventory dictionary back to the JSON database file."""
    with open(DB_PATH, 'w') as f:
        json.dump(inventory, f, indent=4)

def receive_order(json_string):
    """
    Inventory Function:
    - Receives a JSON string from the Sales module.
    - Parses it back into a Python object using json.loads().
    - Subtracts the sold quantity from the database.
    - Triggers a Low Stock Alert if stock falls to 5 or below.
    - Returns a JSON string result back to the caller.
    """
    # ── Step 1: JSON string → Python dict (API simulation: json.loads)
    order = json.loads(json_string)
    isbn     = order["isbn"]
    quantity = order["quantity"]

    # ── Step 2: Load current inventory from database
    inventory = load_inventory()

    # ── Step 3: Subtract quantity
    inventory[isbn]["stock"] -= quantity
    book_title = inventory[isbn]["title"]
    remaining  = inventory[isbn]["stock"]

    # ── Step 4: Save updated inventory
    save_inventory(inventory)

    # ── Step 5: Low stock alert
    alert = None
    if remaining <= LOW_STOCK_THRESHOLD:
        alert = (
            f"⚠️  LOW STOCK ALERT: '{book_title}' has only {remaining} copies left! "
            f"Please reorder soon."
        )
        print(alert)

    # ── Step 6: Build result and return as JSON string
    result = {
        "status": "success",
        "isbn": isbn,
        "title": book_title,
        "quantity_sold": quantity,
        "remaining_stock": remaining,
        "low_stock_alert": alert
    }
    return json.dumps(result, indent=2)   # json.dumps() → Python dict to JSON string

def show_inventory():
    """Print current inventory status in a readable format."""
    inventory = load_inventory()
    print("\n" + "=" * 68)
    print(f"{'📚 CURRENT INVENTORY STATUS':^68}")
    print("=" * 68)
    print(f"{'ISBN':<10} {'Title':<25} {'Unit Price (RM)':>16} {'Stock':>8}")
    print("-" * 68)
    for isbn, details in inventory.items():
        stock_display = f"{details['stock']}"
        if details["stock"] <= LOW_STOCK_THRESHOLD:
            stock_display += " ⚠️"
        print(f"{isbn:<10} {details['title']:<25} {details['price']:>14.2f} {stock_display:>8}")
    print("=" * 68 + "\n")