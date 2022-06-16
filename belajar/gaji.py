JK = float(input("Masukan Jumlah Kerja ="))
JL = float(input("Masukan Jumlah Lembur ="))
TH = float(input("Masukan Jumlah Tidak Hadir ="))

TJK = JK * 15.000
TJL = JL * 10.000
TTH = TH - 100.000
uangmakan = JK * 10.000
totalgaji = TJK + TJL - TTH

print("Total Gaji Anda =", totalgaji)
print("Uang Makan Anda =", uangmakan)