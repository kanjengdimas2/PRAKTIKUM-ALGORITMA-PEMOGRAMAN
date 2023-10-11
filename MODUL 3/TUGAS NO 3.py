while True:
    waktupinjam = int(input("Berapa Hari anda meminjam buku : "))
    DendaHarian = 2000
    DendaMingguan = 5000
    Total = 0

    for i in range (1,waktupinjam+1)  :
        if i > 7 :
            Total += DendaHarian
            if i % 7 == 0 :
                Total += DendaMingguan
    if waktupinjam > 7 :
        print(f"Anda Meminjam buku lebih dari 1 Minggu Anda Terlambat Mengembalikan Buku selama {waktupinjam-7} Hari Dan Anda terkena Denda Sebesar Rp {Total} ")
        
    else :
        print(f"Anda Meminjam Buku Selama {waktupinjam} hari, Jadi Anda Tidak Terkena Denda!")

    ulangi = input("Apakah ingin mengulangi program? (ya/tidak): ")
    if ulangi.lower() != "ya":
        print("selesai")
        break
