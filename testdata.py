product1 = Product("GR01", "Test1", "GR__", 1, 10.00)
product2 = Product("HB02", "Test2", "HB__", 5, 20.00)
product3 = Product("ZZ03", "Test3", "ZZ__", 10, 30.00)

p_list = []
p_list.append(product1)
p_list.append(product2)
p_list.append(product3)


for i in p_list: 
    print(i.__str__())
