user = {}

name = input("what is your name :")
age = input("what is your age :")
fav_mov = input("your fav movie ,").split(" ,")
fav_song = input("your fav song ,").split(" ,")

user["name"] = name
user["age"] = age
user["fav_mov"] = fav_mov
user["fav_song"] = fav_song

for key, value in user.items():

    print(f"{key} : {value}")