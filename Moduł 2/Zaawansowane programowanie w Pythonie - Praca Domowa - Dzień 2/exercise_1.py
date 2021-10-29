class Product:
    next_id = 1
    def __init__(self, name, price):
        self.id = self.next_id
        Product.next_id += 1
        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        self.products[product.id] = product
        if product.id in self.quantities:
            self.quantities[product.id] += 1
        else:
            self.quantities[product.id] = 1

    def remove_product(self, product):
        if product.id in self.products and product.id in self.quantities:
            self.products.pop(product.id)
            self.quantities.pop(product.id)

    def change_product_quantity(self, product, new_quantity):
        if product.id in self.products and product.id in self.quantities:
            if new_quantity < 0:
                raise ValueError('Parametr new_quantity nie może być ujemny.')
            elif new_quantity == 0:
                self.products.pop(product.id)
                self.quantities.pop(product.id)
            else:
                self.quantities[product.id] = new_quantity

    def get_receipt(self):
        result = ''
        suma = 0
        for key in self.products:
            if self.quantities[key] >= 3:
                result += f'{self.products[key].name} - ilość: {self.quantities[key]}, cena: {self.products[key].price} zł, suma: {self.products[key].price * self.quantities[key] * 0.7} zł \n'
                suma += self.products[key].price * self.quantities[key] * 0.7
            else:
                result += f'{self.products[key].name} - ilość: {self.quantities[key]}, cena: {self.products[key].price} zł, suma: {self.products[key].price * self.quantities[key]} zł \n'
                suma += self.products[key].price * self.quantities[key]
        sum_string = f'\nSuma: {suma} zł'
        result += sum_string
        return result
            
    



a = Product('Worek ziarna', 200)
b = Product('Woda', 100)
d = Product('Konewka', 300)
c = ShoppingCart()
c.add_product(a)
c.add_product(a)
c.add_product(a)
c.add_product(b)

print(c.get_receipt())

