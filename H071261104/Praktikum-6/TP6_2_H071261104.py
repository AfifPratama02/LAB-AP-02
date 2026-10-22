kandidat = set()
rekap_suara_nya = {}


def daftar_kandidat(kandidat_set, nama):
    if nama in kandidat_set:
        print(f"'{nama}' telah ada di dalam daftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Tidak ada kandidat dengan nama '{pilihan}'")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print(f"Suara berhasil diberikan kepada '{pilihan}'!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for nama in kandidat_set:
        perolehan[nama] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print()
    print("=================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("=================================")

    for nama, jumlah in sorted(perolehan.items()):
        print(f"   {nama}: {jumlah} suara")

    total_suara = sum(perolehan.values())
    print()
    print(f"Total suara masuk: {total_suara}")

    if not perolehan:
        print("Belum ada kandidat yang terdaftar.")
        return

    tertinggi = max(perolehan.values())

    
    nama_tertinggi = [
        nama for nama, jumlah in perolehan.items()
        if jumlah == tertinggi
    ]

    if len(nama_tertinggi) > 1:
        print("Hasil seri dan perlu pemilihan ulang!")
    else:
        pemenang = nama_tertinggi[0]
        print(f"PEMENANG: {pemenang} dengan {tertinggi} suara!")


print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")

# FASE PENDAFTARAN KANDIDAT
while True:
    nama_kandidat = input(
        "Masukkan nama kandidat (kosongkan untuk selesai): "
    ).strip().title()

    if nama_kandidat == "":
        print()
        break

    daftar_kandidat(kandidat, nama_kandidat)

if len(kandidat) < 2:
    print("Minimal ada 2 kandidat untuk melanjutkan.")

else:
    print(f"Kandidat terdaftar: {sorted(kandidat)}")
    print()
    print("--- FASE PEMUNGUTAN SUARA ---")

   
    while True:
        print()
        nama_pemilih = input(
            "Nama pemilih (kosongkan untuk selesai): "
        ).strip().title()

        if nama_pemilih == "":
            break

        if nama_pemilih in rekap_suara_nya:
            print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
            continue

        print(f"Kandidat yang tersedia: {sorted(kandidat)}")

        pilih_kandidat = input("Pilih kandidat: ").strip().title()

        if pilih_kandidat == "":
            print("Nama kandidat tidak boleh kosong.")
            continue

        berikan_suara(
            rekap_suara_nya,
            kandidat,
            nama_pemilih,
            pilih_kandidat
        )


    perolehan = hitung_suara(rekap_suara_nya, kandidat)
    tampilkan_hasil(perolehan)