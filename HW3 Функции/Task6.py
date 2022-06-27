"""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. """


def int_func(word):
    r"""Increases the first letter of word.

        :param word: lowercase word
        :type word: str

        :return: a word with a capital first letter
        :rtype: str"""
    return chr(ord(word[0]) - ord("a") + ord("A")) + word[1:]


print(int_func(input("Type an English word: ")))
