import random



def jeradebi_4isa(my_list):
    print(my_list)
    for element in my_list:
        if element % 4 == 0:
            print(element, "არის 4-ის ჯერადი")
    
    

my_list = []
for i in range(10):
    my_list.append(random.randint(1, 50))





jeradebi_4isa(my_list)