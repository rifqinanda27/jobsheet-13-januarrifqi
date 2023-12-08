weight = int(input("Masukkan Berat badan"))
types = input("Masukkan satuan Kg(K) atau Lbs(L)")

if (types == "K"):
    kg = weight * 0.453592
    print(f"Berat badan adalah {kg}K")
elif(types == "L"):
    lbs = weight * 2.204623
    print(f"Berat badan adalah {lbs}L")
