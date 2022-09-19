"""
Hello I am the Developer of This Code
First of all, we need to open a separate txt file for the x and y values between them and their names should be xdeg.txt and ydeg.txt.
Please enter your school number for this project Usage.
In this coding, there is a field with the Cross Method.
It is found in the environment with this code
This code was developed by Hüseyin Furkan Yalvaç on 05.04.2022
"""
def alanbul(A):
    try:
        if (len(A) == 9 or A == int()):
            ax = open("xdeg.txt", "r", encoding='utf-8')
            bx = ax.readlines()
            cx = bx[0]
            dx = cx.split(",")
            ay = open("ydeg.txt", "r", encoding='utf-8')
            by = ay.readlines()
            cy = by[0]
            dy = cy.split(",")
            B = int(A[-2])
            C = int(A[1])
            D = 0.9 + B / 100
            E = 0.8 + C / 100
            x = 0
            xx = 0
            yy = 0
            y = 0
            ex = []
            ey = []
            exx = []
            eyy = []
            for i in range(len(dx)):
                zx = dx[x]
                x = x + 1
                ex.append(zx)
            ex = list(map(float, ex))
            for i in range(len(dx)):
                sx = ex[xx] * D
                xx = xx + 1
                exx.append(sx)
            for i in range(len(dy)):
                zy = dy[y]
                y = y + 1
                ey.append(zy)
            ey = list(map(float, ey))
            for i in range(len(dy)):
                sy = ey[yy] * E
                yy = yy + 1
                eyy.append(sy)
            yekle = eyy[0]
            yeklee = eyy[1]
            eyy.append(yekle)
            eyy.append(yeklee)
            ALAN = []
            p = 0
            dr = 1
            rd = 2
            for i in range(len(eyy) - 2):
                alan = exx[p] * (eyy[dr] + eyy[rd])
                p = p + 1
                dr = dr + 1
                rd = rd + 1
                ALAN.append(alan)
            al = float(sum(ALAN))
            print(f"ALAN:{al} Metrekare")

    except FileNotFoundError:
        print("DOSYA BULANAMADI")

def islak(A):
    try:
        if (len(A) == 9 or A == int()):
            ax = open("xdeg.txt", "r", encoding='utf-8')
            bx = ax.readlines()
            cx = bx[0]
            dx = cx.split(",")
            ay = open("ydeg.txt", "r", encoding='utf-8')
            by = ay.readlines()
            cy = by[0]
            dy = cy.split(",")
            B = int(A[-2])
            C = int(A[1]) 
            D = 0.9 + B / 100
            E = 0.8 + C / 100
            x = 0
            xx = 0
            yy = 0
            y = 0
            ex = []
            ey = []
            exx = []
            eyy = []
            for i in range(len(dx)):
                zx = dx[x]
                x = x + 1
                ex.append(zx)
            ex = list(map(float, ex))
            for i in range(len(dx)):
                sx = ex[xx] * D
                xx = xx + 1
                exx.append(sx)
            for i in range(len(dy)):
                zy = dy[y]
                y = y + 1
                ey.append(zy)
            ey = list(map(float, ey))
            for i in range(len(dy)):
                sy = ey[yy] * E
                yy = yy + 1
                eyy.append(sy)

            islx=0
            islxx=1
            islyy=1
            isly=0
            ay=[]
            ax=[]
            for i in range(len(dy)-1):
                a=abs(eyy[isly]-eyy[islyy])
                islyy=islyy+1
                isly=isly+1
                ay.append(a)

            for i in range(len(dy)-1):
                b=abs(exx[islx]-exx[islxx])
                islxx=islxx+1
                islx=islx+1
                ax.append(b)

            sx=0
            sy=0
            C=[]
            for i in range(len(ax)):
                c=((ax[sx]**2)+(ay[sy]**2))
                sy=sy+1
                sx=sx+1
                C.append(c)
            cz=(((ax[0]-ax[-1])**2)+((ay[0]-ay[-1])**2))

            islakcevre=float(sum(C)-cz)
            print(f"ISLAK ÇEVRE:{islakcevre} metre")




    except FileNotFoundError:
        print("DOSYA BULUNAMADI")



A = input("Lütfen Öğrenci Numaranızı Giriniz:")

B = int(A[-2])  # Öğrenci Numarasının 8.Hanesini Alır.
C = int(A[1])
if (len(A) == 9 or A == int()):
    manpu = float(input("MANİNG PÜRÜZLÜLÜK KATSAYISINI GİRİNİZ:"))
    hidreg=float(input("HİDROLİK EĞİMİ GİRİNİZ:"))
    dane=float(input("Çökeltmek İstediğinz Dane Çapını Santimetre Cinsinden Giriniz:"))
    ozgagr = float(input("Dane Özgül Ağırlığını Giriniz:"))
    danerev=dane*0.01

    B = int(A[-2])  # Öğrenci Numarasının 8.Hanesini Alır.
    C = int(A[1])  # Öğrenci Numarasının 2.Hanesini Alır.
    print(f"X Katsayınız: 0.9{B}")
    print(f"Y Katsayınız: 0.8{C}")
    isl = islak(A)
    alan = alanbul(A)
    Q=(1/manpu)*((hidreg)**0.5)
    print(Q)