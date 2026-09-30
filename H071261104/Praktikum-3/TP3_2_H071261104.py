

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))

        if baris <= 0:
            print("Jumlah baris harus lebih ari 0!")
            continue
        break
    except:
        print("input baris harus berupa angka")

while True:
    try:
        kursi = int(input("Masukkan jumlah kursi: "))

        if kursi <= 0:
            print("Jumlah kursi harus lebih ari 0!")
            continue
        break
    except:
        print("input kursi harus berupa angka")

for baris in range (1, baris+1):
    for kursi in range (1, kursi+1):
        if kursi == 13:
            continue
        if baris==1 and kursi%2 == 0:
            continue
        print("Baris", baris, "- Kursi", kursi)

