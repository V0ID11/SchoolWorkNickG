item = input("What would you like to compress: ")
number = []
count = 1
first = item[0]
for i in range(1,len(item)):
    if item[i] == first:
        count += 1
    else:
        try:
            number.append([first, count])
            count = 1
            first = item[i]
        except:
            break
number.append([first,count])
print(number)
