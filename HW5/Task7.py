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
