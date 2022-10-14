text = []
with open("8.1.txt", "r") as lines:
    for line in lines:
        text.extend(line.strip().lower().split())
text.sort()
n = 0
j = 1
col = 0
word = ''
while j < len(text):
    while text[n] == text[j]:
        n += 1
        j += 1
        if j == len(text):
            break
    if text.count(text[n]) > col:
        col = text.count(text[n])
        word = text[n]
    n += 1
    j += 1
print(word, col)
