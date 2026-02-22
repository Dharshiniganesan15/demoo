# Function Documentation


None
---

## calculate_discount

**Signature:** `def calculate_discount(price: float, discount_percent: float)`

**Summary:** Calculate discount amount on price.

```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discount amount on price."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price * (discount_percent / 100)
```

---
