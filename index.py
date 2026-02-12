#E-Commerce Shopping System

print("****** E-Commerce Shopping System ************")

# Product catalog with prices
products = {
    "Jacket": 900,
    "T-Shirt": 300,
    "Shoes": 700,
    "Jeans": 600,
    "Shirt": 500,
    "Cap": 400,
    "Socks": 100
}

customer_count = 1
while customer_count <= 3:
    print(f"\n============= Customer {customer_count} =============")
    
    # Input
    name = input("Your Full Name: ")
    budget = eval(input("Your Budget (Rs): "))
    
    original_budget = budget
    cart = []
    total_spent = 0
    
    # Shopping items available
    print(f"\nDear {name}, Available Items:")
    print("-" * 40)
    for item, price in products.items():
        print(f"{item}: Rs. {price}")
    print("-" * 40)
    
    # Shopping loop - customer selects items
    shopping = True
    while shopping:
        purchase = input("\nEnter item name to buy (or 'done' to exit): ").strip().capitalize()
        
        if purchase.lower() == 'done':
            shopping = False
        elif purchase in products:
            price = products[purchase]
            if budget >= price:
                cart.append((purchase, price))
                budget -= price
                total_spent += price
                print(f"✓ {purchase} added to cart! Remaining budget: Rs. {budget}")
            else:
                print(f"✗ Insufficient budget! Need Rs. {price}, you have Rs. {budget}")
        else:
            print("✗ Item not found! Please enter a valid item name.")
    
    # Calculate discount based on total spent
    if total_spent >= 2000:
        discount_percent = 20
        special = "VIP Customer! Get 20% discount on next purchase"
    elif total_spent >= 1500:
        discount_percent = 15
        special = "Premium Customer! Get 15% discount on next purchase"
    elif total_spent >= 1000:
        discount_percent = 10
        special = "Regular Customer! Get 10% discount on next purchase"
    elif total_spent >= 500:
        discount_percent = 5
        special = "Thank you for shopping! Get 5% discount on next purchase"
    else:
        discount_percent = 0
        special = "Thank you! Visit us again"
    
    # Calculate bill
    discount_amount = (total_spent * discount_percent) / 100
    final_amount = total_spent - discount_amount
    
    # Display receipt
    print(f"\n{'='*50}")
    print(f"RECEIPT FOR {name.upper()}")
    print(f"{'='*50}\n")
    
    if cart:
        print("Items Purchased:")
        for item, price in cart:
            print(f"  • {item}: Rs. {price}")
        print(f"\nSubtotal: Rs. {total_spent}")
        print(f"Discount ({discount_percent}%): Rs. {discount_amount:.2f}")
        print(f"Final Amount: Rs. {final_amount:.2f}")
    else:
        print("No items purchased!")
    
    print(f"\nRemaining Budget: Rs. {budget}")
    print(f"\nCustomer Status: {special}")
    print(f"{'='*50}\n")
    
    customer_count += 1
    print("-----------------------------------\n")
    