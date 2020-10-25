print()
print("Fill in the blanks of this code to print out the numbers 1 through 7.")
print()
number = 1
while number < 8:
    print(number, end=" ")
    number = number + 1

print()
print("The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.")
print()


def show_letters(word):
    for i in word:
        print(i)


show_letters("Hello")
# Should print one line per letter

print()
print("Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.")
print()


def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n > 0):
        count += 1
        n = n // 10
    return count


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))    # Should print 1


print()
print("This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:")
print()


def multiplication_table(start, stop):
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

print()
print("This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:")
print()


def counter(start, stop):

    if start > stop:
        return_string = "Counting down: "
        while start >= stop:
            return_string += str(start)
            if start > stop:
                return_string += ","
            start = start - 1
    else:
        return_string = "Counting up: "
        while start <= stop:
            return_string += str(start)
            if start < stop:
                return_string += ","
            start = start + 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"

print()
print("The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.")
print()

def even_numbers(maximum):
	return_string = ""
	for x in range(2, maximum + 1, 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

for x in range(1, 10, 3):
    print(x)

for x in range(10):
    for y in range(x):
        print(y)

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

print(votes("yes", "no", "maybe"))