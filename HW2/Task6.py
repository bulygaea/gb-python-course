n = int(input("How many positions do you want to add? "))
list_of_items = []
for i in range(n):
    item = {"название": input("Type the name of item: "),
            "цена": int(input("Type the price: ")),
            "количество": int(input("Type the number of items: ")),
            "ед.": input("Type the units of measurement of the item: "),
            }
    list_of_items.append((i + 1, item))

info_of_items = {"название": [i[1]["название"] for i in list_of_items],
                 "цена": [i[1]["цена"] for i in list_of_items],
                 "количество": [i[1]["количество"] for i in list_of_items],
                 "ед.": [i[1]["ед."] for i in list_of_items],
                 }

print(*list_of_items, sep="\n")
print(*[f"'{key}': {value}" for key, value in info_of_items.items()], sep="\n")
