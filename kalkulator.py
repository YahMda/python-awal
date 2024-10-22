import os 
def hapus_jejak_text():
    os.system("cls")
def menu():
    print ("pilih perhitunagan yang mau dijalankan")
    print ("1. penjumlahan ")
    print ("2. pengurangan ")
    print ("3. perkalian ")
    print ("4. pembagian ")
    print ("5. perpangkatan ")
    print ("0. keluar")
    
def penjumlahan (a,b):
    return a + b
def penguranagan (a,b):
    return a - b
def perkalian (a,b):
    return a * b
def pembagian (a,b):
    if b == 0:
        return "tidak dapat dibagi 0"
    return a / b
def perpangkatan (a,b):
    return a ** b
def kalkulator ():
    hapus_jejak_text()
    while True:
        menu()
        pilihan = input("tentukan jalan mana yang kamu pilih :")
        if pilihan == '0':
            hapus_jejak_text()
            print ("perjalanan anda tamat")
            break
        elif pilihan in ['1','2','3','4','5']:
            hapus_jejak_text()
            if pilihan == '1':
                print ("penjumlahan")
            if pilihan == '2':
                print ("pengurangan")
            if pilihan == '3':
                print ("perkalian")
            if pilihan == '4':
                print ("pembagian")
            if pilihan == '5':
                print ("perpangkatan")
            try:
                angka1 = float(input("masukan angka pertama: "))
                angka2 = float(input("masukan angka kedua: "))
                hapus_jejak_text()
            except ValueError:
                print ("masukan tidak valid, harap masukan angka yang benar.")
                continue

            if pilihan == '1':
                print (angka1, " + ", angka2, " = ", penjumlahan(angka1,angka2))
            if pilihan == '2':
                print (angka1, " - ", angka2, " = ", penguranagan(angka1,angka2))
            if pilihan == '3':
                print (angka1, " x ", angka2, " = ", perkalian(angka1,angka2))
            if pilihan == '4':
                print (angka1, " / ", angka2, " = ", pembagian(angka1,angka2))
            if pilihan == '5':
                print (angka1, " ^ ", angka2, " = ", perpangkatan(angka1,angka2))

            lanjut = input("apakah mau melanjukan perjalanan ini? (y/n):")
            if lanjut.lower() != 'y':
                hapus_jejak_text()
                print ("perjalanan telah tamat")
                break
            hapus_jejak_text()

#panggil perogram kalkulator 
kalkulator()