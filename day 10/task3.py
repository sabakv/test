x = int(input("enter X:"))
y = int(input("enter Y: "))
z = int(input("enter Z:"))


def comparision_of_nums(x, y, z):
    if x > y and x > z:
        return "x მეტია y-ზე " + str(x/y) + " ჯერ" + " ხოლო, x მეტია z -ზე " + str(x/z) + " ჯერ"
    elif y > x and y > z:
        return "y მეტია x -ზე " + str(y/x) + " ჯერ" + " ხოლო, y მეტია z -ზე " + str(y/z) + " ჯერ"
    elif z > y and z > x:
        return "z მეტია y -ზე " + str(z/y) + " ჯერ" + " ხოლო, z მეტია x -ზე " + str(z/x) + " ჯერ"


print(comparision_of_nums(x, y, z))
