import sqlite3

con = sqlite3.connect("kutuphane.db") #varsa bağlanacak yoksa oluşturacak

cursor = con.cursor() #imleçi cursora atıyoruz.

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT, Yazar TEXT, Yayinevi TEXT, Sayfa INT)") #Tablo oluşturduk
    con.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES ('Hükümdar', 'Makyavel', 'İş Bankası', 331)")
    con.commit()

def veri_ekle2(isim, yazar, yayin_evi, sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES (?, ?, ?, ?)",(isim,yazar,yayin_evi,sayfa_sayisi ))
    con.commit()

isim = input("Kitap adı: ")
yazar = input("Yazar: ")
yayin_evi = input("Yayınevi: ")
sayfa_sayisi = int(input("Sayfa sayısı: "))
tablo_olustur()
veri_ekle()
veri_ekle2(isim,yazar,yayin_evi,sayfa_sayisi)
con.close() #bağlantıyı kapatıyoruz