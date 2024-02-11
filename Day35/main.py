def your_vat():
    while True:
        try:
            # Get the price and VAT percentage from the user
            price = float(input("Enter the price of the item: "))
            vat_percentage = float(input("Enter the VAT percentage (e.g., 15 for 15%): "))

            # Check for negative inputs
            if price < 0 or vat_percentage < 0:
                raise ValueError("Price and VAT percentage must be non-negative.")

            # Calculate the VAT amount and the VAT-inclusive price
            vat_amount = (vat_percentage / 100) * price
            vat_inclusive_price = price + vat_amount

            return vat_inclusive_price

        except ValueError as e:
            print("Invalid input. Please enter valid non-negative numbers.")
            print(f"Error: {e}")

# Example usage:
final_price = your_vat()
print(f"The VAT-inclusive price is: {final_price:.2f}")
