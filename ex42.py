class Thething(object):

    def __init__(self):
        self.number = 0

    def some_function(self):
        print("我接到一个电话")

    def add_me_up(self,more):
        self.number += more
        return self.number

# Two different things
the_one = Thething()
the_two = Thething()

the_one.some_function()
the_two.some_function()

print(the_one.add_me_up(20))
print(the_one.add_me_up(20))
print(the_two.add_me_up(30))
print(the_two.add_me_up(30))

print(the_one.number)
print(the_two.number)


