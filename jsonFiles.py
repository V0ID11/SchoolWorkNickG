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
drinks = urllib.request.urlopen(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={type}").read().decode()
drinks = json.loads(drinks)
drinks = drinks["drinks"]
choice = 1
if len(drinks) > 1:
    print()
    for i,drink in enumerate(drinks):
        drink_name = drink["strDrink"]
        print(f"{i+1}) {drink_name}")
    choice = int(input("\nWhat drink do you want: "))

try:
    instructions = drinks[choice-1]
except:
    instructions = drinks[0]
        



ingredients = []
for i in range(15):
    if instructions[f"strIngredient{i+1}"] != None:
        ingredients.append(instructions[f"strIngredient{i+1}"])
measures = []
for i in range(15):
    if instructions[f"strMeasure{i+1}"] != None:
        measures.append(instructions[f"strMeasure{i+1}"])
x = "\n "
ingMeasures = {}
for i in range(len(ingredients)):
    try:
        ingMeasures.update({ingredients[i]:measures[i]})
    except:
        ingMeasures.update({ingredients[i]:"Follow Instructions"})
y = instructions["strInstructions"]
y = y.split(".")
print("Name: ", instructions["strDrink"])
print("Ingredients: \n", x.join(i+":"+ingMeasures[i] for i in ingMeasures))
print("Instructions: \n", "\n".join(y))