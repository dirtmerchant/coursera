number = 1
while number < 8:
	print(number, end=" ")
	number = number + 1


def show_letters(word):
	for i in word:
		print(i)

show_letters("Hello")
# Should print one line per letter