import random
i=0
Bcc=0
B=int(input("Okul Numaranızın 8.Hanesini Giriniz:"))

while(True):
    ex=int(input("Çıkmak İçin 1'e Basınız:"))
    if(ex!=1):
        Hd = float(input("Dalgıç Perdenin Suya Batan Yüksekliği(cm):"))
        Hg = float(input("Giriş Eşiği Yüksekliğini Giriniz(cm):"))
        if (105 > Hd >= 40):
            if (150 > Hg >= 50):
                Bc = float(input("Çökeltim Havuzu Genişliğini Giriniz(cm):"))
                while (True):
                    b = random.uniform(14, 15)
                    n = random.randint(1, 50)
                    i = 0
                    if ((((5 * n) + (n * b) + b) - 0.1) <= Bc <= (((5 * n) + (n * b) + b) + 0.1)):
                        print(f"Aralık Sayınız:{n} adet")
                        print(f"Izgara Kalınlığı: {b}cm")
                        print(f"Izgaralar Arasındaki Mesafe:5 cm")
                        i=b
                        Bcc=Bc/100


                        break


                    else:
                        print(f"{n} aralık için {((5 * n) + (b * n) + b)} ")




            else:
                print("Giriş Eşiği Yüksekliğini Yeniden Tayin Ediniz")
        else:
            print("Dalgıç Perdenin Suya Batan Yüksekliğini Yeniden Tayin Ediniz")




    break


Qmin=float(input("Lütfen Minimum Su Debisi Giriniz(m^3/sn):"))
Hc=float(input("Lütfen Çökeltim Havuzu Yüksekliğini Girinizi(m):"))
Qc=Qmin*(0.4+B/100)
Aiz=Bcc*Hc
Viz=Qc/Aiz

print(f"Izgara Debiniz:{Qc} m^3/sn,")
print(f"Izgara Hızının:{Viz} m^2/sn,")
print(f"Izgara Alanınız:{Aiz} m^2")

# Izgara Yük Kaybının Belirlenmesi
Be=float(input("Dalgıç Perde Tipinize Göre Katsayı Giriniz:"))
Dh=Be*(((5/Bcc)**1.333)*(Viz/19.62))
print(f"Izgara Yük Kaybı:{Dh}")
# Dalgıç Perde Yük Kaybı
Dhd=((Viz)**2)*0.0509
print(f"Dalgıç Perde Yük Kaybı{Dhd}")
# Toplam Su Yüksekliğinin Bulunması
E1=Hc+((Qc/(Bcc*Hc))**2)
E2=E1-Dh-Dhd-1
print(E2)

while(True):
    Hdd=random.uniform(0,8)
    if(((Hdd+((Qc/(Bcc*Hdd))**2))-0.1)<=E2<=((Hdd+((Qc/(Bcc*Hdd))**2))+0.1)):
        print(f"Su Yüksekliği:{Hdd}")
        break
    else:
        print(E2)
        print(f"{Hdd} İçin {(Hdd+((Qc/(Bcc*Hdd))**2))}")