def reverse(n):
    if n < 10:
        print(n)
    else:
        print(n%10)
        reverse(n//10)
reverse(3124)
