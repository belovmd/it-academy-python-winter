country_num = int(input())
catalog1 = {}
for i in range(country_num):
    list1 = [el for el in input().split()]
    catalog = {a: list1[0] for a in list1[1::]}
    catalog1.update(catalog)

num_req = int(input())
list_request = []

for i in range(num_req):
    list2.append(input())
for element in list_request:
    print(catalog1.get(element))
