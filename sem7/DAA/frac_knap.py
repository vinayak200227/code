def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['value_to_weight'] = item['value'] / item['weight']

    # Sort the items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x['value_to_weight'], reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        if item['weight'] <= capacity:
            # Add the whole item to the knapsack
            knapsack.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            # Add a fraction of the item to the knapsack
            fraction = capacity / item['weight']
            knapsack.append({'item': item['item'], 'weight': capacity, 'value': fraction * item['value']})
            total_value += fraction * item['value']
            break

    return knapsack, total_value

if __name__ == "__main__":
    items = [
        {'item': 'A', 'weight': 10, 'value': 60},
        {'item': 'B', 'weight': 20, 'value': 100},
        {'item': 'C', 'weight': 30, 'value': 120}
    ]
    
    capacity = 50

    knapsack, total_value = fractional_knapsack(items, capacity)
    print("Items in the knapsack:")
    for item in knapsack:
        print(f"Item: {item['item']}, Weight: {item['weight']}, Value: {item['value']}")
    print(f"Total value in the knapsack: {total_value}")
