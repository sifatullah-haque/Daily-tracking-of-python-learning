print("Hello world")
a=21
b=23
print (a+b)
#+,-,*,/ are called arithmatic operator
print("Arithmatic operator 1(+); a+b=",a+b )
print("Arithmatic operator 2 (-); a-b=", a-b)
print("Arithmatic operator 3 (*);a*b=",a*b)
print("Arithmatic operator 3 (/);a/b=",a/b)
#Assignment operators
c=21
c+=5
c-=7
c*=8
c/=8
print(c)
#<,>,<=,>=, == , != are called comparision operators. it return a bullian nnumber
d=(7>4)
e= (56==56)
print(d)
# and or not are call logical operator 
bull1=True
bull2=False
print("bull1 and bull 2 is ", bull1 and bull2)
print("bull1 or bull2 is ", bull1 or bull2)
print("not of bull1", not bull1)
# converting
a = input("Enter your age= ")
print (a)
print(type(a)) #here the output will be str just because we have taken the input as str(if possible)
a= int(a)
print(type(a))#here the output will be int because we have converted the input into int(if possible)
#we can convert int to str and str to int exactly like  that. BUt not always. 
