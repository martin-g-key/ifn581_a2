import Product

product1 = Product("GR001", "Test1", "GR__", 1, 10.00)
product2 = Product("HB002", "Test2", "HB__", 5, 20.00)
product3 = Product("ZZ003", "Test3", "ZZ__", 10, 30.00)

p_list = []
p_list.append(product1)
p_list.append(product2)
p_list.append(product3)


for i in p_list: 
    print(i.__str__())
