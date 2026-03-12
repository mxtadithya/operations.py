my_tuple=(2,4,56,34,2,5,6,32,89)
print(my_tuple[2])
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple.count(4))
print(my_tuple.index(56))
print(my_tuple[3:6])
print(my_tuple[-4:-1])

my_list=list(my_tuple)
my_list.remove(5)
my_tuple=tuple(my_list)
print(my_tuple)

fruits=('mango','apple','grape')
a,b,c = fruits
x,*y,z = fruits
print(a)
print(b)
print(c)
print(x)
print(y)
print(z)