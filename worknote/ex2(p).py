def check(ex):
    check_list = {'()': 0, '[]': 0, '{}': 0}

    for i in ex:
        if i == '(':
            check_list['()'] += 1
        elif i == ')':
            check_list['()'] -= 1
        elif i == '[':
            check_list['[]'] += 1
        elif i == ']':
            check_list['[]'] -= 1
        elif i == '{':
            check_list['{}'] += 1
        elif i == '}':
            check_list['{}'] -= 1

        if check_list['()'] < 0 or check_list['[]'] < 0 or check_list['{}'] < 0:
            print('неправильно')
            return False
    if check_list['()'] == 0 or check_list['[]'] == 0 or check_list['{}'] == 0:
        print('правильно')
        return True
    else:
        print('неправильно')
        return False


print(check('({ some food)}'))
print(check(input('Введите строчку для проверки: ')))
