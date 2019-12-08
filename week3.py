import math

#inputbath = float(input("จำนวนเงินบาท : "))
#sum = inputbath/38.97
#print("แปลงค่าเงินปอนด์ได้ คือ ",sum,"ปอนด์")

#inputbath = float(input("ราคาสินค้า : "))
#sum = inputbath*7/100
#ans = sum +inputbath
#print("รวมภาษีมูลค่าเพิ่ม 7% ทั้งหมด รวมเป็น : ",ans)



#inputnn = float(input("น้ำหนัก : "))
#inputh = float(input("ส่วนสูง : "))
#sum = inputh*inputh
#ans = inputnn/sum
#print("BMI =  : ",ans)

inputpcar = float(input("ราคารถ : "))
inputvat = float(input("อัตราดอกเบี้ย : "))
inputpon = float(input("จำนวนปีที่ต้องการผ่อน : "))
#sum = inputpcar*inputvat/100
#per = sum+inputpcar
#ans = per/(inputpon*12) 
ans = (((inputpcar*inputvat/100)+inputpcar)/(inputpon*12))
print("ผ่อนเดือนละ =  : ",ans,"บาท")

#((20*2)*2+1/2)*5-1(222-156)
