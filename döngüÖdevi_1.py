"""Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""


sayi_ = int(input("Kontrol edilmesini istediğiniz sayıyı girin : "))
toplam=0
i= 1

for i in range (1,sayi_) :
    if(sayi_% i == 0) :
         toplam += (i)
if toplam == sayi_ :
     print("Girilen sayı mükemmel sayıdır.")
else:
    print("Girilen sayı mükemmel sayı değildir.")
