a = ['string', 1, 1.0, True, [1, 2, 3], {"name": "Ekaterina"}, (5, 6, 7), {8, 9, 10}]
print(*[f"{i}: {type(i)}" for i in a], sep="\n")
