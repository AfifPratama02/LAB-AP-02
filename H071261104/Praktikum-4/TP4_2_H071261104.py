

def rekap_nilai(*args):
    if not args:
        return None
    rata_rata = sum(args)/len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if not masukan:
        break
    nilai = float(masukan) if '.' in masukan else int(masukan)
    daftar_nilai.append(nilai)

rekap_nilai(*daftar_nilai)

hasil = rekap_nilai(*daftar_nilai)

if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")


