# def add(x, y):
#     return x + y

# add_lambda = lambda x, y: x + y

# print(f"Normal Function: {add(2, 3)}")
# print(f"Lambda Function: {add_lambda(2, 3)}")

# nums = [1, 2, 3, 4]

# squared_nums = list(map(lambda x: x**2, nums))

# print(squared_nums)

# nums = [1, 2, 3, 4, 5, 6]

# even_nums = list(filter(lambda x: x % 2 == 0, nums))

# print(even_nums)

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300},
]

sorted_products = sorted(products, key=lambda item: item["price"])

print(sorted_products)
