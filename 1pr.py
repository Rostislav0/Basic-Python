b = []
print("Add a number('end' - to stop)\n>>")
a = input()
b.append(float(a))
while 1 > 0:
	a = input()	
	if a == 'end':
		break
	b.append(float(a))

while 1 > 0:
	print(b)


	d = int(input("Which one of>>"))
	print(b[d-1])

	print('Do you want to do?>>\n "/" -- for devited\n "*" -- for multiply \n "+" -- for add minus \n "-" -- for take away \n "info" -- for more info')
	inf = input()
	if inf == "/":
		kol = float(input("by>>"))
		newNum = b[d - 1] / kol
		print(newNum)
		if input("Add new num?(y/n)>>") == 'y':
			b.append(newNum)
		else:
			continue
	elif inf == '*':
		kol = float(input("by>>"))
		newNum = b[d - 1] * kol
		print(newNum)
		if input("Add new num?(y/n)>>") == 'y':
			b.append(newNum)
		else:
			continue
	elif inf == '+':
		kol = float(input("by>>"))
		newNum = (b[d - 1]) + kol
		print(newNum)
		if input("Add new num?(y/n)>>") == 'y':
			b.append(newNum)
		else:
			continue
	elif inf == '-':
		kol = float(input("by>>"))
		newNum = (b[d - 1]) - kol
		print(newNum)
		if input("Add new num?(y/n)>>") == 'y':
			b.append(newNum)
		else:
			continue
	elif inf == 'info':
		print(' "del" -- for delete num \n "add" -- for add new num \n "replace" -- f\
or replace num \n "clear" -- for clear')
		continue
	elif inf == 'del':
		#vop = input('"p" -- for delete by index \n "r" -- for delete by value\n>>')
		#if vop == 'p':
			#print(b)
			#vop1 = int(input("Enter index of num which you want delete\n>>"))2
			b.pop(d-1)
			#vop2 = input('"back" -- for back\n"con" -- for continue to delete\n>>')
			#if vop2 == 'back':
			#	continue
			#elif vop2 == 'con':
			continue
		#elif vop == 'r':
		#	print(b)
		#	vop1 = str(input("Enter value which you want delete\n>>"))
		#	b.remove(vop1)
		#	continue
	elif inf == 'add':
		b.append(float(input("Enter new num to add")))
		continue
	elif inf == 'replace':
		#rep = int(input("Enter index"))
		b[d-1] = float(input("New num"))
		continue
	elif inf == 'clear':
		b.clear()
		b.append(0)
		continue
	else:
		continue
