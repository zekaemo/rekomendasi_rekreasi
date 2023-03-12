print('REKOMENDASI REKREASI MAHASISWA TEKNIK KOMPUTER')

print ('Silahkan masukkan data diri anda!')
class maba:
    nama=input('Masukkan nama anda:')
    asal=input('Dimana asal anda? (provinsi) ')
    kos=input('Dimana area Seamarang mana kos anda berada? (atas atau bawah) ')
    angkatan=input('Tahun berapa anda bergabung di Teknik Komputer? ')

print(maba.nama.capitalize() + ' berasal dari ' + maba.asal.capitalize() + ' angkatan ' + maba.angkatan)

print("Selamat datang " + maba.nama.capitalize())

print ("Ada yang bisa kami bantu? ")
print("\n1 - Tempat wisata di daerah anda\t2 - Tempat makan sekitar anda")
selectmenu = int(input("\nSilahkan pilih menu: "))

import webbrowser

if selectmenu == 1:
    if maba.asal == 'jateng':
        webbrowser.open('https://www.tripadvisor.co.id/Attractions-g2301793-Activities-c57-Central_Java_Java.html')
    elif maba.asal == 'jabar':
        webbrowser.open('https://www.detik.com/jabar/wisata/d-6176779/25-tempat-wisata-di-jawa-barat-paling-terbaik')
    elif maba.asal == 'jatim':
        webbrowser.open('https://www.gotravelly.com/blog/tempat-wisata-di-jawa-timur/')
    

elif selectmenu == 2:
    if maba.kos == 'atas':
        webbrowser.open('https://www.idntimes.com/food/dining-guide/intan-deviana-safitri-1/kuliner-enak-di-sekitar-kampus-undip-tembalang')
    elif maba.kos == 'bawah':
        webbrowser.open('https://www.anekawisata.com/kuliner-simpang-lima-semarang.html')

else:
    print("Error. Maaf, menu tidak tersedia")

