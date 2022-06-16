# Menu operasi
print("===BANGUN RUANG===")
print("1. Kubus")
print("2. Balok")
print("3. Bola")

# Meminta input dari user
pilih = int(input("Masukkan pilihan(1/2/3): "))

if pilih == 1:
    sisi = int(input("Masukan Panjang Sisi Kubus : "))
    volume = (6*sisi**2)
    luas = (sisi*sisi)*6
    print("Luas Kubus Adalah : ", volume, "\n", "keliling Kubus", luas)
elif pilih == 2:
    p = int(input("Masukan Panjang Balok : "))
    l = int(input("Masukan lebar Balok : "))
    t = int(input("Masukan Tinggi Balok : "))
    volume = (p * l * t)
    luas = (2 * p * l) + (2 * p * l) + (2 * p * l)
    print("Luas Balok Adalah : ", volume, "\n", "Keliling Balok Adalah : ", luas)
else:
    r = int(input("Masukan Jari-jari : "))
    luas = 4 * 3.14 * r ** 2
    print("Luas Bola Adalah : ", luas)