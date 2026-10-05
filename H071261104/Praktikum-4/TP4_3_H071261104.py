# import time

# def hitung_mundur(angka):
#     print(angka)
#     if angka == 0:
#         print("Luncurkan!")
#         return
#     time.sleep(1)
#     hitung_mundur(angka - 1)

# while True:
#     try:
#         angka = int(input("Masukkan angka awal hitung mundur: "))
#         if angka < 0:
#             print("Input tidak valid, angka tidak boleh negatif.")
#         else:
#             hitung_mundur(angka)
#             break
#     except ValueError:
#         print("Input tidak valid, masukkan angka bulat.")













def hitung_mundur(angka):   

    print(angka)
    if angka > 0:
        hitung_mundur(angka - 1)
    else:
        print("Luncurkan")
    
     
while True:
    try:
        mundur = int(input("Masukkan angka awal hitung mundur: "))
        if mundur < 0:
            print("Input tidak valid, angka tidak boleh negatif")
            continue
    except:
        print ("Input harus angka")
    hitung_mundur(mundur)
        


            
