'''Create a function called my_discount. The function takes no
arguments but asks the user to input the price and the discount
(percentage) of the product.'''

def my_discount():
    # Ask the user to input the price and discount percentage
    price = float(input("Enter the price of the product: $"))
    discount_percentage = float(input("Enter the discount percentage (e.g., 15 for 15%): "))

    # Calculate the price after the discount
    discount_amount = (discount_percentage / 100) * price
    discounted_price = price - discount_amount

    return discounted_price

# Call the function and print the result
discounted_price = my_discount()
print(f"The price after discount is: ${discounted_price:.2f}")
