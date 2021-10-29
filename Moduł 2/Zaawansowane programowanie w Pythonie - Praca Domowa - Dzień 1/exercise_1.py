class Product:
    next_id = 1
    def __init__(self, name, description, price, quantity):
        
        self.id = self.next_id
        Product.next_id += 1
        if isinstance(name, str) == True:
            self.name = name
        else:
            raise ValueError("Name must be a string.")
        if isinstance(description, str) == True:
            self.description = description
        else:
            raise ValueError("Description must be a string.")
        if isinstance(price, float) == True and price > 0.01:
            self.price = price
        else:
            raise ValueError("Description must be a float larger than 0.01.")
        if isinstance(quantity, int) == True and quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Quantity must be an int larger than 0.")
        

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
            self._id = id

    def get_total_sum(self):
        return self.quantity * self.price

a = Product("Cookies", "Tasty cookies.", 10.0, 5)
#b = Product("Cola", "Tasty cola.", 2.0, 10)
#c = Product("Chips", "Tasty chips.", 100.0, 20)

print(a.next_id)
#print(b._id)
#print(c._id)
        
        
