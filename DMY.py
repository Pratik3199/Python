#Pratik Singh

d=int(input("Date"))
m=int(input("Month"))
y=int(input("Year"))
old_year=(2018-y)
print("Your Date of Birth is",d,"-",m,"-",y)
print("Your current year is", old_year)

if(old_year > 32):
    print("Your are my uncle ")
