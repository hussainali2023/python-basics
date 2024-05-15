mylist = [123, "hello", 3.123, True]

print(len(mylist))

print(mylist[1])

mylist[1] = "World"

print(mylist[1])

myListOne = [1, 2, 3]
myListTwo = myListOne
# myListOne = "chai"

myListOne[0] = 32

print(myListOne)
print(myListTwo)

l1 = [1, 2, 3]
l2 = l1

print(l1)
print(l2)

l1[0] = 33

print(l1)
print(l2)

a1 = [1, 2, 3]
a2 = a1
a2 = [1, 2, 3]

a1[0] = 22

print(a2)

b1 = [1, 2, 3]
b2 = b1[:] # copy of b1
