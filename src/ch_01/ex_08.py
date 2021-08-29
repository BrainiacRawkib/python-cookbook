prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_key = min(prices, key=lambda k: prices[k])
min_value = prices[min(prices, key=lambda k: prices[k])]

if __name__ == '__main__':
    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)
    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))
    # print(max(prices_and_names))
    print(min_key)
    print(min_value)
