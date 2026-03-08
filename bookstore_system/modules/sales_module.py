import json
from utils.validator import validate_isbn, validate_quantity, validate_stock, validate_email
from modules.inventory_module import load_inventory, receive_order

def process_order(isbn, quantity, customer_email):
    """
    Sales Function:
    - Validates all inputs (ISBN, quantity, stock availability, email).
    - Masks the customer email for security before any logging/display.
    - Builds an order object and serialises it to a JSON string using json.dumps().
    - Sends that JSON string to the Inventory module's receive_order().
    - Parses the response JSON string back using json.loads().
    - Returns a formatted receipt string.
    """
    # ── Step 1: Load inventory for validation
    inventory = load_inventory()

    # ── Step 2: Validate ISBN
    ok, msg = validate_isbn(isbn, inventory)
    if not ok:
        return msg

    # ── Step 3: Validate quantity (type check)
    ok, msg = validate_quantity(quantity)
    if not ok:
        return msg

    # ── Step 4: Validate stock availability
    ok, msg = validate_stock(isbn, quantity, inventory)
    if not ok:
        return msg

    # ── Step 5: Validate email (Security Point – protect PII)
    ok, msg = validate_email(customer_email)
    if not ok:
        return msg

    # ── Step 6: Mask email for any display/logging (e.g. alice@mail.com → a***@mail.com)
    masked_email = _mask_email(customer_email)

    # ── Step 7: Build order payload and convert to JSON string (json.dumps)
    book  = inventory[isbn]
    order = {
        "isbn":           isbn,
        "quantity":       quantity,
        "customer_email": masked_email      # never store raw email in transit
    }
    order_json_string = json.dumps(order)   # Python dict → JSON string

    print(f"\n📤 Sales Module sending order to Inventory Module...")
    print(f"   JSON Payload: {order_json_string}")

    # ── Step 8: Send JSON string to Inventory module (module-to-module communication)
    response_json_string = receive_order(order_json_string)

    # ── Step 9: Parse response (json.loads)
    response = json.loads(response_json_string)

    # ── Step 10: Generate and return receipt
    total_price = book["price"] * quantity
    receipt = _generate_receipt(isbn, book, quantity, total_price, masked_email, response)
    return receipt

def _mask_email(email):
    """Security helper: mask email so raw PII is never exposed in logs."""
    local, domain = email.split("@")
    return local[0] + "***@" + domain

def _generate_receipt(isbn, book, quantity, total_price, masked_email, inv_response):
    """Build a readable receipt string."""
    lines = [
        "\n" + "=" * 50,
        f"{'🧾  PURCHASE RECEIPT':^50}",
        "=" * 50,
        f"  Book Title  : {book['title']}",
        f"  Author      : {book['author']}",
        f"  ISBN        : {isbn}",
        f"  Quantity    : {quantity}",
        f"  Unit Price  : RM {book['price']:.2f}",
        f"  Total Price : RM {total_price:.2f}",
        f"  Customer    : {masked_email}",
        "-" * 50,
        f"  Status      : ✅ Order Successful",
        f"  Remaining   : {inv_response['remaining_stock']} copies left in stock",
        "=" * 50,
    ]
    return "\n".join(lines)