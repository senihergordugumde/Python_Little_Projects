import sqlite3
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()
class Kitaplik():
    def __init__(self,kitap_adi, yazar, yayinevi, sayfa):

        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.sayfa = sayfa

    def tablo_olustur(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Kitap TEXT, Yazar TEXT, Yayinevi TEXT, Sayfa INT)")
        con.commit()
    def kitap_ekle(self):
        cursor.execute("INSERT INTO kitaplik VALUES (?, ?, ?, ?)" ,(self.kitap_adi, self.yazar, self.yayinevi, self.sayfa))
        con.commit()


kitap_adi = input("Kitap adı: ")
yazar = input("Yazar: ")
yayinevi = input("Yayınevi: ")
sayfa = int(input("Sayfa sayısı: "))

kitaplik = Kitaplik(kitap_adi,yazar,yayinevi,sayfa)

kitaplik.tablo_olustur()
kitaplik.kitap_ekle()
