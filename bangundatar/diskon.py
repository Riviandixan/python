# Menghitung Diskon
total = int(input("Masukan Total Belanja : "))

# kondisi
if total >= 1500000:
    diskon1 = total * (10/100)
    setelahDiskon = total - diskon1
    print("===Hitung Diskon===")
    print("Diskon yang di dapat yaitu : ", format(int(diskon1)))
    print("Harga setelah diskon : ", format(int(setelahDiskon)))
elif total >= 1000000:
    diskon2 = total * (5/100)
    setelahDiskon2 = total - diskon2
    print("Diskon yang di dapat yaitu : ", format(int(diskon2)))
    print("Harga setelah diskon : ", format(int(setelahDiskon2)))
elif total >= 500000:
    diskon3 = total * (2/100)
    setelahDiskon3 = total - diskon3
    print("Diskon yang di dapat yaitu : ", format(int(diskon3)))
    print("Harga setelah diskon : ", format(int(setelahDiskon3)))
else:
    print("Maaf Anda tidak memenuhi minimal belanja untuk dapat diskon ini!")