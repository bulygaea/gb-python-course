rating = [7, 5, 3, 3, 2]

result = int(input("Type new result: "))
for i in range(len(rating)):
    if result > rating[i]:
        result, rating[i] = rating[i], result
rating.append(result)

print(*rating)
