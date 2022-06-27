"""1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и
строки и сохраните в переменные, затем выведите на экран. """

name = input("Type your name: ")
age = int(input("Type your age: "))
print(f"Hello, {name}! Your age is {age}.\n"
      f"And I'm {'younger than' if age > 20 else 'older than' if age < 20 else 'the same age as'} you!")
