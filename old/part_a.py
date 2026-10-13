"""
part_a.py
define Product class
"""
    

class Product():
    # class variables
    categoryCodes = ["GR", "HB", "CF", "EL", "HL", "OT"]
    categoryNames = ["Groceries", "Health & Beauty", "Clothing & Footwear", "Electronics", "Home & Living", "Others"]
    
    def __init__(
            self, 
            product_id = None, 
            product_name = "", 
            quantity = 0, 
            price = 0.0
            ):
        self.__product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        
    # print object attributes as string
    def __str__(self):
        string = f"product_id: {self.product_id} |"
        string += f" category_name_of_product: {self.category_name_of_product} |"
        string += f" product_name: {self.product_name} |"
        string += f" quantity: {self.quantity} |"
        string += f" price: {self.price}"
        return string

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product):
        self.product_id = product

    @property
    def category(self):
        self.category = f"{self.product_id}_CAT"
        return self.category

def main():
    p1 = Product("GR001", "Test1", 1, 10.00)
    print(p1.product_id)
    print(p1.category)


if __name__ == "__main__":
    main()