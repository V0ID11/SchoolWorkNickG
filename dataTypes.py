from sys import getsizeof

test_variable = True
print(test_variable, type(test_variable)) #variable type can be found with type command

print(10/3, type(10/3))
print(10.0//3.0,type(10.0//3.0)) #integer division rounds down but if one is a float a float data type will remain

a = 5
a = a+0.1 #implicit by using the certain type
b = float(12) #explicit telling it to become a float

test_var = '😀'
print(test_var,type(test_var), getsizeof(test_var)) #use getsize of from sys to get size in bytes
