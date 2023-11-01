biodata = {
    "nama" : "SUSANTI",
    "alamat" : "SURAKARTA",
    "prodi" : "SISTEM INFORMASI",
    "semester" : "5",
    "angkatan" : "2015" 
}

for k, v, in biodata.items():
    print((k),":",(v))

ulang = 1
while ulang == 1:
    print("==============================================")
    print("=====      MASUKKAN TAHUN PERUBAHAN      =====")
    print("=====             2018 / 2019            =====")
    print("==============================================")
    perubahan = int(input("PIIHAN ANDA YANG MANA? : "))
    print(" ")

    if perubahan == 2018:
        alamat = str(input("Masukkan Alamat Pada Tahun 2018 : "))
        biodata["alamat"] = alamat
        prodi = str(input("Masukkan Prodi Pada Tahun 2018 : "))
        biodata["prodi"] = prodi
        print("==============================================")
        print("=== Data Susanti Setelah Perubahan di 2018 ===")
        print("==============================================")
        print(biodata)
        print(" ")
        print("==============================================")
        print("===    APAKAH INGIN MENGULANGI PROGRAM?    ===")
        print("===           1 : IYA / 2 : TIDAK          ===")
        print("==============================================")
        ulang = int(input("PILIHAN ANDA ? : "))
        if ulang != 1:
            print("=-=-=-= Program Selesai =-=-=-=")
    elif perubahan == 2019:
        del biodata["prodi"]
        del biodata["semester"]
        biodata["status"] = "Sudah Berhenti"
        print("==============================================")
        print("=== Data Susanti Setelah Perubahan di 2019 ===")
        print("==============================================")
        print(biodata)
        print(" ")
        print("==============================================")
        print("===    APAKAH INGIN MENGULANGI PROGRAM?    ===")
        print("===           1 : IYA / 2 : TIDAK          ===")
        print("==============================================")
        ulang = int(input("PILIHAN ANDA ? : "))
        if ulang != 1:
            print("=-=-=-= Program Selesai =-=-=-=")
    else:
        print("==============================================")
        print("===  MASUKKAN TAHUN PERUBAHAN YANG BENAR!  ===")
        print("==============================================")
        print(" ")
        print("==============================================")
        print("===    APAKAH INGIN MENGULANGI PROGRAM?    ===")
        print("===           1 : IYA / 2 : TIDAK          ===")
        print("==============================================")
        ulang = int(input("PILIHAN ANDA ? : "))
        if ulang != 1:
            print("=-=-=-= Program Selesai =-=-=-=")

        

