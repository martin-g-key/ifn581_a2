 #p1 = Product()
    #print(p1.product_id, p1.category_name_of_product)
    p1 = Product("GR001", "Test1", 1, 10.00)
    print(p1.product_id, p1.category_name_of_product)
    p1.product_id = "HB001" 
    print(p1.product_id, p1.category_name_of_product)
    p1.product_id = "ZZ001" 
    print(p1.product_id, p1.category_name_of_product)
    print(p1.__str__())

