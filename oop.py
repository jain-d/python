# The Product class represents items in our store
class Product:
    def __init__(self, id: str, name: str, price: float, stock: int):
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock
        self._reserved_stock = 0

    def reserve_stock(self, quantity: int) -> bool:
        if self._stock - self._reserved_stock >= quantity:
            self._reserved_stock += quantity
            return True
        return False

    def release_stock(self, quantity: int):
        self._reserved_stock = max(0, self._reserved_stock - quantity)

    def confirm_stock_reduction(self, quantity: int):
        if self._reserved_stock >= quantity:
            self._stock -= quantity
            self._reserved_stock -= quantity
            return True
        return False

    @property
    def available_stock(self) -> int:
        return self._stock - self._reserved_stock

# The ShoppingCart manages products being purchased
class ShoppingCart:
    def __init__(self):
        self._items = {}  # Dictionary of product_id to quantity
        self._product_catalog = None

    def set_product_catalog(self, catalog):
        self._product_catalog = catalog

    def add_item(self, product_id: str, quantity: int) -> bool:
        if not self._product_catalog:
            raise Exception("Product catalog not set")
            
        product = self._product_catalog.get_product(product_id)
        if not product:
            return False
            
        if product.reserve_stock(quantity):
            if product_id in self._items:
                self._items[product_id] += quantity
            else:
                self._items[product_id] = quantity
            return True
        return False

    def remove_item(self, product_id: str, quantity: int = None):
        if product_id not in self._items:
            return
            
        product = self._product_catalog.get_product(product_id)
        if quantity is None or quantity >= self._items[product_id]:
            quantity = self._items[product_id]
            del self._items[product_id]
        else:
            self._items[product_id] -= quantity
            
        product.release_stock(quantity)

    def get_total(self) -> float:
        total = 0.0
        for product_id, quantity in self._items.items():
            product = self._product_catalog.get_product(product_id)
            total += product._price * quantity
        return total

# The ProductCatalog manages our inventory of products
class ProductCatalog:
    def __init__(self):
        self._products = {}

    def add_product(self, product: Product):
        self._products[product._id] = product

    def get_product(self, product_id: str) -> Product:
        return self._products.get(product_id)

# The Order represents a completed purchase
class Order:
    def __init__(self, order_id: str, cart: ShoppingCart):
        self.order_id = order_id
        self._items = cart._items.copy()
        self._total = cart.get_total()
        self._status = "Pending"

    def confirm(self, product_catalog: ProductCatalog) -> bool:
        # Verify and reduce stock for all items
        for product_id, quantity in self._items.items():
            product = product_catalog.get_product(product_id)
            if not product.confirm_stock_reduction(quantity):
                return False
        self._status = "Confirmed"
        return True

# Usage Example
def main():
    # Create our product catalog
    catalog = ProductCatalog()
    
    # Add some products
    laptop = Product("1", "Laptop", 999.99, 5)
    phone = Product("2", "Phone", 599.99, 10)
    catalog.add_product(laptop)
    catalog.add_product(phone)
    
    # Create a shopping cart
    cart = ShoppingCart()
    cart.set_product_catalog(catalog)
    
    # Add items to cart
    cart.add_item("1", 2)  # 2 laptops
    cart.add_item("2", 1)  # 1 phone
    
    # Create and confirm order
    order = Order("ORD-001", cart)
    success = order.confirm(catalog)
    
    if success:
        print(f"Order {order.order_id} confirmed! Total: ${order._total}")
        print(f"Remaining laptop stock: {laptop.available_stock}")
        print(f"Remaining phone stock: {phone.available_stock}")
