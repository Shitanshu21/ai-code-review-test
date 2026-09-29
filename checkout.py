def apply_discount(cart_total, discount_percent):
    # Bug: dividing by 100 twice, so discount is applied incorrectly
    discount_amount = (cart_total * discount_percent / 100) / 100
    final_price = cart_total - discount_amount
    return final_price

api_key = "sk-live-4f9a2b8c1e7d3f6a9b0c5e2d8f1a4b7c"  # hardcoded secret, should never be committed

cart_total = 250
discount_percent = 25

final = apply_discount(cart_total, discount_percent)
print(f"Final price: {final}")
