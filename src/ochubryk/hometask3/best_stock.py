# You are given the current stock prices.
# You have to find out which stocks cost more.


def best_stock(a):
    max_value = max(a.values())
    key = [key for key, value in a.items() if value == max_value]
    return key[0]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
