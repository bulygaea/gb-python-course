def int_func(word):
    r"""Increases the first letter of word.

        :param word: lowercase word
        :type word: str

        :return: a word with a capital first letter
        :rtype: str"""
    return chr(ord(word[0]) - ord("a") + ord("A")) + word[1:]


def enlarger(line):
    r"""Increases the first letter of each word in the string.

        :param line: a string of words in lowercase
        :type line: str

        :return: a string of words with a capital first letter
        :rtype: str"""
    new_line = ""
    for word in line.split():
        new_line += int_func(word) + " "
    return new_line


input_line = input()
print(enlarger(input_line))
