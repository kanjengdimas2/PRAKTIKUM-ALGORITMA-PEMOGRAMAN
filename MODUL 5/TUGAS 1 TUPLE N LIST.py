#data makanan
makanan = []

jumlahdata = int(input(" Masukkan Jumlah data yang ada ingin di masukan! (minimal 5): "))

if jumlahdata < 5:
    print(" !! DATA MINIMAL 5 !!")
else:
    for i in range(jumlahdata):
        data_makanan = input(" Masukan Data Nama Makanan : ")
        makanan.append(data_makanan)

    print(" ")

    #data harga
    harga = []
    for j in range(jumlahdata):
        data_harga = int(input(" Masukan Data Harga Dari Setiap Makanan : Rp "))
        harga.append(data_harga)

    print(" ")

    #output
    for d in range(jumlahdata):
        print(f"Makanan: {makanan[d]}, Harga: Rp {harga[d]}")


