data = {}
while True:
    print("")
    g = input("(T)ambah, (U)bah, (H)apus, (L)ihat,(C)ari, (K)eluar: ")
    # Untuk keluar dari program
    if g.lower() == "k":
        print("Keluar dari program")
        break
    # untuk melihat list
    elif g.lower() == "l":
        if data.items():
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Data Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("======================================================================================")
            print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
            print("======================================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:4} | {0:13s} | {1:13} | {2:8d} |  {3:6d} | {4:7d} | {5:12.2f} | " \
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("======================================================================================")
                print("")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~Data Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("======================================================================================")
            print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
            print("======================================================================================")
            print("|                                 Tidak Ada Daftar Nilai                             |")
            print("======================================================================================")
    # Untuk menambahkan data
    elif g.lower() == "t":
        print("Tambah Data")
        nama = input("Nama          : ")
        nim = int(input("NIM           : "))
        tugas = int(input("Tugas         : "))
        uts = int(input("Nilai UTS     : "))
        uas = int(input("Nilai UAS     : "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
    # Untuk mengubah data
    elif g.lower() == "u":
        print("Edit Data Nilai Mahasiswa")
        nama = input(" Masukan Nama:")
        if nama in data.keys():
            nim = input("Nim               :")
            tugas = int(input("Nilai Tugas Baru  : "))
            uts = int(input("Nilai UTS Baru    : "))
            uas = int(input("Nilai UAS Baru    : "))
            nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
            data[nama] = nim, tugas, uts, uas, nilaiakhir
        else:
            print("Data nilai{0} tidak ada ".format(nama))
    # Untuk menghapus data
    elif g.lower() == "h":
        print("Hapus Data Nilai Mahasiswa")
        nama = input(" Masukan Nama:")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data {0} tidak ada".format(nama))
        # Untuk Mencari data
    elif g.lower() == "c":
        print("Cari Data Nilai Mahasiswa")
        nama = input(" Masukan Nama: ")
        if nama in data.keys():
            print("~~~~~~~~~~~~~~~~~~~~~~Data Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("==================================================================")
            print("~~~~~~~~~~~NAMA  NIM  TUGAS  UTS UAS NILAI AKHIR~~~~~~~~~~~~~~~~~~~")
            print("| {0} | {1} | ".format(nama, data[nama]))
            print("==================================================================")
        else:
            print("Datanya {0} tidak ada ".format(nama))
    else:
        print("\\~~~~~~~~~~~~~~~~~~~~~~~~~~~Data Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//")
        print("======================================================================================")
        print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        print("======================================================================================")
        print("|                                 Tidak Ada Daftar Nilai                             |")
        print("======================================================================================")

else:
    print("Pilih Menu Yang Tersedia")
