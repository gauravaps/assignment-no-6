# write a python script to accept one complex number from the users and display the greater number between real part and imaginary part.

num= complex(input("enter a number"))

if num.real>num.imag:
    print(num.real)

else:
    print(num.imag)    