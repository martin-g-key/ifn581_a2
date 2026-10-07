# IFN581 Assignment 2

## Quickstart

### Github Version Control

Working on a feature branch

```
git branch <jira key><branch>
git checkout <jira key><branch>
git status
git add .
git status
git commit -m "message” 
```

Merging code into main

```
git branch <jira key><branch>
git checkout <jira key><branch>
git add .
git commit -m "<jira key> message"
git push origin <jira key><branch>

git checkout main
git pull origin main
```

## Requirements

Due: 16 October

Specifiction: https://canvas.qut.edu.au/courses/24582/pages/ifn581-assessment-2-project-programming-assignment?module_item_id=2273841

Part A: Product Class
    
1. category code and name lists 
2. instance attributes
    * private attribute: product_ID accessed by get_product_id(), set product_id()
    * read only attribute: category_name_of_product 
    * public attribute: product_name, string
    * public attribute: quantity, integer
    * public attribute: prices, float
3. Product ID validation
    <category ID><number>
    * getter / setter logic
    * use 1st two characters from product_id and look up category name -- don't save category code as attribute
    * if code exists, assign the corresponding category_name_of product
    * if does not exists, assign "OT" as category_code
4. Constructor method    
5. string representation method

Part B: Functions within a main program
1. display_introduction()
2. input_value(min, max)
3. is_valid(product_id)
4. get_product_data(n) --> 1 to 50 items
5. display_all_products(products) --> use __str__ method
6. get_product_lists(products) --> filter by category code

Part C: File operations 
1. save_products_to_file(filename, products) --> csv file format
2. load_products_from_file(filename)
3. main()
    