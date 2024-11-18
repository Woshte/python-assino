def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price


def example_runs():
    
    print("Example 1:")
    original_price = 1500
    discount_percent = 25
    final_price = calculate_discount(original_price, discount_percent)
    print(f"Original Price: ${original_price:.2f}, Discount: {discount_percent}%")
    print(f"The final price after applying the discount is: ${final_price:.2f}\n")
    
    
    print("Example 2:")
    original_price = 1000
    discount_percent = 15
    final_price = calculate_discount(original_price, discount_percent)
    print(f"Original Price: ${original_price:.2f}, Discount: {discount_percent}%")
    print(f"No discount applied. The price remains: ${final_price:.2f}\n")

    
    print("Example 3:")
    try:
        original_price = float("90.5")  
        discount_percent = 25
        final_price = calculate_discount(original_price, discount_percent)
        print(f"Original Price: ${original_price:.2f}, Discount: {discount_percent}%")
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the price and discount percentage.\n")


example_runs()
