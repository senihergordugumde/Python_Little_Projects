class Calculator():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sonuc = 0
    def toplama(self):
        self.sonuc = self.x + self.y
        return self.sonuc
    def cıkarma(self):
        self.sonuc = self.x - self.y
        return self.sonuc
    def carpma(self):
        self.sonuc = self.x * self.y
        return self.sonuc
    def bolme(self):
        self.sonuc = self.x / self.y
        return self.sonuc

while True:
    print("[1] Toplama\n[2] Çıkarma\n[3] Çarpma\n[4] Bölme\n")
    islem = int(input("Bir İşlem Seçin: "))
    x = int(input("Birinci sayıyı giriniz: \n"))
    y = int(input("İkinci sayıyı giriniz: \n"))
    hesapMakinesi = Calculator(x, y)
    if islem == 1:
        print(hesapMakinesi.toplama())
    elif islem == 2:
        print(hesapMakinesi.cıkarma())
    elif islem == 3:
        print(hesapMakinesi.carpma())
    elif islem == 4:
        print(hesapMakinesi.bolme())


