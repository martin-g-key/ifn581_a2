import os

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
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    ## getters and setters:
    # product_id
    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product):
        ## dependency of input validation ...
        if product[:2] not in self.categoryCodes:
            product = "OT"+product[2:]
        self.__product_id = product

    # category is read only --> no setter needed. 
    @property 
    def category_name_of_product(self):
        if self.__product_id == None: 
            return None
        else: 
            for i, code in enumerate(self.categoryCodes): 
                if code == self.__product_id[:2]:
                    return self.categoryNames[i]

    # print attributes as as string
    def __str__(self):
        string = f"product_id: {self.product_id} |"
        string += f" category_name_of_product: {self.category_name_of_product} |"
        string += f" product_name: {self.product_name} |"
        string += f" quantity: {self.quantity} |"
        string += f" price: {self.price}"
        return string

def main():
    
    def display_introduction(): 
        string = "------------------------------------\n"
        string += "Name: Martin Keylock\n"
        string += "StudentID: n12882933\n"
        string += "Hello, welcome to assignment 2.\n"
        string += "------------------------------------"
        print(string)    


    def input_value(min=1, max=50):
        # data validation for input
        while True: 
            first = input(f"\nHow many products would you like to add?\nPlease provide an integer between {min} and {max}: ")
            try: 
                num = int(first) 
            except ValueError:
                print(f"{first} is not an integer. Please try again.")
                continue
            if min <= num <= max:
                print(f"{num} has been selected.")
                return num
            print(f"{num} is outside the range. Please try again.")


    def is_valid(product_id):
        if len(product_id) == 5 and product_id[:2].isupper() and product_id[:2].isalpha() and product_id[2:].isdigit() :
            return True


    def get_product_data(num_products, min=1, max=50):
        product_list = []

        print("\nPlease fill out the following product details for each product that you want to add:")

        # assumption that num_products will always be nu (output of input_value())
        for i in range(num_products):
            product = input("Product ID: ")

            # input validation
            while not is_valid(product):
                print("\nPlease fill out the following product details for each product that you want to add:")
                product = input("Product ID: ")

            # product_name is a string --> no input validation applied
            product_name = input("Product Name: ")

            # input validation for quantity as it's integer with a range
            while True:
                quantity = int(input(f"Quantity (integer between {min} and {max}): "))

                if min <= quantity <=max:
                    print(f"{quantity} is a valid input")
                    break 

            # input validation for price as its float with a range
            while True:
                # rounding to 2 decimal points as well 
                price = round(float(input("Price (decimal number): ")),2) 

                if 0 <= price: 
                    print(f"{price} is a valid input")
                    break

            # instantiate Product object and append to list  
            product_list.append(Product(product, product_name, quantity, price))
            print("Product added\n")

        return product_list


    def display_all_products(product_list):
        print("All products:")
        for product in product_list: 
            print(product.__str__())


    def get_product_lists(product_list):
        # get the generic codes list from class object
        code_list = Product.categoryCodes

        print("\nFilter product data from product list process:")

        # input validation and ! control
        while True: 
            user_input = input("What category would you like to filter for? (note: enter '!' to exit): ").strip().upper()

            # exists the loop
            if user_input == "!":
                print("Ending filtering step")
                break

            # check the code is in the list
            if user_input not in code_list:
                print(f"{user_input} is not a valid code. please choose from {code_list}")
                continue

            # total is based on category counter
            category_counter = 0
            for product in product_list:
                if product.product_id[:2] == user_input:
                    # simple output as a string
                    print(product.__str__())
                    category_counter +=1 
            print(f"Total of {category_counter} products in {user_input}.\n")


    def save_products_to_file(products_list, filename="Martin_Keylock_n12882933.txt", delimiter=","):
        # begin writing 
        print("\nSave products to file process:")
        with open(filename, "w", encoding="utf-8") as f:
            print(f"{filename} opened.")
            # header row
            f.write("product_id, product_name, category_name_of_product, price, quantity\n")
            # body rows
            for p in products_list: 
                row = [p.product_id, p.product_name, p.category_name_of_product, f"{float(p.price):.2f}", str(p.quantity)]
                f.write(",".join(row) + "\n")
                print("Row written to file.")
        f.close()


    def load_products_from_file(filename="Martin_Keylock_n12882933.txt"):
        product_list = []
        print("\nLoading products from file process:")
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip().split(",")

                # variable assingment for Product
                p = Product(line_list[0], line_list[2], line_list[3], line_list[4])

                # append product to product_list output
                product_list.append(p)

        f.close()
        return product_list

   
    display_introduction()
    output_list = get_product_data(input_value())
    display_all_products(output_list)
    get_product_lists(output_list)
    save_products_to_file(output_list)
    loaded_list = load_products_from_file()
    display_all_products(loaded_list)


if __name__ == "__main__":
    main()
