import random

Hc=float(input("Çökeltim Havuzunun Yüksekliği:")) #Bu Değer 3. Hafta Kodlarından Alınmıstır 3.hafta Kodları İle Kullanıldığında Buralar Silinebilir..
Qc=float(input("Debi:"))                          #Bu Değer 3. Hafta Kodlarından Alınmıstır 3.hafta Kodları İle Kullanıldığında Buralar Silinebilir..
Bcc=float(input("Cökeltim HAvuzu Genisliği:"))    #Bu Değer 3. Hafta Kodlarından Alınmıstır 3.hafta Kodları İle Kullanıldığında Buralar Silinebilir..
#İsale Kanalı Giriş Yüksekliğinin Belirlenmesi
while(True):
  Hi=round(random.uniform(1,5),2)
  Ec=Hc+(0.00815) #Va hızı 0.4 m/s alınmıştır.
  Ei=Hi+(((Qc/(Bcc*Hi))**2)/19.62)
  if((Ei-0.01)<=Ec<=(Ei+0.01)): #Tam Değer Bulunmaya Çalışıldığında Binlerce Kez Denenmektedir Ancak Bir aralık Verildiğinde Daha Kısa Sürede Tespit Edilir.
      print(f"İsale Kanalı Giriş Yüksekliği:{Hi} m")
      print(f"Çökeltim Havuzu Su Enerjisi:{Ec}")
      print(f"İsale Kanalı Giriş Enerjisi:{Ei}")
      break
  else:
      print(f"Seçilen İsale Kanalı Giriş Yüksekliği:{Hi} m")

#Eisale Belirlenmesi
while(True):
  Dh=random.uniform(0,0.1)
  Dhh=2.88*Bcc*((0.67*(Dh**1.5))+((Dh**0.5)*Hc))
  if( (Qc-0.1)<=Dhh<=(Qc+0.1)):
      print(f"Yıkama Kanalı Yüksekliğinden Dolayı Oluşan Yük Kaybı:{Dh} m")
      break
  else:
      print(f"Seçilen Yük Kaybı:{Dh}")
      print(Dhh)
Dz=float(input("Yıkama Kanalı Yüksekliği:"))

Ei=Ec-Dz-Dh
print(f"İsale Kanalı Su Enerjisi:{Ei} m")
# İsale Kanalı Giriş Yükeskliğinin Belirlenmesi
while(True):
    His=random.uniform(0,1)
    Eis=His+(((Qc/(Bcc*His))**2)/19.62)
    if(Ei-0.01<=Eis<=Ei+0.01):
        print(f"İsale Kanalı Giriş Yüksekliği:{His} m")
        print(Eis)
        break
    else:
        print(f"Seçilen İsale Kanalı Giriş Yüksekliği:{His}")
        print(Eis)

#İletim Borusu Dic Bulunması,Froude Sayısı Tespiti Ve Akış Türünün Belirlenmesi
Qc=4.7
while(True):
    Vil=float(input("İletim Borusunda Kullanılacak Hızı Giriniz:"))
    if(0.6<Vil<1.8):
        Bad=int(input("Kullanmak İstediğiniz Boru Adedini Giriniz:"))
        print(f"İsale Kanalındaki Kullanılacak Debi {Qc*1000} L/sn")
        Qis=Qc/Bad
        Dic=((4*Qis)/(Vil*3.141592))**0.5
        print(f"İletim Borularının İç Çapları {Dic} mm")
        break
    else:
        print("Hız Değerini Tekrar Giriniz!!!!")

Fr=Vil/(9.81*(Dic/1000))
print(f"Froude Sayınız: {Fr}")
if(Fr<1):
    print("Akış Nehir Rejmidir")
else:
    print("Akış Sel Rejmidir")
# S Değerinin Bulunması
VA=float(input("Wittman Quick Eğrisi:"))
VB=float(input("Gordon Eğrisi:"))
VC=float(input("Reddy Rickford Eğrisi:"))
VD=float(input("Denny Joung Eğrisi:"))

Grf=[VA,VB,VC,VD]
MaxGrf=max(Grf)
print(MaxGrf)
S=(Dic/1000)*MaxGrf
print(f"S Değeri:{S} m")

# Hsualma Yapısının Boyutlandırılması
Hsu=S+Dic+(0.3*Dic)
print(f"Su Alma Yapısının Yüksekliği:{Hsu} m")
print(f"Kare Teşkil Edildiğinden Lsu:{Hsu} m")