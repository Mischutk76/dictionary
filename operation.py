from direct import dictionary


while True:
    word = input('Введите слово: ')
    if word not in dictionary:
        if word == '':
            break
        translete = []
        x = input('Введите перевод: ')
        while x != '':
            if x not in translete:
                translete.append (x)
            else:
                print("Этот перевод у слова уже есть")
            x = input('Введите перевод: ')
        dictionary[word] = translete
    else:
        print('Данное слово вы уже изучаете')
        x = input('Введите перевод: ')
        while x != '':
            translete = dictionary[word]
            if x not in translete:
                translete.append (x)
            else:
                print("Этот перевод у слова уже есть")
            x = input('Введите перевод: ')
        dictionary = translete