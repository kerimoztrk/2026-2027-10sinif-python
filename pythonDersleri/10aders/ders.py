#Bu haftanın konusu değişken ve sabit tanımlama 


"""
Üç tane çift tırnak a rasına yorum sayırı coklu yorum satırı olarak yazılır
adadasasd
asdasdasd
"""

'''
3 tane tek tırnak arasına yorum sayırı coklu yorum satırı olarak yazılır
'''

# print("Hello World") #Bu satırın sonuna yorum eklenebilir
# print("Hello World")


# sayi= 5  # bu bir tamsayı (integer) değişkenidir.
# Sayi=1233

# print(sayi) # değişkenin değeri ekrana yazdırılır.

# sayi3= 5.0 # bu bir ondalıklı sayı (float) değişkenidir.

# ogrenci_no=1111
# ogrenciNo= 1111112312


# print(type(sayi))
# print(type(sayi3))


"""
12metin="metin" şeklinde bir değişken hatalı isimlendirilmiştir.
değişkenlerin başına herhangi bir sayi gelemez
degiskenler büyük küçük harf duyarlıdır. sayi=5 ile Sayi=5 aynı ifade değildir
programlama dilinde kullanılan özel karakterler kullanılamaz örneğin for class while if switch-case gibi ifadeler
değişkenin başına ve ortasına boşluk ifadesi konulamaz
ogrenci adi ="ali" şeklinde bir ifade hatalı değişken isimlendirmesidir.
"""


# metin = "Bu bir metin değişkenidir 1"
# Metin = "Bu da farklı bir değişkendir 2 "
# meTin = "Bu da farklı bir değişkendir 3"
# METİN= "Bu da farklı bir değişkendir 4 "

# print(METİN)


# #doğru isimlendirmeleri örnek olarak yazalım


# telefon="1234567890"

# _bilgisayar="bilgisayar değişkeni"

# mikrodalga123= "mikrodalga değişkeni"

# camasir-makinesi="çamaşır makinesi değişkeni"


#değişken isimlendirme alışkanları vardır

# sise-gecirilmis-et= 1  #kebap-case olarak adlandırılır. değişken isimlendirmede kelimeler arasına tire işareti konulmaz
# pazartesiGunuKahvaltisi= 1 #camelCase olarak adlandırılır. değişken isimlendirmede kelimeler arasına boşluk konulmaz ve kelimelerin ilk harfi büyük yazılır
# pazartesi_gunu_kahvaltisi= 1 #snake_case olarak adlandırılır. değişken isimlendirmede kelimeler arasına alt çizgi konulur
# Pazartesi_Gunu_Kahvaltisi= 1 #PascalCase olarak adlandırılır. değişken isimlendirmede kelimeler arasına boşluk konulmaz ve kelimelerin ilk harfi büyük yazılır
# PAZARTESİGUNUKAHVALTISI= 1 #UPPERCASE olarak adlandırılır. değişken isimlendirmede kelimeler arasına boşluk konulmaz ve kelimelerin tamamı büyük yazılır
# intOgrenciNumarası= 1 #HungarianCase olarak adlandırılır. değişken isimlendirmede kelimeler arasına boşluk konulmaz ve kelimelerin ilk harfi küçük yazılır ve değişkenin başına değişkenin tipini belirten bir ifade eklenir

# for =1234
# if=1234   # bunlar özel karakterler oldugu için bu isimle değişken tanımlanamaz
# None =1234


# yas = 25 #int veri tipindedir. sayısal veri türlerini ifade  eder

# sicaklık = 35.4 #float veri tipindedir. sayısal veri türlerini ifade  eder

# metin ="Bu bir metin değişkenidir" #str (string) veri tipindedir. metinsel veri türlerini ifade  eder

# pi= 3.14 # const (sabit) veri tipindedir. sayısal veri türlerini ifade  eder. pi sayısı matematikte sabit bir sayıdır ve değiştirilemez.

# print(type(yas))
# print(type(sicaklık))
# print(type(metin))
# print(type(pi))

#menu örneği

ana_yemek= "Adana Kebap"
tatli="sutlac"
icecek="ayran"

print("Günün MEnüsü")
print(f"1- Ana Yemek: {ana_yemek}")
print(f"2- Tatlı: {tatli}")
print(f"3- İçecek: {icecek}")