boyage=int(input("Enter age of boy="))
if boyage>=21:
    print("Eligible to marry")

else:
    print("not eligible to marry")

girlage=int(input("Enter age of girl="))
if girlage>=18:
    print("Eligible to marry")
else:
    print("not eligibla to marry")



if boyage>=21 and girlage>=18:
    print("boy and girl both are eligible to marry")
