# def wrapper():
#     print("Preparing a pizza base...   ")

# wrapper()

def my_decorator(func):
    def wrapper():
        print("Preparing a pizza base...   ")
        func()
        print("Adding toppings...   ")

    return wrapper

@my_decorator
def make_pizza():   
    print("Baking the pizza...   ") 

make_pizza()