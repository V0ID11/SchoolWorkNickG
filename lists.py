

name_list = ['Sam', 'Mack', 'Jai', 'Jack', 'Nick', 'Edward', 'Ian', 'Matthew', 'Humphrey', 'Toby', 'Jacob']
for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(', '.join(name_list))

print(f"The third name is: {name_list[2]}")
print(f"The last seven names are: {', '.join(name_list[-7:])}")

numberList = []
for i in range(5):
    number = int(input("Enter a number"))
    numberList.append(number)

print(min(numberList))
print(max(numberList))
print(sum(numberList)/len(numberList))
print(sum(numberList))