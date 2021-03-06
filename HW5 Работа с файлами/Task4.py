"""4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Напишите
программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """

numbers = {'1': "one",
           '2': "two",
           '3': "three",
           '4': "four",
           '5': "five",
           '6': "six",
           '7': "seven",
           '8': "eight",
           '9': "nine",
           }
with open("task4.txt", 'r', encoding="utf-8") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        for key, value in numbers.items():
            line = line.replace(key, value)
        print(line)
