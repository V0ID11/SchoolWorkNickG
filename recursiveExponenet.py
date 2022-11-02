import timeit
def exponentByRecursion(a,n):

    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        if n % 2 == 0:
            result = exponentByRecursion(a,n/2)
            return result * result
        else:
            result = exponentByRecursion(a,(n-1)/2)
            return result * result * a

start = timeit.default_timer()
exponentByRecursion(2,343002)
end = timeit.default_timer()
print(end - start)