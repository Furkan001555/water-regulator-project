"""
Hello I am the Developer of This Code
This Coding has been coded for Konya Technical University Civil Engineering Hydraulics Department.
With this code, the energy breaker pool type of the building has been determined according to the USBR-1987 standards.
The regulator has been verified according to hydrostatic forces.
Python Math Library Used
This code was developed by Hüseyin Furkan YALVAÇ on 17.11.2022
Advisor: Cihangir KÖYCEĞİZ

"""

#Determination of Energy Breaking Structure
import random
import math

P=float(input("Savak Yüksekliğini Giriniz:"))
Ho=float(input("Maksimum Su Seviyesini Giriniz:"))
Qmax=float(input("Maksimum Debiyi Giriniz:"))
B=float(input("Maksimum Debinin Geçeceği Genişliği Giriniz:"))
C=float(input("Zemin Cinsine Bağlı Olarak Katsayıyı Giriniz:"))
tk = float(input("Düşüm Kalınlığını Giriniz:"))
while True:
    H1 = random.uniform(0, 1)
    Denk1 = ((P + Ho - H1) * 2 * 9.81) - (((Qmax) / (B * H1)) ** 2)

    if(0<=Denk1<=0.5):

        break

while True:
    H2 = random.uniform(1, 25)
    Denk1 = ((P + Ho - H2) * 2 * 9.81) - (((Qmax) / (B * H2)) ** 2)

    if(0<=Denk1<=0.5):
        print(f"Hidrolik Sıçramanın Yapılacağı Su Yüksekliği:{H2} Nehir Rejmi")
        print(f"Hidrolik Sıçramanın Yapılacağı Su Yüksekliği:{H1} Sel Rejmi")
        break
V=((Qmax)/(B*H1))
Fr=((V)/((9.81*H1)**0.5))
print(f"Hız Değeri:{V}")
print(f"Froud Sayısı:{Fr}") # The Pool Type is Selected with the Values Found here.
if(1<Fr<1.7):
     print("Havuz 1.Tip")
     print(f"Havuz Uzunluğu{5*H2}")

elif(1.7<Fr<2.5):
    print("Havuz 1.Tip")
    print("Havuz Uzunluğu Tablodan Okunur")
elif(2.5<Fr<4.5):
    print("Havuz 4.Tip")
    print(f"h3 Değeri:{1.1*H1}")
elif(4.5<Fr<9 and V<17):
    print("Havuz 3.Tip")
    while(True):
        h2=random.uniform(0,5)
        denk3=((H1*0.5)*(((8*(Fr**2))+1)**0.5)-1)-h2
        if(0<denk3<0.5):
            h3=((1.33*Fr)+0.72)*h2
            d4=((0.142*h3)+1.51)*H1
            d3=((0.0357*h3)+1.53)*H1
            print(f"Engel Yüksekliği:{d4}")
            print(f"Çıkış Eişiği Yüksekliği:{d3}")
            S1=(B/(2*H1))
            S3=(B/(2*0.75*d3))
            print(f"Düşüm Engeli Sayısı:{round(S1)}")
            print(f"Enerji Kırıcı Yapı Sayısı:{round(S3)}")
            print("Sıçrama Uzunluğunu Tablodan Okuyunuz")
            break


elif(4.5<Fr<9 and 17<V):
    print("Havuz 2.Tip")
else:
    print("Havuz Tipi USBR Standartları Dışında")


# Crest Width Base Width
horan=(Ho/(P+Ho))
psu=1
m=0.7
pbeton=2.5
poran=(pbeton/psu) # Ratio of Concrete Density to Water Density
C1=1-((horan**2)*(2-horan))
C2=1-((horan**2)*(3-2*horan))
tana=((C2)/((C1*poran)-m))**0.5
B=Ho*tana
Bta=(Ho+P)*tana
print(f"Taban Genişliği:{Bta}")
print(f"Kret Genişliği:{B}")
print(f"Tepe Açısı:{math.degrees(math.atan(tana))}")
# Investigation of Forces Acting on the Body
n=0.3
P1=(((P*P)/2)*psu)
P2=(((P+(P+2))/2)*2*psu)
G1=B*P*pbeton
G2=(((Bta-B)*P)/2)*pbeton
G3=Bta*2*pbeton
U1=Bta*n*psu*(P+2)
U2=((Bta*((m*psu*(P+2))-(n*psu*(P+2))))/2)*psu
# Overturn Inspection
Mk=(G1*(Bta-(B/2)))+(G2*((Bta-B)*0.66666))+((G3)*(Bta/2))
Md=(P1*((P*0.333)+2))+(P2*1)+(U1*(Bta*0.66666))+(U2*(Bta*0.5))
A=Mk/Md
if(1.5<=A):
    print("Yapı Devrilmeye Karşı Güvenlidir")
else:
    print("Yapı Devrilmeye Karşı Güvensizdir")

# Slip Inspection
Pkay=P1+P2
Pkor=G1+G2+G3-(U1+U2)
if(0.4<=Pkay/Pkor):

    Sb = float(input("Sıçrama Boyunu Giriniz:"))

    A=Pkay/(Pkor+(tk*1*pbeton*Sb))
    if(0.4<=A):
        print("Yapı Kaymaya Göre Güvensizdir")
    else:
        print("Yapı Kaymaya Karşı Güvenlidir")
else:
    print("Yapı Kaymaya Karşı Güvenlidir")

# Base Pressure Inspection
Ntop=G1+G2+G3
Mtop=-(P1*((P/2)+2))-(P2*1)+(G1*((Bta/2)-(B/2)))+(G2*((Bta*0.5)-(((Bta-B)*0.333)+B)))+(U2*((Bta*0.5)-(Bta*0.333)))
A=Bta*1
W=(1*(Bta**2))/6
Qmax=(Ntop/A)+(Mtop/W)
Qmin=(Ntop/A)-(Mtop/W)
if(Qmax<=25 and 0<=Qmin):
    print("Taban Basıncı Uygundur")
else:
    print("Taban Basıncı Uygun Değildir")
# Infiltration Inspection

H=P+tk
L=C*H
L1=2+((7.57*7)*0.3333)+1+2.89
if(L1<=L):
    print("Palplanıj İnşa Edilir")
    Lp=(L-1-2.89-2-((7.57*7)*0.333))/2
    print(f"Palplanıj Boyu:{Lp}")
else:
    print("Palplanıj İnşasına Gerek Duyulmaz")
