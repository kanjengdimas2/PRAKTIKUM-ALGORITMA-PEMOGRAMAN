angka_awal = int(input("Masukkan Angka Awal : "))
angka_akhir = int(input("Masukkan Angka Akhir : "))

for i in range(angka_awal, angka_akhir+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)