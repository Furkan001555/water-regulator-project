"""
Hello I am the Developer of This Code
This Coding has been coded for Konya Technical University Civil Engineering Hydraulics Department.

This code was developed by Hüseyin Furkan YALVAÇ on 26.05.2022
Advisor: Cihangir KÖYCEĞİZ
"""


import random

Qmax5 = float(input("MAKSİMUM DEBİYİ GİRİNİZ:"))
Qort5 = float(input("ORTALAMA DEBİYİ GİRİNİZ:"))
Qmin5 = float(input("MİNİMUM DEBİYİ GİRİNİZ:"))
Hsav = float(input("LÜTFEN SAVAK YÜKSEKLİĞİNİ GİRİNİZ:"))
while True:

    pHo=round(random.uniform(0.01,3),2)

    if(pHo>2.75):
        Cmax=2.18
    else:
       Cmax = ((-0.0210) * (pHo ** 6)) + ((0.2148) * (pHo ** 5)) - ((0.915) * (pHo ** 4)) + ((1.982) * (pHo ** 3)) - (
                   (2.3081) * (pHo ** 2)) + ((1.414) * (pHo ** 1)) + (1.7719)  #Hocam Burada Denklemde Hata Olabilir Burayı Kontrol Etmekte Fayda Var


    Ho1=float(Hsav/pHo)
    Cmaxr=round(Cmax,2)
    Qmaxr=Cmaxr*Hsav*((Ho1)**1.5)
    if((Qmaxr-1)<=Qmax5<=(Qmaxr+1)):



        Hortma = round(random.uniform(0.01, 1.6), 2)
        Cortma = (0.3 * (Hortma ** 3)) - (0.14 * (Hortma ** 2)) + (0.32 * Hortma) + 0.79 #Hocam Yine Aynı Şekilde Denklemi Kontrol Ederdek Daha İyi Olabilir
        Hort = Hortma * Ho1
        Cort = Cortma * Cmaxr
        Qort = Cort * Hsav * (Hort ** 1.5)
        if ((Qort5 - 0.8) <= Qort <= (Qort5 + 0.8)):

            Hminma = round(random.uniform(0.01, 1), 2)
            Cminma = (0.3 * (Hminma ** 3)) - (0.14 * (Hminma ** 2)) + (
                    0.32 * Hminma) + 0.79  # Hocam Yine Aynı Şekilde Denklemi Kontrol Ederdek Daha İyi Olabilir
            Hmin = Hminma * Ho1
            Cmin = Cminma * Cmaxr
            Qmin = Cmin * Hsav * (Hmin ** 1.5)
            if ((Qmin5 - 0.8) <= Qmin <= (Qmin5 + 0.8)):#Hocam Bu kısımda Hassasiyeti Ayarlayabilriz Yine Yukarıdaki İf Komutlarıylada Ayarlayabiliriz Ama Hassasiyet Arttıkça Verileri Bulması Uzun Sürüyor

                print("LÜTFEN VERİLERİ DÜZELTİNİZ HASSAİYET OLDUĞUNDAN DÜZELTME YAPILMALIDIR")
                print(f"P/HO Değeriniz:{pHo} Seçıilmiştir.")
                print(f"Cmax Değeriniz:{Cmaxr}")
                print(f"Cort Değeriniz:{Cort}")
                print(f"Cmin Değeriniz:{Cmin}")
                print(f"Hmax Değeriniz:{Ho1}")
                print(f"Hort Değeriniz:{Hort}")
                print(f"Hmin Değeriniz:{Hmin}")
                print(f"Bulunan Maksimum Debi:{Qmaxr}")
                print(f"Bulunan Ortalama Debi:{Qort}")
                print(f"Bulunan Minimum Debi:{Qmin}")
                print(f"Maksimum Su Seviyesi:{Hsav+Ho1}")
                print(f"Ortalama Su Seviyesi:{Hsav + Hort}")
                print(f"Minimum Su Seviyesi:{Hsav + Hmin}")
                break

            else:
                print(f"Seçilen:{Qmin}")
                print(f"Verilen:{Qmin5}")
        else:
            print(f"Seçilen:{Qort}")
            print(f"Verilen:{Qort5}")

    else:
        print(f"Seçilen:{Qmaxr}")
        print(f"Verilen:{Qmax5}")
