with open("test.txt", "r") as txt2:
    txt = txt2.readline().strip()
letter = 0
while letter < len(txt):
    num = letter + 1
    while num < len(txt) and txt[num].isdigit():
        num += 1
    print(txt[letter] * int(txt[letter + 1:num]), end='')
    letter = num
