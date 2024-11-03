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


hitung = 0 
jawab = 'ya'


while(jawab == 'ya'):
    bulan = int(input('Masukan Bulan : '))
    tahun = int(input('Masukan Tahun : '))
    jawab = str(input('Konfirmasi : '))



    def hitung_bulan():

         if(bulan == 1 or bulan == 3 or bulan ==5 
            or bulan == 7 or bulan == 8 or bulan == 10
            or bulan == 12):
              print('Hari = 31')


         elif(bulan >= 13 or bulan <=0):
              print('Data Invalid')


         elif (bulan == 2):
              
              if(tahun % 4 == 0 and bulan == 2):
                   print('Hari = 29')
                   return 
              
              else:
                   print('Hari = 28')

         else :
              print('Hari = 30')  


    hitung_bulan()   