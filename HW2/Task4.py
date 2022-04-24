users_string = list(input().split())
print(*[f"{i+1} {word[:10]}" for i, word in enumerate(users_string)], sep="\n")
