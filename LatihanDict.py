import os
import random
import string

data = dict()
while True:
    os.system("cls") # WIN
    # os.system("clear") # mac/linux
    print(f" {'DATA TATA SURYA':❤^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    bumi = input("Enter planet biru\t\t:")
    jupiter = input("Enter planet terbesar\t\t:")
    saturnus = input("Enter planet bercincin\t:") 

    data[ keyFinal ] = { 'bumikey' : bumi, 'jupiterkey' : jupiter,'saturnuskey' : saturnus } 
     
    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"Key\t Biru\t besar\t bercincin")
print("-"*40)
for key, value in data.items():
    print(f"{key}.\t {value['bumikey']}\t {value['jupiterkey']}\t \t{value['saturnuskey']}")