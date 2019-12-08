'''
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are qeual")
else:
    print("a is greater than b")
'''
'''x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")'''

price = float(input("ราคาสินค้า : "))
vat = price*7/100
pricevat = vat+price
print("ภาษี 7%  = ", vat,"บาท")
print("ราคารวมภาษี = ", pricevat,"บาท")
threeper = pricevat*3/100
fiveper = pricevat*5/100
sevenper = pricevat*7/100
tenper = pricevat*10/100
#--------------------
if price < 1000:
    print("ราคาสินค้า : ",pricevat)
elif price < 2000:
    print("ราคาสินค้า : ",(pricevat-threeper),"บาท")
elif price < 3000:
    print("ราคาสินค้า : ",(pricevat-fiveper),"บาท")
elif price < 5000:
    print("ราคาสินค้า : ",(pricevat-sevenper),"บาท")
else:
    print("ราคารวมส่วนลดสุทธิ : ",(pricevat-tenper),"บาท")