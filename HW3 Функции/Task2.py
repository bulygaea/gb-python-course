"""2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой. """


def user_bio(name="undefined", surname="undefined", birthday=None, city="undefined", email="undefined",
             phone="undefined"):
    birthday = ["undefined"] if birthday is None else birthday[:]
    return f"Name: {name}\n" \
           f"Surname: {surname}\n" \
           f"Birthday: {'-'.join(birthday)}\n" \
           f"City: {city}\n" \
           f"Email: {email}\n" \
           f"Phone: {phone}"


print(user_bio(name=input("Type your name: "),
               surname=input("Type your surname: "),
               birthday=input("Type date of your birthday via the space: ").split(),
               city=input("Type your city name: "),
               email=input("Type your email: "),
               phone=input("Type your phone: ")))
