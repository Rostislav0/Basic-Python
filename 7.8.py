with open('7.8.txt', 'a+', encoding='utf-8') as file:
    print(file.read(2))  #кол-во символов

    file.seek(0)  #Позиция
    print(file.read())

    print(file.readline())

    file.seek(0)
    s = file.readlines()
    print(s)

    file.close()