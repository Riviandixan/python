# menghitung umt

# rumus imt (berat/tinggi**2)
# berat = float(input("berapa berat kamu?"))
# tinggi = float(input("berapa tinggi kamu?"))

# imt = berat/tinggi**2

# print("imt kamu adalah : ", imt)

berat = float(input("Berapa berat badan kamu?"))
tinggi = float(input("Berapa tinggi kamu?"))
imt = berat/tinggi**2

print("IMT kamu :" , imt)
if imt <= 16.9:
    print("Kurus")
elif imt >= 28.6:
    print("Gemuk")
else:
    print("Normal")




