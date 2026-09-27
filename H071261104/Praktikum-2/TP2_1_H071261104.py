

level = int(input("Masukkan persentase cabai: "))

if level >= 0 and level <= 10:
    print ("Level Aman")
elif level >= 11 and level <= 40:
    print ("Level Sedang")
elif level >= 41 and level <= 70:
    print ("Level Pedas")
elif level >=71 and level <= 100:
    print ("Level Ekstrem")
else:
    print("Invalid")
    