# i = 1
# for char in "nika  kesh":
    
#     print(i, char)
#     i += 1
    
    


my_str = "nika  kesh"
i = len(my_str)
# while i < len(my_str):
#     print(i+1, my_str[i])
#     i += 1

while i > 0:   #სანამ 10 მეტია 0-ზე   ( როდესაც 0 > 0 დაჯდება, აღარ გაგრძელდება ციკლი)
    print(my_str[i-1])     #დაიპრინტება my_str სტრინგის i - 1 ინდექსზე მყოფი სიმბოლო
    i -=1    #i შემცირდეს ერთით, ყოველ ციკლის ბრუნვაზე(იტერაციაზე) 




