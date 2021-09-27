shopping_items = {"eggs": 1.85, "bread": 1.50, "peppers": 0.90}
shopping_items1 = {"eggs": 2.50, "bread": 1.35, "peppers": 1.20}

def calculate_total_basket_cost(shopping_list):
    total = 0

    for item in shopping_list.values():
        total += item
    return total

print(calculate_total_basket_cost(shopping_items))
print(calculate_total_basket_cost(shopping_items1))
