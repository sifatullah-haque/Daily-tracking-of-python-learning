print("Hello", "World", "my name", ("is"), ("sifat"), sep="_")#sep"*" with in the double quote if you write something it will turn every space with it
#sequential formatting
a = "Hey"
b = "my name"
c ="sifat"
print("{} is {}".format(b,c))
print("{} {} is {}".format(a, c,b))
#pass value as a number while formatting
print("{0} {2} is {1}".format(a,b,c))
#pass value as a name while formatting
print("{name1} {name2} is {name3}".format(name1=a,name2=b,name3=c))
#pass value as a tuple
print("%s %s is %s "%(a,b,c))
#Input mathod
# input1=input( "Enter your name " )
# input2 =input("Enter your age ")
# print("Your name is {} \nyour age is {} ".format(input1, input2))
#Taking many input in a single line
# q,w,e,r,t,y = input("Enter some number with space between them= ").split()
# print("{}{}{}{}{}{}".format(q,w,e,r,t,y))
#to check if anything that we need are present in the list or line or not
dummy_txt = "Hello there this is a random text i don't know what i am writting. I am writting this because i wanna learn about 'in' operators"
print("there" in dummy_txt)
g = 12
h = 12
print(g is h)#python usually add same number under the same address
