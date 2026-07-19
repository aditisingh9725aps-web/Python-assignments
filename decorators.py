def my_decorator (func):
    def wrapper():
        print("something is happening before the function is called.")
        func()
        print("something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

#generators
def countdown(n):
    while n>0:
        yield n
        n-=1
#using generators
for num in  countdown(5):
    print(num)

#closures
def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func
add_five=outer_func(5)
print(add_five(3))
#iterators
my_list=[1,2,3,4,5]
my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


