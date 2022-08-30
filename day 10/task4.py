
def more(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.sort(reverse = True)
    return "{n1} is more than {n2} {a} times and {n1} is more than {n3} {b} times".format(n1 = num_list[0], n2 = num_list[1], n3 = num_list[2], a = num_list[0]/num_list[1], b = num_list[0]/num_list[2])

more(1,2,5)
