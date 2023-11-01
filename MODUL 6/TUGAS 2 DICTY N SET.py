ukm_pecintaalam = {"Bima", "Ari", "Dono", "Sinta", "Mira", "Akbar"}
ukm_bulutangkis = {"Dono","Sinta", "Gilang", "Dini", "Haidar", "Cecep"}
ukm_teater = {"Ari", "Mami", "Dika"}
ukm_taritradisional = {"Sinta", "Dika", "Budi", "Tri", "Raja", "Aidan"}

#menampilkan mahasiswa lebih dari satu UKM
hasil_ukm = set()
multi_ukm = [ukm_pecintaalam, ukm_bulutangkis , ukm_teater, ukm_taritradisional]
for i in multi_ukm:
    for j in multi_ukm:
        if i == j : 
            continue
        else:
            hasil_ukm.update(i&j)
print("==============================================================================")
print(f"Mahasiswa Yang bergabung dalam lebih dari satu UKM adalah{hasil_ukm}")
print("==============================================================================")
print(" ")

#menambah haidar ke dalam UKM pecinta alam
ukm_pecintaalam.add("Haidar")
print("==============================================================================")
print(f"Haidar Ikut ke dalam UKM pecinta alam {ukm_pecintaalam}")
print("==============================================================================")
print(" ")

#menghapus Dini dari UKM bulu tangkis 
tidak_ikut_UKM = []
ukm_bulutangkis.remove("Dini")
tidak_ikut_UKM.append("Dini")
print("==============================================================================")
print(f"Dini keluar dari UKM bulu tangkis {ukm_bulutangkis}")
print("==============================================================================")
print(" ")

#mencari ukm dari 4 
persatuan_ukm = {
    "BULU TANGKIS" : ukm_bulutangkis,
    "PECINTA ALAM" : ukm_pecintaalam,
    "TARI TRADISIONAL" : ukm_taritradisional,
    "TEATER" : ukm_teater,
}

ukm_kurangdari_4 = []
for a,b in persatuan_ukm.items():
    if len(b) < 4:
        ukm_kurangdari_4.append(b)
    else:
        continue

print("==============================================================================")
print("UKM dengan Anggota Kurang Dari 4 :", ukm_kurangdari_4)
print("==============================================================================")
print(" ")

# menampilkan mahasiswa yang tidak ikut UKM
kumpulan_UKM = (ukm_bulutangkis, ukm_pecintaalam, ukm_taritradisional, ukm_teater)
fix_tidakikut = set()
for d in kumpulan_UKM:
    for b in tidak_ikut_UKM:
        if b in d:
            continue
        else :
            fix_tidakikut.add(b)

print("==============================================================================")
print(f"Mahasiswa yang tidak ikut ukm {fix_tidakikut}")
print("==============================================================================")