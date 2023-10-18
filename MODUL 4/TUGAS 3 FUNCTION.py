def pangkat(bilangan, pangkatnya):
    if pangkatnya == 0:
        return 1
    else:
        return bilangan * pangkat(bilangan, pangkatnya-1)
    
bilangan = int(input("MASUKKAN BILANGAN : "))
pangatknya = 2
hasil = pangkat(bilangan, pangatknya)

print(f"Hasil dari {bilangan} pangkat {pangatknya} adalah {hasil}")