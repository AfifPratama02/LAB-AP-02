def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_valid = {'C', 'F', 'K'}

    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    if skala_asal == 'C':
        celsius = suhu
    elif skala_asal == 'F':
        celsius = (suhu - 32) * 5 / 9
    elif skala_asal == 'K':
        celsius = suhu - 273.15

    if skala_tujuan == 'C':
        return celsius
    elif skala_tujuan == 'F':
        return (celsius * 9 / 5) + 32
    elif skala_tujuan == 'K':
        return celsius + 273.15

print("=== Konversi Suhu ===")
while True:
    masukan_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip().lower()
    if masukan_suhu == 'selesai':
        break

    try:
        suhu = float(masukan_suhu)
        skala_asal = input("Skala asal (C/F/K): ").upper()
        skala_tujuan = input("Skala tujuan (C/F/K): ").upper()

        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {float(suhu)} {skala_asal} = {hasil} {skala_tujuan}")

    except ValueError as e:
        if str(e) == "Skala suhu tidak dikenali.":
            print(f"Error: {e}")
        else:
            print("Error: Input suhu harus berupa angka.")