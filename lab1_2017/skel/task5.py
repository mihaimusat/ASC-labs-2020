# More python stuff!!!

""" Mutability """

l1 = [0, 1, 2, 3, 4, 5]
l2 = l1

# TODO modify l2, print l1 and l2
l2[1] = 100
print(l2)
print(l1)

######

t1 = ('a', 'b')
t2 = t1

# TODO modify t1, print t1 and t2
tmp = list(t1)
tmp[0] = 'c'
print(tuple(tmp))

######

s1 = "abc"
s2 = s1

print(id(s1))
print(id(s2))

s1 = s1.upper()

# TODO print s1 and s2 and their id()
print(s1)
print(s2)
print(id(s1))
print(id(s2))
######


""" List comprehensions """

my_list = [5] * 5 + [3] * 2 + [4] * 2 + [10] * 3
# TODO: print a list of all the odd elements divided by 10, using list comprehensions
print(my_list)
comp = [x for x in my_list if x%2 != 0 and x%10 == 0]
print(comp)

""" Identity vs equality """

size = 10
a = 'a' * size
b = 'a' * size

print(a == b)
print(a is b)

print(id(a))
print(id(b))

# TODO check the size from which a no longer has the same references as b

n = 10
m = 10

print(n == m)
print(n is m)

print(id(n))
print(id(m))

# TODO Give n and m a value so that n is m is False

