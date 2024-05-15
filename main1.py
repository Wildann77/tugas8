import tugas9 as db

while True :
   print('selamat datang di sini ')
   print('pilihan')
   print('1. Tambah data barang ')
   print('2. hapus data barang ')
   print('3. tampilkan data barang ')
   print('4. keluar')
   pilihan = int(input('masukan plihan ')) 
   if pilihan == 1:
      db.insert()
   elif pilihan == 2:
      db.hapus_data()
   elif pilihan == 3:
      db.view_data()
   elif pilihan == 4:
     print('terima kasih telah datang')
     break