# You have a table with all available goods in the store.
# The data is represented as a list of dicts
# Your mission here is to find the TOP most expensive goods.
# The amount we are looking for will be given as a first
# argument and the whole data as the second one


def bigger_price(limit: int, data: list) -> list:
    def get_price(dictionary):
        return dictionary['price']

    data.sort(key=get_price, reverse=True)
    result = data[:limit]
    return result


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"
