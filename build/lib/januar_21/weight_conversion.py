def weight_conversion():
    weight = int(input("Masukkan Berat badan"))
    types = input("Masukkan satuan Kg(K) atau Lbs(L)")

    if (types == "K" or types == 'k'):
        kg = weight * 0.453592
        print(f"Berat badan adalah {kg}K")
    elif(types == "L" or types == 'l'):
        lbs = weight * 2.204623
        print(f"Berat badan adalah {lbs}L")

weight_conversion()