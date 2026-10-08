from part_a import Product #, set_product_id

product1 = Product("GR001", "Test1", "GR__", 1, 10.00)
product2 = Product("HB002", "Test2", "HB__", 5, 20.00)
product3 = Product("ZZ003", "Test3", "ZZ__", 10, 30.00)

p_list = []
p_list.append(product1)
p_list.append(product2)
p_list.append(product3)

def main(): 
    def display_introduction(): 
        string = "------------------------------------\n"
        string += "Name: Martin Keylock\n"
        string += "StudentID: n12882933\n"
        string += "Hello, welcome to assignment 2.\n"
        string += "------------------------------------\n"
        print(string)

    def input_value(min=1, max=50):
        ## TO DO: Input validation based on a range?
        num = int(input(f"Please provide an integer between {min} and {max}: "))
        print(f"Thank you. You have selected {num}")
        return num

    def is_valid(product_id):
        if len(product_id) == 5 and product_id[:2].isupper() and product_id[2:].isdigit() :
            return True 

    def get_product_data(num_products):
        for i in range(num_products):
            product_id = input("Product ID: ")

            while not is_valid(product_id):
                print("Please provide a product_id in a valid format.")
                product_id = input("Product ID: ")

            category_name_of_product = input("category_name_of_product: ")
            product_name = input("Product Name: ")
            quantity = input("Quantity: ")
            price = input("Price: ")
                    
            p_list.append(Product(product_id, category_name_of_product, product_name, quantity, price))

    def display_all_products(product_list):
        for i in product_list: 
            print(i.__str__())

    def get_product_lists(product_list):
        pass
        """
        for i in product_list:
            if i.code
        """


    display_introduction()
    get_product_data(input_value())
    display_all_products(p_list)


if __name__ == "__main__":
    main()
