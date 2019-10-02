def printBackwards(name, i):
	if i == -1:
		return
	print(name[i], end = '')
	printBackwards(name, i - 1)

name=input("Enter your name here")
back=input("Do you want your name printed backwards? y/n")
if back == "y":
	printBackwards(name, len(name) - 1)	
else:
	print("Thats ok", name)	
