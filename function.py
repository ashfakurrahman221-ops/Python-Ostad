print("Hello")
user_name = input("Enter your name: ")
print(f"Hello,{user_name}")


#user Defined Function

def greet(name):
    print(f"Hello, {name}. Welcome to the world of Python functions!")

greet("Ishtiak")

#default arguments
def print_my_name(f_name, l_name="Ahmed"):
    print(f"My name is {f_name} {l_name}")
print_my_name("Ishtiak")