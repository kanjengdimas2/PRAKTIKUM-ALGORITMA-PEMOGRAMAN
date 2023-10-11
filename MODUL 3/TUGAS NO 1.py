ukuran = int(input("Masukkan Ukuran : "))
print(" ")

if ukuran < 5:
    print()
else:
    print("invalid")

#angka pertama
for i in range(ukuran):
        if i == 0 or i == ukuran-1:
            print("x" * ukuran)
        else:
            print("x" + " " *(ukuran-2) + "x")
print(" ")

#angka kedua
for j in range(ukuran):
    if j == 0 or j == ukuran-1 or j == ukuran//2 :
        print("x" * ukuran)
    else:
        print(" " * (ukuran-1)+ "x")
print(" ")

#angka ketiga
for n in range(ukuran):
    if n == 0 or n == ukuran-1 or n == ukuran//2 :
        print("x" * ukuran)
    elif n > 0 and n < ukuran//2:
        print("x")
    else:
        print(" " * (ukuran-1) + "x")
        