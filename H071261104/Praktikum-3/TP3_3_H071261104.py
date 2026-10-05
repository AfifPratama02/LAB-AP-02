

while True:
    try:
        kursi = int(input("Masukkan maksimal kursi bus: "))

        if kursi <= 0:
            print("Input jumlah kursi harus lebih dari 0")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka")

pendapatan = 0

while kursi>0:
    umur = int(input("Masukkan umur penumpang: "))

    if umur < 0:
        print("Umur tidak valid")
        continue

    if umur <= 5:
        harga = 0
        print ("Kategori: Balita - Harga: Rp0")

    elif umur <= 12:
        harga = 50000
        print ("Kategori: Anak - Harga: Rp50.000")
    else:
        harga = 100000
        print ("Kategori: Dewasa - Harga: Rp100.000")

    pendapatan += harga
    kursi -= 1
    print("Sisa kursi:", kursi)

print("--- Semua kursi terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini:", pendapatan)

