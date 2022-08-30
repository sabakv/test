#ჰკითხეთ მომხმარებელს სახელი და ეკრანზე გამოიტანეთ შეტყობინება, 
#"გამარჯობა, saxeli"

#გააკეთეთ format ფუნქციით

# user_name = input("whats your name: ")

# print("greetings {}".format(user_name))




#მომხმარებელს ორჯერ შემოატანინეთ რიცხვი 
#შეკრიბეთ ეს ორი რიცხვი და გამოიტანეთ ეკრანზე.
#num1 + num2 = sum_of_nums <- ასეთი სტრინგი უნდა გამოვიდეს ეკრანზე
 
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

# sum_of_nums = num1 + num2 

# print("{} + {} = {}".format(num1, num2, sum_of_nums))






# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))
# num4 = int(input("enter num4: "))

# sum_of_nums = (num1num1 + num2 num2 + \
#     num3num3 + num4 num4) / (num1+num2+num3+num4)


# print("{} * {} + {} * {} + {} * {} + {} * {} = {} / {} + {} + {} + {}".format(num1, num1, num2, num2, num3, num3, num4, num4, 
# num1, num2, num3, num4, sum_of_nums))








# მომხმარებელს შემოაქვს ორი ცვლადი  1) რამდენნაჭრიანი პიცაა 2) რამდენი ნაჭერი შეჭამა

# გამოიტანეთ წინადადების სახით, xნაჭრიან პიცაში შეიჭამა yნაჭერი და დარჩა zნაჭერი.


# pizza_size = int(input("How many slices does pizza have:"))
# slices_eaten = int(input("How many slices of pizza did you eat:"))
# slices_left = int(pizza_size-slices_eaten)

# print("{}ნაჭრიან პიცაში {}ნაჭერი შეიჭამა დარჩა{}ნაჭერი".format(
#     pizza_size, slices_eaten, slices_left))






Host_in_restaurants = int(input("Enter How many people are in the restaurant? "))
money_spent = int(input("Enter How much money did they spend? ") )


print("ერთ ადამიანს მოუწევს " + str(money_spent/Host_in_restaurants) + "გადახდა")