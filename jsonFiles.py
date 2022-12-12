import json
import urllib.request

# children = {}
# for i in range(3):
#     name = input("name: ")
#     nice_str = input("Nice? ")
#     if nice_str.lower()[0] == 'y':
#         nice = True
#     else:
#         nice = False
#     present = input('present: ')
#     children[name] = {'present': present, 'nice': nice}
# print(children)



# with open('files/presents.json', 'w') as json_file:
#     json_str = json.dumps(children, indent = 4)
#     print(json_str)
#     json_file.write(json_str)


type = input("What type of Cocktail do you want")
url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={type.lower()}"
data = urllib.request.urlopen(url).read().decode()
instructions = json.loads(data)
ingredients = []
for i in range(15):
    if instructions["drinks"][0][f"strIngredient{i+1}"] != None:
        ingredients.append(instructions["drinks"][0][f"strIngredient{i+1}"])
x = ", "
y = instructions["drinks"][0]["strInstructions"]
y = y.split(".")
print(f"Ingredients: {x.join(ingredients)}\nInstructions: \n", "\n".join(y))