"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь
введённых чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу. """


def input_string():
    """Reading a line from the console. Return a string before the completion symbol and a label about the presence
    of the completion symbol in the string."""
    input_line = input().split(".")
    return (input_line[0], False) if len(input_line) < 2 else (input_line[0], True)


def summer(nums):
    r"""Summing numbers from a string to the global variable summary.
        :param nums: a string of numbers separated by a space
        :type nums: str"""
    global summary
    summary += sum(map(int, nums.split()))


summary = 0
while True:
    line = input_string()
    summer(line[0])
    print(summary)
    if line[1]:
        break
