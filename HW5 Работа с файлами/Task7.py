"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением
убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}] """

import json

with open("task7.txt", 'r', encoding="utf-8") as f:
    company_profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3])
                      for line in f.readlines()}
    f.seek(0)
    profit_list = [int(line.split()[2]) - int(line.split()[3]) for line in f.readlines()
                   if int(line.split()[2]) - int(line.split()[3]) > 0]
    average_profit = {"average_profit": round(sum(profit_list) / len(profit_list))}

profit = [company_profit, average_profit]
js_profit = json.dumps(profit, ensure_ascii=False, indent=4)

with open("task7.json", 'w', encoding="utf-8") as f:
    f.write(js_profit)
