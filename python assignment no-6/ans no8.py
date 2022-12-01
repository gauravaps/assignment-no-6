# write a python script to print whetether a givenquadratic equation has two real & distinct roots ,ral,& equal root &or imaginaryroots.

x,y,z=int(input("x ")),int(input("y" )),int(input("z "))

ans=(y*y) - 4*x*y
if ans>0:
    print("distinct and real")

elif ans==0:
    print("real and equal")
else:
    print("imaginary")


   

   

