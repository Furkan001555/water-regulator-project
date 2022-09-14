#Çökeltim Havuzu Kodları
#Re Sayısına Bağlı Olarak Geçiş Hali, Türbülan Akım Ve Laminee Akım Şartları Aranmaktadır
#Random Kütüphanesi Kullanılmıştır
#Hüseyin Furkan Yalvaç Tarafından 14.09.2022 Tarihinde Geliştirilmiştir.
"""----------------------------------------------------------------------"""
import random
#a Katsayısının Bulunması Ve Yatay Hızın Tespiti
D=float(input("Çökeltmek istediğiniz Dane Çapını Giriniz:"))
Qmin=float(input("Minimum Debiyi Giriniz:"))
Pdane=float(input("Dane Özgül Ağırlığını Giriniz:"))
hc=float(input("Lütfen Çökeltim Havuzunun Yüksekliğini Giriniz:"))
J=float(input("Lütfen Yük Kaybını Giriniz:"))
No=int(input("Lütfen Okul Numaranızın 8.Hanesini Giriniz:"))


if(D<0.1):
    a=51
elif(0.1<D<1):
    a=44
else:
    a=36
Va=round((a*(D**0.5)/100),1)
# W Düşey Hızın Bulunması
A=0
while True:
    Re=random.uniform(0,2000)
    if(Re<0.5):
        Cd=24/Re
        W = (1.33 * ((Pdane - 1) / 1) * (9.81) * (D / (Cd * (10 ** 3)))) ** 0.5

        Re1 = (W * D * 0.001) * (10 ** 6)
        if (Re1 - 0.1 <= Re <= Re1 + 0.1):
            print("Laminer Akım")
            break

    elif(0.5<=Re<=1000):
        Cd=(24/Re)+(3/(Re**0.5))
        W = (1.33 * ((Pdane - 1) / 1) * (9.81) * (D / (Cd * (10 ** 3)))) ** 0.5

        Re1 = (W * D * 0.001) * (10 ** 6)
        if (Re1 - 0.1 <= Re <= Re1 + 0.1):
            print("Geçiş Hali")
            break


    elif(1000<Re):
        Cd=(0.4+0.5)*0.5
        W = (1.33 * ((Pdane - 1) / 1) * (9.81) * (D / (Cd * (10 ** 3)))) ** 0.5
        Re1 = (W * D * 0.001) * (10 ** 6)
        if (Re1 - 0.1 <= Re <= Re1 + 0.1):
            print("Türbülanslı Akım")
            break







if(1.5<=hc<=4 and 0.01<=J<=0.04):
      L=(hc*Va)/W
      Qc=Qmin*(0.4+(No/100))
      Bc=(Qc/(Va*hc))
      if(Bc/hc>1.5):
          hcson=hc+(L*J)
          Qyk=Qc*0.10
          hyk=(Qyk/3)**0.5
          byk=hyk*1.5
          print(f"Çökeltim Havuzu Son Yükseklik:{hcson}")
          print(f"Çökeltim Havuzu Genişliği:{Bc}")
          print(f"Çökeltim Havuzu Uzunluğunu Giriniz:{L}")
          print(f"Yıkama Kanalı Genişliği:{byk}")
          print(f"Yıkama Kanalı Yüksekliği:{hyk}")
          print(f"Yatay Hızını:{Va}")
          print(f"Re Sayınız:{Re}")
          print(f"Düşey Hızınız:{W}")


else:
    print("Lütfen Geçerli Değerler Giriniz")