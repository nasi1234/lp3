class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def fractionalKnapsack(W, arr):
    # Sorting based on profit/weight ratio
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    finalvalue = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue


# ----------- USER INPUT SECTION -----------
if __name__ == "__main__":
    # Take knapsack capacity from user
    W = float(input("Enter total capacity of Knapsack: "))

    # Take number of items
    n = int(input("Enter number of items: "))

    arr = []  # Empty list for items

    # Take profit and weight for each item
    for i in range(n):
        print(f"\nEnter details of item {i+1}:")
        profit = float(input("Profit: "))
        weight = float(input("Weight: "))
        arr.append(Item(profit, weight))

    # Call function
    max_val = fractionalKnapsack(W, arr)

    print("\nMaximum total profit in Knapsack =", max_val)
