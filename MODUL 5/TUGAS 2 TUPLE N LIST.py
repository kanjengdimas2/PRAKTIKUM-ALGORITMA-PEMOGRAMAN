#inputan user
dataMahasiswa = []

jumlahdata = int(input(" Masukkan Jumlah data yang ada ingin di masukan! (minimal 5): "))

if jumlahdata < 5:
    print(" Minimal 5 Data ")
else:
    for i in range (jumlahdata):
        nim = int(input(f"masukan NIM mahasiswa ke-{i+1}: "))
        nama = str(input(f"masukan nama mahasiswa ke-{i+1}: "))
        alamat = str(input(f"masukan alamat mahsiswa ke-{i+1}: "))
        prodi = str(input(f"masukan prodi mahasiswa ke-{i+1}: "))
        data = (nim, nama, alamat, prodi)
        dataMahasiswa.append(data)

    #program pencarian
    pencarian = str(input("Masukkan Prodi Yang ingin Dicari : "))

    hasilpencarian = []

    for data in dataMahasiswa:
        if pencarian.lower() == data[3].lower():
            hasilpencarian.append(data)
    #output
    if len(hasilpencarian) > 0: 
        print(" Data mahasiswa yang ditemukan : ")
        for data in hasilpencarian:
            print(f"NIM: {data[0]}")
            print(f"nama: {data[1]}")
            print(f"alamat: {data[2]}")
            print(f"program studi: {data[3]}")
    else:
        print(f"tidak ditemukan mahasiswa dengan program studi: {pencarian}")