x = int(input())
max_digit = 0

while x > 0:
    max_digit = x % 10 if x % 10 > max_digit else max_digit
    x //= 10

print(max_digit)
