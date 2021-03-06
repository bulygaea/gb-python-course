"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (
зима, весна, лето, осень). Напишите решения через list и dict. """

seasons = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11],
}
number_of_month = int(input("Type the number of the month: "))

f = lambda key, value: key if number_of_month in value else ""
print(*[f(key, value) for key, value in seasons.items()], sep="")

# or

for season, list_of_months in seasons.items():
    if number_of_month in list_of_months:
        print(season)
        break
