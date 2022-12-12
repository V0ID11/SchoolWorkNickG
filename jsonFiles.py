import json

children = {}
for i in range(3):
    name = input("name: ")
    nice_str = input("Nice? ")
    if nice_str.lower()[0] == 'y':
        nice = True
    else:
        nice = False
    present = input('present: ')
    children[name] = {'present': present, 'nice': nice}
print(children)

json_str = json.dumps(children)
print(json_str)