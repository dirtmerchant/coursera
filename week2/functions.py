def greet(name):
    print("Welcome, " + name)


def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds * 1)


print_seconds(1, 2, 3)


def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")


def month_days(month, days):
    result = f"{month} has {days} days."
    return (result)

print(month_days("June", 30))
print(month_days("July", 31))

def rectangle_area(base,height):
    area = base * height
    return area

print("The area is ", str(rectangle_area(5,6)))