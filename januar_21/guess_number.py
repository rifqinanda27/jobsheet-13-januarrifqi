def guess_number():
    secret_number = 9
    guess_count = 0
    guess_limit = 3

    while(guess_count < guess_limit):
        number = int(input("Masukkan nomor "))
        if(number == secret_number):
            print(f"Guess: {number}")
            print("Benar")
            break
        else:
            print("Salah")
        guess_count +=1
    else:
        print("Kesempatan habis")

guess_number()