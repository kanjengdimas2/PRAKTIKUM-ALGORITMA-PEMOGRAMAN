#luas permukaan kerucut
def luas_pkerucut(jarijari, garispelukis):
    luas_hkerucut = 22/7 * jarijari * (jarijari+garispelukis)
    return luas_hkerucut

#luas permukaan limas segilima
def luas_plimassegilima(sisi, alas, tinggi2):
    luas_alas = 1.72 * sisi*sisi
    luas_segitiga = 5*(1/2 * alas * tinggi2)
    luas_hlimassegilima = luas_alas + luas_segitiga
    return luas_hlimassegilima

#luas permukaan prisma segilima 
def luas_pprismasegilima(sisi2, tinggi3):
    lupersegi = sisi2 * tinggi3
    lusegiilima = 1.72 * sisi2 * sisi2
    luas_hprisma = 5*(lupersegi) + 2*(lusegiilima)
    return luas_hprisma

#inputan user
while True:
    print("1 = kerucut")
    print("2 = Limas")
    print("3 = Prisma")
    pilih = str(input("INGIN MENGERJAKAN YANG MANA (1/2/3): "))
    print(" ")
    if pilih == "1":
        jarijari = float(input("Masukan Nilai Jari-Jari nya : "))
        garispelukis = float(input("Masukan Nilai Garis Pelukis nya : "))
        hasil = luas_pkerucut(jarijari, garispelukis)
        print(f"jadi luas permukaan kerucut adalah {round(hasil)}")
    elif pilih == "2":
        sisi = float(input("Masukan Nilai Sisi Limas : "))
        alas = float(input("Masukan Nilai Alas Limas : "))
        tinggi2 = float(input("Masukan Nilai Tinggi Limas : "))
        hasil2 = luas_plimassegilima(sisi, alas, tinggi2)
        print(f"jadi luas permukaan limas segilima adalah {round(hasil2)}")
    elif pilih == "3":
        sisi2 = float(input("Masukan Nilai Sisi Prisma Segilima : "))
        tinggi3 = float(input("Masukan Nilai Tinggi Prisma segilima : "))
        hasil3 = luas_pprismasegilima(sisi2, tinggi3)
        print(f"jadi luas permukaan dari prisma segilima adalah {round(hasil3,2)}")
    else:
        print("Pilih antara 1 sampai 3")

    ulangi = str(input("Apakah ingin di ulangi? (iyah/tidak) ")).lower()
    if ulangi != "iyah":
        print(" ")
        break
            
