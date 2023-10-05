print("PERMAINAN KERTAS BATU GUNTING")
print(" ")
print("PILIH SALAH SATU!")
print(" ")

playersatu = input("Player 1 : Masukkan Pilihan (kertas/batu/gunting): ").lower()
playerdua = input("Player 2 : Masukkan Pilihan (kertas/batu/gunting: ").lower()

if playersatu == playerdua:
    print("PERMAINAN SERI!!")
elif playersatu == "kertas" and playerdua == "batu" : 
    print("PLAYER 1 MENANG!!")
elif playersatu == "kertas" and playerdua == "gunting" :
    print("PLAYER 2 MENANG!!")
elif playersatu == "batu" and playerdua == "gunting" : 
    print("PLAYER 1 MENANG!!")
elif playersatu == "batu" and playerdua == "kertas" :
    print("PLAYER 2 MENANG!!")
elif playersatu == "gunting" and playerdua == "kertas" :
    print("PLAYER 1 MENANG!!")
elif playersatu == "gunting" and playerdua == "batu" :
    print("PLAYER 2 MENANG!!")
else:
    print("Permainan Tidak valid")
    