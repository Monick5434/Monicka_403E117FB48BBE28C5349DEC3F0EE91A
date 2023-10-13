def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Test the function with a sample product list and target product
products = ['Apple', 'Banana', 'Apple', 'Orange', 'Apple']
target_product = 'Apple'

result = linear_search_product(products, target_product)

# Print the result
print(f"Indices of '{target_product}': {result}")
