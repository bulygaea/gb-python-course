class ListValueError(ValueError):
    def __str__(self):
        return 'The value isn\'t the number'


my_list = []
while True:
    try:
        a = input('Type the number: ')
        if not a.replace('-', '').isdigit():
            raise ListValueError
        my_list.append(int(a))
    except ListValueError as err:
        print(err)
    except BaseException:
        print(f'\n{" ".join(map(str, my_list))}')
        break
    else:
        print('The numer is added')
