""" global_a = "global"


def foo():
    local_a = "local"
    return(local_a)


print(foo())
print(global_a)

"""


# using global keyword:

global_x = 10

def foo():

    global x 
    # this line allows the use of the actual global var in local scope
    # that is, the value of global scope can be modified

    global_x = 5

    print(global_x)
