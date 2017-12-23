"""def repeat(func):
   func()
   func()

   return("twice")

# @repeat ----> outputs: hi
                        #hi
def func_hi():             
   print("hi")

# repeat(func_hi) ----> outputs: hi
                                 #hi

func_hi = repeat(func_hi)  # ---> outputs: hi
                                          #hi

# func_hi()
print(func_hi) # ----> outputs: twice
# print(func_hi()) ----> outputs: str not callable error

"""
# -----------------------------------------------------------------------

"""
def my_decorator(func):
   def func_return(*args, **kwargs):
      print(1)

      func(*args, **kwargs)

      print(2)

   return func_return

@ my_decorator
def is_str(x):
   if type(x) == str:
      print("str")

   else:
      print("not str")


#is_str("yo") ---> method 1

#is_str = my_decorator(is_str("yo")) ---> method 2
"""
# ------------------------------------------------------------------------

"""
def foo():
   def bas(name):
      return("hi " + name)

   return bas


baz = foo()  

# print(baz("Polaris")) ---> o: hi Polaris

# print(baz) ---> o: <function foo.<locals>.bas at ....>

# print(foo("Polaris")) ---> o: TypeError: foo() takes 0 positional arguments
#                                      but 1 was given

# print(bas("Polaris")) ---> o: NameError: name 'bas' is not defined

# print(foo.bas("Polaris")) ---> o: AttributeError: 'function' object has no
#                                    attribute 'bas'

"""
# ---------------------------------------------------------------------------

"""
def decorate(func):
   def wrapper(name):
      return("hi " + func(name))

   return(wrapper)

@decorate
def get_text(name):
   return(name)

# without decorator:
# final = decorate(get_text)
# print(final("Polaris")) ---> o: hi Polaris

# with decorator:
# final = get_text("Polaris")
# print(final) ---> o: hi Polaris
"""
# -----------------------------------------------------------------------

"""
# multiple decorators:

def _dec(func):

   def wrapper(name):

      return("_" + func(name) + "_")

   return(wrapper)


def i_dec(func):

   def wrapper(name):

      return("i" + func(name) + "i")

   return(wrapper)


@_dec
@i_dec
def foo(name):
   return("+" + name + "+")

final = foo("Polaris")

print(final) ---> o: _i+Polaris+i_
"""
# ------------------------------------------------------------------------

"""
# decorator generator:

def dec_gen(tag):

   def decorator(func):

      def wrapper(name):

         return("{0}{1}{0}".format(tag, func(name)))

      return(wrapper)

   return decorator


@dec_gen("_")
@dec_gen("i")
@dec_gen("+")
def get_name(name):
   return(name)

print(get_name("Polaris")) ---> o: _i+Polaris+i_
"""
# -----------------------------------------------------------------------

"""
# checking __name__, __module__ and __doc__
# the wrapper function's attribute values are used..
# to get those of the original function, import wrap from functools

from functools import wraps

def dec_gen(tag):

   def decorator(func):

      @wraps(func)
      def wrapper(name):
         # (docstring_wrapper)  --> both the part that's in () inside""
         return("{0}{1}{0}".format(tag, func(name)))

      return(wrapper)

   return decorator


@dec_gen("_")
@dec_gen("i")
@dec_gen("+")
def get_name(name):

   # (docstring get_name) --> both the part that's in () inside""

   return(name)


print(get_name.__name__)
print(get_name.__module__)
print(get_name.__doc__)

# without @wraps:
#o: wrapper, __main__, docstring_wrapper

# with @wraps:
#o: get_name, __main__, docstring get_name

"""