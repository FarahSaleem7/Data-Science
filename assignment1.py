print("----------------------------Question no. 1--------------------------------------------")
print("Twinkle twinkle little star,\n \t How I wonder what you are!\n\t\t Up above the world so high, "
      "\n \t\t Like a diamond in the sky.\nTwinkle, twinkle, little star, \n \tHow I wonder what you are")


print("\n----------------------------Question no. 2--------------------------------------------")
import sys
print("Python version : "+sys.version)



print("\n----------------------------Question no. 3--------------------------------------------")
import datetime
now = datetime.datetime.now()
print ("Current date and time : "+ now.strftime("%Y-%m-%d %H:%M:%S"))

print("\n----------------------------Question no. 4--------------------------------------------")
import math
radius=input("Enter the radius: ")
area=3.14* (math.pow(int(radius), 2))
print("The area of the square is : "+ str(area))

print("\n----------------------------Question no. 5--------------------------------------------")
fname=input("Enter your First Name: ")
lname=input("Enter your Last Name: ")
reverse= (fname+" "+lname)[::-1]
print("Name in reverse order is :" + reverse)

print("\n----------------------------Question no. 5--------------------------------------------")
n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
print("The addition of two numbers is  :  "+str(n1+n2))
