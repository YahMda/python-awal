def konversi_nilai (nilai):
    if 85 <= nilai <= 100 :
        return 'A'
    elif 80 <= nilai < 85 :
        return 'AB'
    elif 75 <= nilai < 80 :
        return 'B'
    elif 70 <= nilai < 75 :
        return 'BC'
    elif 65 <= nilai < 70 :
        return 'C'
    elif 50 <= nilai < 65 :
        return 'D'
    else:
        return 'E'
    
nilai = int(input("masukan nilai 1 - 100 : "))
hasil = konversi_nilai(nilai)
print (f"anda mendapatkan nilai {hasil}")