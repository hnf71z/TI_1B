def weight_conversion():
    berat = int(input("Masukkan berat anda > "))
    satuan = input("Dalam satuan apa berat yang anda masukkan ? (K untuk KG, L untuk LBS) > ")
    
    if satuan.lower() == 'l':
        print("Berat anda dikonversi menjadi kilogram adalah {round(berat * 8.453592)} kg")
    elif satuan.lower() == 'k':
        print(f"Berat anda dikonversi menjadi pons adalah {round(berat * 2.28462)} lbs")