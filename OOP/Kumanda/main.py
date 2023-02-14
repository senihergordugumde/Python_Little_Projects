class Kumanda():
    def __init__(self,tvDurum = "Kapalı",tvSes = 0,tvKanal = "TRT",miktar = 0):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.tvKanal = tvKanal
        self.miktar = miktar
    def tvAc(self):
        self.tvDurum = "Açık"

    def sesArttir(self):
        self.miktar = int(input("Sesi ne kadar arttırmak istiyorsun? :  "))
        if (self.tvSes <= 99):
            self.tvSes += self.miktar
            print("Yeni ses seviyesi {}".format(self.tvSes))
        else:
            print("Ses seviyesi maximum")

    def sesAzalt(self):
        self.miktar = int(input("Sesi ne kadar azaltmak istiyorsun? :  "))
        if (self.tvSes > 0):
            self.tvSes -= self.miktar
            print("Yeni ses seviyesi {}".format(self.tvSes))
        else:
            print("Ses seviyesi minimum")

kumanda = Kumanda()

while kumanda.tvDurum == "Kapalı":
    print("TV Kapalı açmak için [1]'e basın")
    secim = int(input(""))
    if secim == 1:
        kumanda.tvAc()
    else:
        pass

while kumanda.tvDurum == "Açık":
    print("[1] Sesi Arttır"
          "[2] Sesi Azalt"
          "[3] Kanal Değiştir"
          "[4] TV'yi Kapat" )
    secim = int(input(""))
    if secim == 1:
        kumanda.sesArttir()
    elif secim == 2:
        kumanda.sesAzalt()
    elif secim == 3:
        pass


