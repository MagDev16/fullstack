class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Precio: {self.price} - Cantidad: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product)

    def calculate_total_value_of_inventory(self):
        return sum(product.price * product.quantity for product in self.products)


def main():
    product1 = Product("Mouse", 5000, 3)
    product2 = Product("Teclado", 8000, 2)

    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)

    inventory.show_products()
    print(inventory.calculate_total_value_of_inventory())  # 31000


if __name__ == "__main__":
    main()
