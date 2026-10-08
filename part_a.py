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
            category_name_of_product = "",
            quantity = 0, 
            price = 0.0
            ):
        
        self.product_id = product_id
        self.product_name = product_name
        self.category_name_of_product = category_name_of_product
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




product1 = Product("GR01", "Test1", "GR__", 1, 10.00)
product2 = Product("HB02", "Test2", "HB__", 5, 20.00)
product3 = Product("ZZ03", "Test3", "ZZ__", 10, 30.00)

p_list = []
p_list.append(product1)
p_list.append(product2)
p_list.append(product3)


for i in p_list: 
    print(i.__str__())


# Q: should i save the product objects in a dict, or list of objects, or something? 
# Q: should i create another class at a high level that product to define methods acorss many objects 
# Q: can I use 

    # mutator methods 
        # include validation checks


    """
    def input_product():
        try:
            num = int("How many products do you want to add?")
            for i in range(num):   
                product_id = input("Product ID: ")
                category_name_of_product = input("category_name_of_product: ")
                product_name = input("Product Name: ")
                quantity = input("Quantity: ")
                price = input("Price: ")
                Product(product_id, category_name_of_product, product_name, quantity, price)
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
    """
