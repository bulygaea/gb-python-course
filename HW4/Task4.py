nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*[a for a in nums if nums.count(a) < 2])

# or


repeated_set = set()
unique_set = set()

for a in nums:
    if a in repeated_set:
        continue
    if a in unique_set:
        repeated_set.add(a)
        unique_set.remove(a)
        continue
    unique_set.add(a)

print(unique_set)
