tup1=(1,2,3,4,5)
tup2=(1,2,3,4,5)
print(tup1>tup2)
print(tup1<tup2)
print(tup1==tup2)

print(max(1,0,3,8,2,9))
print(min(1,0,3,8,2,9))

print(tuple("Python"))
print(list("Python"))

x=tuple([1,2,3,4,5])
print(x)
print(type(x))

(val1,val2,val3)=(1,2,3)
print(val1,val2,val3)
tup1=(100,200,300)
print(tup1)
(val1,val2,val3)=tup1
print(val1,val2,val3)
(val1,val2,val3,val4)=(2+7,4,5/3,9%6)
print(val1,val2,val3,val4)

a=33
b=44
print(a)
print(b)
a,b=b,a
print(a)
print(b)

tup=(1,2,3,4,5)
list1=['a','b','c','d','e']
print(list((zip(tup,list1))))