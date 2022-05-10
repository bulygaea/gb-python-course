import re

with open("task6.txt", 'r', encoding="utf-8") as f:
    subjects = {line.split()[0][:-1]: sum([int(i) for i in re.findall(r'\d*\.\d+|\d+', line)])
                for line in f.readlines()}
print(subjects)
