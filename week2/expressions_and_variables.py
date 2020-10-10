base = 5
height = 3
area = ((base * height)/2)
print(area)

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is " + str(average))

bill = 47.28
tip = bill * 0.15
total = bill + tip
share = (total/2)
print("Each person needs to pay: " + str(total))

numerator = 10
denominator = 10
result = numerator / denominator
print(result)

numerator = 10
denominator = numerator
result = numerator / denominator
print(result)

#brute force
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"
print(word1 +" " + word2 +" " + word3 +" " + word4 +" " + word5 +" " + word6 +" " + word7)

#pythonic
list = ["How" , "do", "you", "like", "python", "so", "far?"]
for i in range(len(list)):
    print(list[i], end =" ")

#print("2 + 2 = " + (2 + 2))
print("2 + 2 = " + str((2 + 2)))

def greet(name):
    print("Welcome, " + name)