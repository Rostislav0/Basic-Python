class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def find(x):
    d = []
    letter = 0
    while letter < len(x):
        num = letter + 1
        while num < len(x) and x[num].isdigit():
            num += 1
        d.append(x[letter] * int(x[letter + 1:num]))
        letter = num
    return d


with open("8.0.txt", "r") as text:
    line1 = text.readline().strip()
    line2 = text.readline().strip()
    line3 = text.readline().strip()

print(color.BOLD + color.PURPLE + '1 line: ' + color.END, end='')
print(color.BOLD + color.GREEN, *find(line1), sep='')

print(color.BOLD + color.PURPLE + '2 line: ' + color.END, end='')
print(color.BOLD + color.GREEN, *find(line2), sep='')

print(color.BOLD + color.PURPLE + '3 line: ' + color.END, end= '')
print(color.BOLD + color.GREEN, *find(line3), sep='')
