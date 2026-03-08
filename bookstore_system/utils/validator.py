import re

def validate_isbn(isbn, inventory):
    """Check if the ISBN exists in the inventory database."""
    if not isbn or not isinstance(isbn, str):
        return False, "Error: ISBN must be a non-empty string."
    if isbn not in inventory:
        return False, f"Error: Book with ISBN '{isbn}' does not exist in inventory."
    return True, "ISBN is valid."

def validate_quantity(quantity):
    """Check if the quantity is a positive integer."""
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        return False, "Error: Quantity must be a whole number (integer)."
    if quantity <= 0:
        return False, "Error: Quantity must be greater than zero."
    return True, "Quantity is valid."

def validate_stock(isbn, quantity, inventory):
    """Check if there is enough stock to fulfill the order."""
    available = inventory[isbn]["stock"]
    if quantity > available:
        return False, (
            f"Error: Insufficient Stock. "
            f"Requested {quantity}, but only {available} available for '{inventory[isbn]['title']}'."
        )
    return True, "Stock is sufficient."

def validate_email(email):
    """Basic check that the email looks valid before storing/using it."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not email or not re.match(pattern, email):
        return False, "Error: Invalid email address format."
    return True, "Email is valid."