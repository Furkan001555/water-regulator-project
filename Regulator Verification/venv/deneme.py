
Pkay=1
Pkor=5
if(0.4<=Pkay/Pkor):
    A=Pkay/(Pkor+(1*1*1*7))
    if(0.4<=A):
        print("Yapı Kaymaya Göre Güvensizdir")
    else:
        print("Yapı Kaymaya Karşı Güvenlidir")
else:
    print("Yapı Kaymaya Karşı Güvenlidir")