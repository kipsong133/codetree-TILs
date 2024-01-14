class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def print_out(self):
        print(f"product {self.code} is {self.name}")

name, code = tuple(input().split())
new_product = Product(name, code)
default_product = Product("codetree", "50")

default_product.print_out()
new_product.print_out()