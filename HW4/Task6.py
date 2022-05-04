from itertools import count, cycle

for i in count(int(input())):
    print(i)
    if i > 10:
        break

k = 0
for i in cycle(['a', 'b', 'c', 'd']):
    print(i)
    k += 1
    if k > 10:
        break
