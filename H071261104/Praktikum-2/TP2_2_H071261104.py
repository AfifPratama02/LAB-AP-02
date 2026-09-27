

jarak = int(input("Masukkan jarak pengiriman (km): "))
if jarak > 0:
    express = input("Layanan express (ya/tidak): ")
    
    if jarak < 5 and jarak > 0:
        biaya = 10000
    elif jarak < 20:
        biaya = 20000
    else:
        biaya = 35000

    if express == "ya":
        layanan = 15000  
    else:
        layanan = 0

    tarif = biaya + layanan

    print("Total tarif pengiriman: Rp", tarif)
else:
    print ("Invalid")

