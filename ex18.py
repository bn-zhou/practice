# this one is like your scripts whis arg

def print_two(*args):
    arg1, arg2 = args
    print ("arg1:",arg1,"arg2:",arg2)

#ok, that *arg is actually pointless, we can just do this.
def print_two_again(arg1,arg2):
    print ("arg1:",arg1,"arg2:",arg2)

#this just takes one argument
def print_one(arg1):
    print ("arg1:",arg1)

#this one takes no arguments
def print_none():
    print("I got nothin'.")



print_two("Zad","Shaw")
print_two_again("Zad","Shaw")
print_one("First!")
print_none()
