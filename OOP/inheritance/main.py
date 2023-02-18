class Calısan(): #Class Oluşturduk

    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self): # Bu method çalışan sınıfının bilgilerini yazdıracak.

        print("Çalışan sınıfının bilgileri....")

        print(" İsim : {}\n Maaş : {}\n Departman : {}\n" .format(self.isim, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calısan):  #Yönetici classı Calısan Classının özelliklerini miras alıyor

    def __init__(self,isim, maas, departman, kisi_sayisi): #Fazladan bir özellik daha ekledik. Override etmiş olduk
        super().__init__(isim,maas,departman) # Tekrar aynı bilgileri yazmamak için super kullanıyoruz

        self.kisi_sayisi = kisi_sayisi
    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari


yonetici = Yonetici("Emir",5000,"IT",10)

yonetici.zam_yap(31)

yonetici.bilgilerigoster()
