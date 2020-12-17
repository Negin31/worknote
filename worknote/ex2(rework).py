def check(ex):
    check_list = []

    for i in ex:
        if i == '(':
            check_list.append(1)
        elif i == ')':
            try:
                if check_list.pop() != 1:
                    print('неправильно')
                    return False
            except IndexError:
                print('неправильно')
                return False
        elif i == '[':
            check_list.append(2)
        elif i == ']':
            try:
                if check_list.pop() != 1:
                    print('неправильно')
                    return False
            except IndexError:
                print('неправильно')
        elif i == '{':
            check_list.append(3)
        elif i == '}':
            try:
                if check_list.pop() != 1:
                    print('неправильно')
                    return False
            except IndexError:
                print('неправильно')

    print('правильно')
    return True



print(check('({ some food)}'))
print(check(input('Введите строчку для проверки: ')))