import numpy
## Main idaea is to create a program that reads both set of numbers and then tells if some item is in both setes
# Prior to that idea the goal is to insert a function that will tell if the conjunction of the sets makes a function, ahead of that were gonna create problems to the machine to solv
A = input("Type the A set")
B = input("Type the B set")
my_array = numpy.array([A])
my_array = numpy.array([B])
intersection = [value for value in A if value in B]

print(A , B)
print("the intersection of the set A:", A,  "and the set B", B, "forms the intersection AUB:", intersection)

#its horrible but it works i guess
