name = ['Tom', "Dick", "Harry"]
age = [12,15,16]
fav_colour = ["Red", "Blue", "Green"]

with open("files/colours.csv", "w") as csv:
    for i in range(3):
        csv.write(f'{name[i]},{age[i]},{fav_colour[i]}\n')