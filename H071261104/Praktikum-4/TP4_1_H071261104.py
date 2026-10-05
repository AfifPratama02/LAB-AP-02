

# def hitung_subtotal(harga, jumlah, member=False):
#     subtotal = harga * jumlah
#     if member:
#         subtotal *= 0.9
#     return int(subtotal)

# print("Selamat datang di Kasir Minimarket!")
# status_member = input("Apakah Anda member? (y/n): ").lower()
# ya = status_member == 'y'

# total_belanja = 0

# while True:
#     nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").lower()
#     if not nama_barang:
#         break
#     harga = int(input("Harga barang: "))
#     jumlah = int(input("Jumlah barang: "))
#     subtotal = hitung_subtotal(harga, jumlah, member=ya)
#     total_belanja += subtotal
#     print(f"Subtotal {nama_barang}: Rp{subtotal}")

# print(f"Total belanja: Rp{total_belanja}")























def hitung_subtotal(jumlah, harga, member = False):
    subtotal = harga * jumlah
    if member:
        subtotal *= 0.9
    return int(subtotal)

status = input("Apakah anda member? (y/n): ").lower()
total = 0
ya = status == 'y'

while True:
    nama = input("Masukkan nama barang (Kosongkan untuk selesai): ")
    if not nama:
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    subtotal = hitung_subtotal(jumlah, harga, member = ya)
    total += subtotal
    print("Subtotal", nama, ":", subtotal)


print("Total belanja: ", total)

    







