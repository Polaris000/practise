# Regular iterations using a for loop allow us to access each element in a list, but not its index directly
# To find, for example, multiple instances of the same element in the list, one can use enumerate()
# This internally iterates over two lists --- the actual one and one storing the indices


fruits = ["apple", "banana"]

for index, fruit in enumerate(fruits, start=1):
        print(index, fruit)
