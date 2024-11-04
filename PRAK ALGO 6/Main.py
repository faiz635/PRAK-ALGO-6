# def rata_rata():
#     jumlah = 0
#     hasil = 0
#     while True:
#         data = input('Masukan data :')
#         if data == "":
#             if jumlah == 0:
#                 return 0
#             return hasil / jumlah
            
#         elif data in ['A','A-','B+','B','B-','C+', 'C','D','E']:
#                 jumlah += 1
#                 if data == 'A':
#                  hasil += 4.00
#                  print('nilai = 4.00')
#                 elif data == 'A-':
#                  hasil += 3.75
#                  print('nilai=3.75')
#                 elif data == 'B+':
#                  hasil += 3.50
#                  print('nilai=3.50')
#                 elif data == 'B':
#                  hasil += 3.00
#                  print('nilai=3.00')
#                 elif data == 'B-':
#                  hasil += 2.75
#                  print('nilai=2.75')
#                 elif data == 'C+':
#                  hasil += 2.50
#                  print('nilai=2.50')
#                 elif data == 'C':
#                  hasil+= 2.00
#                  print('nilai=2.00')
#                 elif data == "C-":
#                  hasil += 1.75
#                  print("nilai = 1.75")
#                 elif data == "D":
#                  hasil += 1.50
#                  print("nilai = 1.50")
#                 elif data == "E":
#                  hasil += 1.25
#                  print("nilai = 1.25")
#                 else:
#                  print('Data Invalid')

# rata = rata_rata ()
# print("Rata Rata : ", rata)


def hitung_hari(bulan, tahun):
    bulan_dan_hari = {
        "Januari": 31, "Februari": 28, "Maret": 31, "April": 30,
        "Mei": 31, "Juni": 30, "Juli": 31, "Agustus": 31,
        "September": 30, "Oktober": 31, "November": 30, "Desember": 31}
    
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        bulan_dan_hari["Februari"] = 29 
    
    if bulan in bulan_dan_hari:
        return bulan_dan_hari[bulan]
    else: 
        return "Bulan tidak valid"
    
bulan = input("Masukkan nama bulan (contoh: Januari): ")
tahun = int(input("Masukkan tahun (contoh: 2024): "))

jumlah_hari = hitung_hari(bulan, tahun)
print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah: {jumlah_hari}")
