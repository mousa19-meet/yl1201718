#def numbers():
#	a = [2,4,5,6]
#	new_list = [a[0],a[-1]]
#	return new_list
#x = numbers()
#print(x)
#def print_numbers(user):
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	lists = []
#	for i in range(len(a)):
#		if i < user:
#			lists.append(i)
#	return lists
#x = print_numbers(10)
#print(x)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = {a[0,-1] + b[0,-1]}
print(c)
