def square(num):
    return num ** 2

def square_list(nums):
    return [square(num) for num in nums]

def apply_func(func,nums):
    return [func(num) for num in nums]


print(square_list([1,3,4,6,7]))
print(apply_func(square,[1,3,4,6,7]))

def add_func(y):
    def add_two(n):
        return n+y
    return add_two



def add_something(n_to_add):
    def new_function(i):
        return i+ n_to_add
    return new_function

add_ten = add_something(10)
print(add_ten(4))