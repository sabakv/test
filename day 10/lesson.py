y = int(input("enter Y: "))
x = int(input("enter X: "))
def comparison(x, y):
    if x > y:
        return "x მეტია y ზე" + str(x-y) + "ით"
    elif y > x:
        return "x ნაკლებია y ზე" + str(y-x) + "ით"
print(comparison(x, y))