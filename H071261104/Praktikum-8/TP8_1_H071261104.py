

import re

def validasi(nim, email, telepon):
    pattern_nim = r"^H071[0-9]{6,6}"
    result_nim = re.match(pattern_nim, nim) 
    if result_nim:
        result_nim = "Valid"
    else:
        result_nim = "Format NIM tidak valid"
    pattern_email = r"\w+@\w+.\w+"
    result_email = re.match(pattern_email, email)
    if result_email:
        result_email = "Valid"
    else:
        result_email = "Format email tidak valid"   
    pattern_telepon = r"[0-9]{10,13}$"
    pattern_pembersih_telepon = r"-|\s+"
    replace = ""
    result_pembersih = re.sub(pattern_pembersih_telepon, replace, telepon)
    result_telepon = re.match(pattern_telepon, result_pembersih)
    if result_telepon:
        result_telepon = "Valid"
    else:
        result_telepon = "Format telepon tidak valid"
    print("\n --- Hasil Validasi --- \n")
    print("NIM".ljust(15)+": "+result_nim)
    print("Email".ljust(15)+": "+result_email)    
    print("Telepon".ljust(15)+": "+result_telepon)    
    if result_nim == "Valid" and result_email == "Valid" and result_telepon == "Valid":
        print("Data mahasiswa berhasil diverifikasi!")
    else:
        print("Data mahasiswa gagal diverifikasi!")

print("\n === Validasi Data Mahasiswa === \n")
nim = input("Masukkan NIM".ljust(18) + ":")
email = input("Masukkan Email".ljust(18) + ":")
telepon = input("Masukkan No. Telp".ljust(18) + ":")

validasi(nim, email, telepon)



    