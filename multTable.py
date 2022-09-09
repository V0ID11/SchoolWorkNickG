
while True:
    table = input("What table do you want to view")
    if table.isnumeric():
        break    
    else:
        print("Please make sure you print a number")
        continue
for i in range(13):
    print(f"{i} x {table} = {i*int(table)}")