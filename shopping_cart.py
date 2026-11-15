products = {"Pen": 10, "Notebook": 50, "Bag": 500}

cart = {}

# ---------- 3. Fixed values (rules given in the problem) ----------
GST_RATE = 0.18          # 18% GST
DISCOUNT_RATE = 0.10     # 10% discount
DISCOUNT_LIMIT = 500     # discount only if subtotal is MORE than 500


# ---------- 4. Functions ----------

def show_products():
    """Show all products with their prices."""
    print("\n--- Available Products ---")
    for name in products:
        print(name, ": Rs.", products[name])


def check_product(name):
    """Return True if the product is in the catalogue, else False."""
    if name in products:
        return True
    else:
        # ", ".join(products) makes: Pen, Notebook, Bag
        print("Invalid product. Available:", ", ".join(products))
        return False


def check_quantity(text):
    """Check that quantity is a whole number and at least 1.
    Returns the quantity as a number, or None if it is invalid."""
    try:
        quantity = int(text)
    except ValueError:
        print("Quantity must be a number.")
        return None

    if quantity < 1:
        print("Quantity must be at least 1.")
        return None

    return quantity


def calculate_subtotal():
    """Add up price x quantity for every item in the cart."""
    subtotal = 0
    for name in cart:
        subtotal = subtotal + products[name] * cart[name]
    return subtotal


def add_to_cart():
    """Ask the user for a product and quantity, then add it to the cart."""
    name = input("Enter product name: ").strip().title()

    if not check_product(name):
        return

    quantity = check_quantity(input("Enter quantity: "))
    if quantity is None:
        return

    # If the item is already in the cart, increase its quantity
    if name in cart:
        cart[name] = cart[name] + quantity
    else:
        cart[name] = quantity

    print(name, "x" + str(quantity), "added | Cart subtotal:", calculate_subtotal())


def remove_from_cart():
    """Remove a product from the cart."""
    name = input("Enter product name to remove: ").strip().title()

    if name in cart:
        del cart[name]
        print(name, "removed.")
    else:
        print(name, "is not in your cart.")


def view_cart():
    """Show everything in the cart."""
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n--- Your Cart ---")
    for name in cart:
        total = products[name] * cart[name]
        print("Cart:", name, "x" + str(cart[name]), "=", total)
    print("Subtotal:", calculate_subtotal())


def checkout():
    """Calculate and print the final bill. Returns True if bill was made."""
    if len(cart) == 0:
        print("\nYour cart is empty. Add items before checkout.")
        return False

    subtotal = calculate_subtotal()

    # Discount: 10% only if subtotal is more than 500
    if subtotal > DISCOUNT_LIMIT:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0

    # GST is calculated on the amount after discount
    gst = (subtotal - discount) * GST_RATE

    grand_total = subtotal - discount + gst

    print("\n========== FINAL BILL ==========")
    for name in cart:
        print(name, "x" + str(cart[name]), "=", products[name] * cart[name])
    print("--------------------------------")
    print("Subtotal:", round(subtotal, 2), "| Discount:", round(discount, 2),
          "| GST:", round(gst, 2))
    print("Grand Total:", round(grand_total, 2))
    print("================================")
    print("Thank you for shopping!")
    return True


def show_menu():
    print("\n===== SHOPPING CART MENU =====")
    print("1. View products")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")


# ---------- 5.The Main program ----------

def main():
    print("Welcome to the Shopping Cart System!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            if checkout():
                break          # stop the program after the bill is printed.
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# This line runs main() when we run the file
main()