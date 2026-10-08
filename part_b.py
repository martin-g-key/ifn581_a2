


def main(): 
    from part_a import Product 
    import os

    def seed_data(): 
        product1 = Product("GR001", "Test1", "GR__", 1, 10.00)
        product2 = Product("HB002", "Test2", "HB__", 5, 20.00)
        product3 = Product("ZZ003", "Test3", "ZZ__", 10, 30.00)

        products_list = []
        products_list.append(product1)
        products_list.append(product2)
        products_list.append(product3)


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
        print(f"Thank you. You have selected {num}\n")
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
                    
            products_list.append(Product(product_id, category_name_of_product, product_name, quantity, price))

    def display_all_products(product_list):
        print("\n All products:")
        for i in product_list: 
            print(i.__str__())
        print("\n")

    def get_product_lists(product_list, category_code):
        # present all products by category
        # repeatedly search until enter "!" to stop
        pass

    def save_products_to_file(filename, products_list, delimiter=","):
        # explicitly delete exising file
        if os.path.exists(filename):
            os.remove(filename)

        # begin writing 
        with open(filename, "w", encoding="utf-8") as f:
            print(f"{filename} opened.")
            # header row
            f.write("product_id, product_name, category_name_of_product, price, quantity\n")
            # body rows
            for p in products_list: 
                row = [p.product_id, p.product_name, p.category_name_of_product, f"{float(p.price):.2f}", str(p.quantity)]
                f.write(",".join(row) + "\n")
                print("Row written to file.")
        print("\n")
                
    def load_products_from_file(filename, products):
        pass


    display_introduction()

    #get_product_data(input_value())
    #display_all_products(products_list)
    #save_products_to_file('Martin_Keylock_Products.txt', products_list)
    # get_product_lists()
    #load_products_from_file('Martin_Keylock_Products.txt', products_list)
    # display_all_products()

if __name__ == "__main__":
    main()
