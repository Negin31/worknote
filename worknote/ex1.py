def split_and_reverse(string):
    length = (len(string) // 2) - 1
    a, b = string[length::-1], string[:length:-1]
    return a + b


print(split_and_reverse('privet'))
