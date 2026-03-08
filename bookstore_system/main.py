"""
BIT1323 Integrated System Technology
Bookstore Simulation – Main Runner
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from modules.inventory_module import show_inventory
from modules.sales_module import process_order

def main():
    print("\n" + "=" * 50)
    print(f"{'📚 BOOKSTORE INTEGRATED SYSTEM':^50}")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Place an order")
        print("  2. View current inventory")
        print("  3. Exit")
        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            isbn    = input("Enter ISBN         : ").strip()
            qty_str = input("Enter Quantity     : ").strip()
            email   = input("Enter Email        : ").strip()

            try:
                qty = int(qty_str)
            except ValueError:
                print("❌ Quantity must be a number.")
                continue

            result = process_order(isbn, qty, email)
            print(result)

        elif choice == "2":
            show_inventory()

        elif choice == "3":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()