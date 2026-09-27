

nilai = int(input("Masukkan nilai tes: "))
if nilai >= 0 and nilai <= 100:
    if nilai >= 80:
        print("Lolos ke Tahap Wawancara")
    elif nilai >= 65:
        pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))
        
        if pengalaman >= 2:
            print ("Lolos Bersyarat")
        else:
            print("Tidak Lolos")
    else:
        print("Tidak Lolos")

else:
    print("Invalid")