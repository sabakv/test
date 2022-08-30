# passwords_dict = {
#     "nika"
# }

# passwords = ["memiyvarsdediko123", "aguri", "paroliparoli", "memiyvarsmamiko123", "shaurma"]

# users_input = input("enter your password: ")

# if users_input in passwords:
#     print("your password is in our server")
# else:
#     print("i don't know you, please register :)) ")


passwords_data = {
    "nika123" : "aguri",
    "giohackera" : "berlin123",
    "aguri2": "aguri3",
    "nikagamer123": "nika12345",
    "lukatmg" : "gaymer",
    "tvimedi" : "youtubeisdangerous",
    "pubgfan" : "iamgay",
    "forniteissobad" : "minecraftisbetter",
    "dota2" : "iamchad",
    "leagueoflegends" : "dota2tutorial"
}

username = input("welcome, enter your username: ")

if username in passwords_data:
    print("okay, now time for the password")
    password = input("enter your password: ")

    for key in passwords_data.keys():  #ციკლი მთლიან ბაზაში
        if key == username:   #ვამოწმებთ თუ გასაღები უდრის შეყვანილ იუზერნეიმს
            if password == passwords_data[username]:  #ვამოწმებთ თუ შეყვანილი პაროლი უდრის რეალურ პაროლს
                print("successfully login")
            else:
                print("invalid password")

else:
    print("please register")