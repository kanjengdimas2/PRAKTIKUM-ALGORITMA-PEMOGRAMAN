nama = input("Masukkan Nama Mahasiswa : ")
nilaitugas = float(input("Masukkan Nilai Tugas : "))
nilaiuts = float(input("Masukkan Nilai UTS : "))
nilaiuas = float(input("Masukkan Nilai UAS : "))
tugasakhir = float(input("Masukkan Nilai Tugas Akhir : "))

ratarata = (nilaitugas + nilaiuts + nilaiuas + tugasakhir) / 4

if not (0 <= nilaitugas <= 100):
    print("Input nilai harus berada antara 0 hingga 100.")
elif not (0 <= nilaiuts <= 100):
    print("Input nilai harus berada antara 0 hingga 100.")
elif not (0 <= nilaiuas <= 100):
    print("Input nilai harus berada antara 0 hingga 100.")
elif not (0 <= tugasakhir <= 100):
    print("Input nilai harus berada antara 0 hingga 100.")
else:
    ratarata
     

if 80 <= ratarata <= 100:
    nilai_huruf = "A"
elif 70 <= ratarata < 80:
    nilai_huruf = "B"
elif 60 <= ratarata < 70:
    nilai_huruf = "C"
elif 40 <= ratarata < 60:
    nilai_huruf = "D"
elif 0 <= ratarata < 40:
    nilai_huruf = "E"
else:
    nilai_huruf = "nilai tidak valid"

print(nama)
print("Nilai Rata Rata Anda Di Semester Ini : ", ratarata)
print(nilai_huruf)
