def fractional_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    result = 0.0

    # Calculate value/weight ratio and sort items
    items = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)

    for weight, value in items:
        if capacity == 0:
            break
        # If weight can be fully part of the knapsack
        if weight <= capacity:
            result += value
            capacity -= weight
        else:
            # Take fraction of the item
            result += value * (capacity / weight)
            capacity = 0

    print("Maximum value in knapsack =", result)

if __name__ == "__main__":
    fractional_knapsack()
