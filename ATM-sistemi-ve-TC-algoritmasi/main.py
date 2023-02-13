import random,time

def Tc(x):  #TC no'nun doğru olması için gereken şartları kontrol ediyoruz
    list(x)
    if x[0] == "0":
        return 0
    tek_rakamlar = int(x[0]) + int(x[2]) + int(x[4]) + int(x[6]) + int(x[8])
    cift_rakamlar = int(x[1]) + int(x[3]) + int(x[5]) + int(x[7])

    if int(x[9]) != (tek_rakamlar * 7 + cift_rakamlar * 9) % 10:
        return 0

    if (tek_rakamlar + cift_rakamlar + int(x[9])) % 10 != int(x[10]):
        return 0


while True:
    TC = str(input("TC No giriniz: "))
    isCorrect = Tc(TC)
    if isCorrect == False:
        print("TC Hatalı")
        continue
    if len(TC) != 11:
        print("TC 11 Haneli Olmalı")
        continue
    while True:
        sifre = str(input("4 haneli bir şifre oluşturun: "))
        if len(sifre) < 4:
            print("Şifre 4 haneden küçük olamaz!")
            continue
        elif len(sifre) > 4:
            print("Şifre 4 haneden büyük olamaz!")
            continue
        sifre_tekrar = str(input("Oluşturduğunuz şifreyi tekrar giriniz: "))
        if sifre != sifre_tekrar:
            print("Şifreler eşleşmiyor.")
            continue
        else:
          break
    break

bakiye = 5000

while True:
    islem_no = int(input("Bir işlem seçiniz:  \n[1] Para Yatır \n"
                                         "[2] Para Çek\n"))
    if islem_no == 1:
        print("...")
        time.sleep(1)
        print("Güncel bakiyeniz: {}".format(str(bakiye) + "TL"))
        yatir = int(input("Yatırmak istediğiniz tutar: "))
        print("Para yatırılıyor...")
        time.sleep(1)
        bakiye += yatir
        print("Yatırdığınız tutar: {}, Güncel bakiye: {}".format(yatir,bakiye))

        isOk = input("Başka bir işlem yapmak istiyor musunuz? E/H: ")
        if isOk == "E":
            continue
        elif isOk == "H":
            break

    elif islem_no == 2:
        print("...")
        time.sleep(1)
        print("Güncel bakiyeniz: {}".format(str(bakiye) + "TL"))
        cek = int(input("Çekmek istediğiniz tutar: "))
        print("Para çekiliyor...")
        time.sleep(1)
        bakiye -= cek
        print("Çektiğiniz tutar: {}, Güncel bakiye: {}".format(cek,bakiye))
        isOk = input("Başka bir işlem yapmak istiyor musunuz? E/H: ")
        if isOk == "E":
            continue
        elif isOk == "H":
            break

    else:
        print("Geçersiz giriş...")
        continue

