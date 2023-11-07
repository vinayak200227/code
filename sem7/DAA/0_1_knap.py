def knapsack_01(items, capacity):
    n = len(items)
    # Initialize a table to store the maximum value for each combination of items and capacities
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                # Base case: no items or no capacity
                dp[i][w] = 0
            elif items[i - 1]['weight'] <= w:
                # If the current item can be included, choose the maximum between including it or excluding it
                dp[i][w] = max(items[i - 1]['value'] + dp[i - 1][w - items[i - 1]['weight']], dp[i - 1][w])
            else:
                # If the current item cannot be included, just take the value from the previous row
                dp[i][w] = dp[i - 1][w]

    # Determine the items included in the knapsack by backtracking through the table
    included_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            # If the value in the table changed, include the item and update the weight
            included_items.append(items[i - 1])
            w -= items[i - 1]['weight']
        i -= 1

    included_items.reverse()
    return dp[n][capacity], included_items

if __name__ == "__main__":
    items = [
        {'item': 'A', 'weight': 10, 'value': 60},
        {'item': 'B', 'weight': 20, 'value': 100},
        {'item': 'C', 'weight': 30, 'value': 120}
    ]
    
    capacity = 50

    max_value, included_items = knapsack_01(items, capacity)

    print("Maximum value:", max_value)
    print("Items included in the knapsack:")
    for item in included_items:
        print(f"Item: {item['item']} (Weight: {item['weight']}, Value: {item['value']})")
