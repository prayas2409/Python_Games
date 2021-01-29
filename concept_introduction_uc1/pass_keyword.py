def do_nothing():
    # this gives a method that it'll do nothing
    # As it'll do a pass that means skip what is below me in current scope
    pass

do_nothing()
print("called do_nothing which did nothing")

demo_var = 10
if demo_var == 10:
    # as demo var is equal to 10 it'll not do anything
    pass
else:
    print("not equal to 10")

print("Executed if else")

while demo_var==10:
    # as it'll always be true it'll be running continously but nothing would be shown
    pass