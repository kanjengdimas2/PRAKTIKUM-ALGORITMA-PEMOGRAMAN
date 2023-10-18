def faktorial(bilangan):
    if bilangan == 0 :
        return 1
    else:
        return bilangan*faktorial(bilangan-1)
    
bilangan = int(input("MASUKAN BILANGAN : "))
hasil = faktorial(bilangan)


print(f"Hasil dari faktorial {bilangan} adalah {hasil}")