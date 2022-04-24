seasons = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11],
}
number_of_month = int(input("Type the result of the month: "))

f = lambda key, value: key if number_of_month in value else ""
print(*[f(key, value) for key, value in seasons.items()], sep="")
