"""
The concept of args and kwargs comes in handy when one is not aware of the number of arguments a method will be given
args stands for arguments, akin to a python list
kwargs stands for keyword arguments, akin to a python dictionary
"""

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

    
foo("hello", "bye", 1, 2, gugu="hi")

"""
output:
    ('hello', 'bye', 1, 2)
    {'gugu': 'hi'}

"""
