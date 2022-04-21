name = input("Type your name: ")
age = int(input("Type your age: "))
print(f"Hello, {name}! Your age is {age}.\n"
      f"And I'm {'younger than' if age > 20 else 'older than' if age < 20 else 'the same age as'} you!")
