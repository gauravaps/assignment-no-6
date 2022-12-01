# write a python script to print greater number  among three numbers.print number only once even if the numbers are the same.

a,b,c=int(input("a")),int(input("b")),int(input("c"))

if a>=b and a>=c:
    print(a)


elif b>=a and b>=c:
    print(b) 

elif a==c and b==c:
    print("same number")

else:
    print(c)     






   

   

