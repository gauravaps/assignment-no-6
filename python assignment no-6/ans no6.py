# write a python script to print whetether a given number is athree digit number or not.
'''a= int(input("enter a number"))

if 99<a<1000:
    print("this is three digit number")

else:
    print("not three digit number") '''


# other way 

num= int(input("enter a number"))
count=0
while(num>0):
   # digit=num%10
    num=num//10
    count+=1

if (count==3):
    print("nuber is three digit")

else:
    print("number is not three digit")        



   

   

