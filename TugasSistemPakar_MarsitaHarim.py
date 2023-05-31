def hitung_bilangan_positif(list):
    i = 0

    for angka in list:
        if angka > 0:
            i += 1

    return i

list_angka = []

while True:
    angka = int(input("Masukkan angka (masukan angka 0 jika ingin berhenti): "))
    if angka > 0:
        list_angka.append(angka)
    elif angka == 0:
        break

jumlah_bilpositif = hitung_bilangan_positif(list_angka)
print("Jumlah bilangan positif dalam list:", jumlah_bilpositif)
