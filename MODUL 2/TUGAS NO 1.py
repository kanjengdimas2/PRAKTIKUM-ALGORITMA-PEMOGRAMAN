umur = int(input("Masukkan Umur Anda : "))
print(" ")
if umur > 50:
    print("Anda Sudah Lanjut Usia")
elif umur > 25:
    print("Anda Sudah Dewasa")
elif umur > 17:     
    print("Anda Masih Muda")
elif umur > 7:
    print("Anda Masih Anak-anak")
elif umur >= 0:
    print("Anda masih Balita")
else:
    print("Umur Salah atau tidak valid")
