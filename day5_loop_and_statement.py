'''problem 5:  Write a program to check whether a number entered by user is even or odd.'''
# a = int (input("Enter a number= "))
# if a%2==0:
#     print("Its an even number")
# else:
#     print("its an odd number")
'''prob_6: Write a program to check whether a number is divisible by 7 or not.'''
# num = int(input("Enter any number= "))
# if num%7==0:
#     print("THis number is divisible")
# else:
#     print("This numer is not divisible")
#problem_7: Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise pront bye
# num = int(input("Enter any number= "))
# if num%5==0:
#     print("hello")
# else:
#     print("bye")
'''Q8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)'''
# num= int(input("Enter the unit of the bill= "))
# amount=0
# if num<=100:
#     print("No charge")
# elif 100<num<=200:
#     amount=(num-100)*5
#     print("Your bill is = ", amount)
# else:
#     amount= 500+(num-200)*10
#     print("Your bill is = ", amount)
'''Q9. Write a program to display the last digit of a number.'''
# num=int(input("Enter any numbr = "))
# print("the last digit is= ", num%10)
'''Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.'''
# num=int(input("Enter any numbr = "))
# last_digit= num%10
# if last_digit%3==0:
#     print("divisible by 3")
# else:
#     print("Not divisible by 3")
'''Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                      A
         > 80 and <= 90                            B
         >= 60 and <= 80                           C
         below 60                                  D'''

# num=int(input("Enter your mark = "))
# if num in range(0,100):
#  if num>90:
#     print("Your Grade is 'A'")
#  elif 80<num<=90:
#     print("Your grade is 'B'")
#  elif 60<=num<=80:
#     print("Your grade is 'C'")
#  elif num==0:
#     print("You Failed")
#  else:
#     print("Your grade is 'D'")
# else:
#     print("enter a valid number")






'''while loop'''
# i=1
# j=1
# while i<=5:
#     while j<=5:
#         print("i= ", i, " j= ", j, sep="")
#         j +=1
#     j=1
#     i+=1
'''for loop'''
for i in range(1,10):
    for j in range(1,5):
        print("i= ",i,"j= ", j ,sep="" )