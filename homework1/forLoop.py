from typing import List

friends: List[str] = ['john', 'pat', 'gary', 'michael']
name: str
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
