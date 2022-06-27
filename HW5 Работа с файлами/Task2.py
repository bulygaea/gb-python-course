"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в
каждой строке. """

from re import sub

with open("task2.txt", "r", encoding="utf-8") as f:
    lines = [i.replace('\n', '').lower() for i in f.readlines() if len(i) > 1]
    print(sum([len(sub(r'[^\w\s]', '', i).replace('  ', ' ').split(' ')) for i in lines]))
    print(len(lines))
