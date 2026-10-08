p_list =  ["HB111", "GR111", "XX111"]


categoryCodes = ["GR", "HB", "CF", "EL", "HL", "OT"]
categoryNames = ["Groceries", "Health & Beauty", "Clothing & Footwear", "Electronics", "Home & Living", "Others"]

def checker(product_id):
    code = product_id[:2]
    i = categoryCodes.index(code) if code in categoryCodes else -1

    catCodeOut = categoryCodes[i]
    catNameOut = categoryNames[i]
    product_id = categoryCodes[i] + product_id[2:]

    print(catCodeOut, catNameOut, product_id)

for i in p_list:
    checker(i)
