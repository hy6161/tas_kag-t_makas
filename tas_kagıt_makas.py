import random
print("------tas kagıt makas-------")
com_point=0
plyr_point=0
while True:
    player=input("1-Taş\n2-Kağıt\n3-Makas\n4-sonuç\n")
    computer=random.choice(["1","2","3"])
    if player=="1":
        if computer=="1":
            print("bilgisayar taş seçti berabere")
        elif computer=="2":
            com_point+=1
            print("bilgisayar kağıt seçti bilgisayar kazandı")
        elif computer=="3":
            plyr_point+=1
            print("bilgisayar makas seçti Kazandınız")
    elif player=="2":
        if computer=="1":
            plyr_point+=1
            print("bilgisayar taş seçti Kazandınız")
        elif computer=="2":
            print("bilgisayar kağıt seçti berabere")
        elif computer=="3":
            com_point+=1
            print("bilgisayar makas seçti bilgisayar kazandı")
    elif player=="3":
        if computer=="1":
            com_point+=1
            print("bilgisayar taş seçti bilgisayar kazandı")
        elif computer=="2":
            plyr_point+=1
            print("bilgisayar kağıt seçti Kazandınız")
        elif computer=="3":
            print("bilgisayar makas seçti berabere")
    else:
        
        print("Sizin puanınız={}\nBilgisayarın puanı={}".format(plyr_point,com_point))
        break