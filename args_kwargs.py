

def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo("hello", "bye", 1, 2, gugu="hi")
