#This code gives you fabonacci numbers less 100(you can change the value for that matter). Also this uses rrecursion.
def fab(a,b):
  c=a+b
  if c<=100:
    print(c)
    a=b
    b=c
    fab(a,b)
a=0
b=1
print(a)
print(b)
fab(a,b)
