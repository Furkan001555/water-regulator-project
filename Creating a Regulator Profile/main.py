Ho1=float(input("MAKSİMUM SU SEVİYESİNİ GİRİNİZ:")) # Yukarıdaki Kod Parçasıyla Çalıştığında Bu kısmı Silebilirsiniz.
#Menba Kısmının Boyutlandırılması
men=[[0,0],[-0.1,-0.005],[-0.2,-0.035],[-0.3,-0.125]]
for i in range(len(men)):

    A=men[i]
    Xmen=A[0]*Ho1
    Ymen=A[1]*Ho1
    print(f"{i}.X Değeriniz:{Xmen}")
    print(f"{i}.Y Değeriniz:{Ymen}")



#Mansap Kısmının Boyutlandırılması
A=int(input("Hassasiyet Giriniz:")) #Bu Kısım Numpy Kütüphanesiylede Çözülebilir Ancak Versiyondan Dolayı İndiremedim
flo=[]
for i in range(A):
       B=i*0.1
       flo.append(B)

for i in range(len(flo)):
     xmas=flo[i]
     Ymas=-Ho1*0.47*((xmas/Ho1)**1.80) # Bu kısımda Projede - değerler alınmış o yüzden - ile çarptım
     print(f"{i}.Y Değeriniz:{Ymas}")
#Etek Kısmının Boyutlandırılması
#Bu Kısımda Sadece Enterpolasyon Yaptırdık Formülüze Edilmesi Durumunda Enterpolasyona Gerek Kalmaz.


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
#Hocam Bu Kısımda Enterpolasyon Yapmaya Çalıştım Ama Hatalar Olabilir Sizde Müsait Olduğunuzda Kontrol Edersiniz. En Kısa Sürede Yanınıza Uğramaya Çalışacağım    """
