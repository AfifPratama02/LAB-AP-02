
import re

nama_valid = []
def validasi(nama):
    pattern_nama = r"^[a-zA-Z]\w{5,12}"
    result_nama = re.match(pattern_nama, nama)
    if result_nama:
        nama_valid.append(nama)
        print ("Username tersedia.")
    else:
        print ("Username tidak valid!")
    return nama_valid

def rekap_data(data):
    nomor = 0
    if data:
        print("\n === Rekapitulasi === \n")
        print("Username Valid: ")
        for i in data:
            nomor += 1
            print (f"{nomor}. {i}")
        print(f"\nJumlah username valid: {nomor}")
    else:
        print ("Tidak ada username yang diinput")

print ("=== Registrasi Username ===")
print ("Ketik 'SELESAI' untuk mengakhiri")

while True:
    username = input("Masukkan username: ")
    if username == "SELESAI":
        break
    if username not in nama_valid:
        validasi(username)
    else:
        print("username sudah pernah diinput")

rekap_data(nama_valid)