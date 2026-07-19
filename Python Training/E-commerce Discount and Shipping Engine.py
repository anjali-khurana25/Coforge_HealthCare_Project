cart_value = float(input("Enter cart value: ₹"))
customer_type = input("Enter customer type (Regular/VIP): ")
coupon = input("Enter coupon code: ")
membership = input("Enter membership status (Premium/Normal): ").lower()

if membership == "premium":
    shipping = 0
else:
    shipping = 100

if cart_value > 5000:
    discount = cart_value * 0.20
elif cart_value > 2000:
    discount = cart_value * 0.10
else:
    discount = 0

if coupon == "SAVE100":
    coupon_discount = 100
elif coupon == "SAVE200":
    coupon_discount = 200
else:
    coupon_discount = 0

final_amount = cart_value - discount - coupon_discount + shipping

if final_amount < 0:
    final_amount = 0

print("Cart Value: ₹", cart_value)
print("Discount: ₹", discount)
print("Coupon Discount: ₹", coupon_discount)
print("Shipping Charges: ₹", shipping)
print("Final Payable Amount: ₹", final_amount)