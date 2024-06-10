class Product:
    def __init__(self, name, price, qty=0):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(qty, int) or qty < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.name = name
        self.price = price
        self.qty = qty
        self.description = ""

    def apply_discount(self, discount):
        if not isinstance(discount, (int, float)) or discount < 0 or discount > 100:
            raise ValueError("Discount must be a number between 0 and 100.")
        self.price -= self.price * (discount / 100)

    def update_description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if len(description) > 300:
            raise ValueError("Description must be 300 characters or less.")
        self.description = description

    def increase_qty(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        self.qty += amount

    def decrease_qty(self, amount):
        print(self.qty, amount)
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if self.qty < amount:
            raise ValueError("Amount is greater than the current quantity.")
        self.qty -= amount
