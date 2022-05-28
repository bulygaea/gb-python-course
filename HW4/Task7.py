def fact(a):
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
        yield factorial


n = int(input())
for i in fact(n):
    print(i)
