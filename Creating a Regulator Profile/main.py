"""
Hello I am the Developer of This Code
This Coding has been coded for Konya Technical University Civil Engineering Hydraulics Department.
By substituting the values given with this code, the dimensioning of the structure is done.
It has tried to interpolate with the limitations given with this code.
This code was developed by Hüseyin Furkan YALVAÇ on 13.09.2022
Advisor: Cihangir KÖYCEĞİZ
"""

Ho1=float(input("MAKSİMUM SU SEVİYESİNİ GİRİNİZ:"))
# Sizing of the Upstream Section
men=[[0,0],[-0.1,-0.005],[-0.2,-0.035],[-0.3,-0.125]]
for i in range(len(men)):

    A=men[i]
    Xmen=A[0]*Ho1
    Ymen=A[1]*Ho1
    print(f"{i}.X Değeriniz:{Xmen}")
    print(f"{i}.Y Değeriniz:{Ymen}")



# Sizing the Downstream Section
A=int(input("Hassasiyet Giriniz:")) # This Part Can Be Solved With The Numpy Library, But I Could Not Download It Due To The Version
flo=[]
for i in range(A):
       B=i*0.1
       flo.append(B)

for i in range(len(flo)):
     xmas=flo[i]
     Ymas=-Ho1*0.47*((xmas/Ho1)**1.80) # In this part - values are taken in the Project, so I multiplied with -
     print(f"{i}.Y Değeriniz:{Ymas}")
# Sizing the Skirt
# In this part, we have only interpolated, and if it is formulated, no interpolation is required.


BirSayi=float(input("Birinici Aralığı Giriniz:"))
ikiSai=float(input("İkinci Aralığı Giriniz:"))
Sonuc5=float
Sonuc51=float

if(BirSayi<Ho1<ikiSai):

    Sayi1 = float(input("Birinici Sayıyı Giriniz:"))
    Sayi2 = float(input("İkinci Sayıyı Giriniz:"))
    Sonuc1=(Ho1-BirSayi)
    Sonuc2=abs(Sayi2-Sayi1)
    Sonuc3=abs(ikiSai-BirSayi)
    Sonuc4=((Sonuc1*Sonuc2)/Sonuc3)
    if(Sayi2>Sayi1):

      Sonuc5=Sonuc4+Sayi1
      print(f"Birinici Değer:{Sonuc5}")
      Sayi3 = float(input("Üçüncü Sayıyı Giriniz:"))
      Sayi4 = float(input("Dördüncü Sayıyı Giriniz:"))
      Sonuc11 = (Ho1 - BirSayi)
      Sonuc21 = abs(Sayi2 - Sayi1)
      Sonuc31 = abs(ikiSai - BirSayi)
      Sonuc41 = ((Sonuc11 * Sonuc21) / Sonuc31)

      if(Sayi3>Sayi4):
          Sonuc51=Sonuc41+Sayi4
          print(f"İkinci Değer:{Sonuc51}")
      else:
          Sonuc51 = Sonuc41 + Sayi3
          print(f"İkinci Değer:{Sonuc51}")
      RevSon2=Sonuc51
    else:
        Sonuc5=Sonuc4+Sayi2
        print(f"Birinci Değer:{Sonuc5}")




else:
    print("Geçersiz Sayı Girdiniz!!!")


RevSayi1 = Sonuc5
RevSayi2 = Sonuc51
Bagh=float(input("Birinci Aralığı Giriniz:"))
Bagh1=float(input("İkinci Aralığı Giriniz:"))
BagSon=float(input("Bağlama Yükseklğini Giriniz:"))
if(Bagh1<BagSon<Bagh1):
    Sonuc1=Bagh1-Bagh
    Sonuc2=abs(RevSayi2-RevSayi1)
    Sonuc3=abs(Bagh-BagSon)
    Sonuc4=(Sonuc3*Sonuc2)/Sonuc1
    Sonuc52=Sonuc4+RevSayi1
    print(f"Etek Yarıçapı:{Sonuc52}")


else:
    print("Lütfen Geçerli Aralık Giriniz")
# I Tried To Interpolate In This Part, But There May Be Errors
