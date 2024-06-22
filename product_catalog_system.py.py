class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

  # Display product info
    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

class Book(Product):

    def __init__(self, product_id, name, author, price):
        super().__init__(product_id,name,price) #what's been inherited from Product class
        self.author = author
    
    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Name: {self.author}")
        print(f"Price: {self.price}")

class Electronic(Product):

    def __init__(self, product_id, name, specs, price):
        super().__init__(product_id,name,price)#what's been inherited from Product class
        self.specs = specs
    
    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Name: {self.specs}")
        print(f"Price: {self.price}")


class Clothing(Product):

    def __init__(self, product_id, name, size, price):
        super().__init__(product_id,name,price)#what's been inherited from Product class
        self.size = size

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Name: {self.size}")
        print(f"Price: {self.price}")

my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()
electronic1 = Electronic(123456789,"Lenovo", "1 TB Hardrive","$1000")
clothing1 = Clothing(456456,"Zara", "M","$40")
clothing1.display_info()
