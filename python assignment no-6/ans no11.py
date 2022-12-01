# write a python script to take the month value  in numeric format and display the number of the day in it.

month= int(input("enter a month"))

if month==1 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(" month in 31 days")

else:
    print("months in 30 days")    