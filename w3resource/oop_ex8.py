class Cart:

    def __init__(self, cart) -> None:
        self.cart: dict[str, list[int]] = cart

    def add_product(self, product: str, qty: int, price: float) -> None:
        if qty < 0 or price < 0:
            raise ValueError("Количество товаров и цена не может быть меньше или равно нулю!")
        self.cart[product] = [qty, price]

    def del_product(self, product: str) -> None:
        if self.cart.get(product)[0] == 0:
            raise ValueError("Данного товара в корзине нет!")
        self.cart[product][0] -= 1
        if self.cart[product][0] == 0:
            del self.cart[product]

    def total(self) -> float:
        total = 0
        product_qty = 0
        for k, v in self.cart.items():
            total += v[0] * v[1]
            product_qty += v[0]
        return f"Товаров в корзине {product_qty}, на общую сумму {total}"


my_cart = Cart({"tablet": [20, 500]})
print(my_cart.cart)
my_cart.add_product("phone", 1, 1000)
print(my_cart.cart)
print(my_cart.total())

my_cart.del_product("tablet")
my_cart.del_product("tablet")
print(my_cart.cart)
print(my_cart.total())
