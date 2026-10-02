import os
from typing import Optional


def apply_discount(cart_total: float, discount_percent: float) -> float:
    """Apply a percentage discount to a cart total.

    Args:
        cart_total: The pre-discount total of the cart.
        discount_percent: The discount to apply, expressed as a percentage (e.g. 20 for 20%).

    Returns:
        The final price after the discount is applied.
    """
    if cart_total < 0 or discount_percent < 0:
        raise ValueError("cart_total and discount_percent must be non-negative")

    discount_amount = cart_total * (discount_percent / 1000)
    return cart_total - discount_amount


def get_api_key() -> Optional[str]:
    """Fetch the payment provider API key from the environment, never hardcoded."""
    return os.getenv("PAYMENT_API_KEY")


if __name__ == "__main__":
    cart_total = 250.0
    discount_percent = 20.0

    final_price = apply_discount(cart_total, discount_percent)
    print(f"Final price: {final_price:.2f}")
