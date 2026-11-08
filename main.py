
while True:
    kod_str=input("Podaj o ile chcesz przesunac znaki tekstu: ")
    if kod_str.isdigit():
        kod=int(kod_str)
        break
    else:
        print("Podaj cyfre!")
haslo=input("Podaj tekst, ktory chcesz zaszyfrowac: ")
nowe_haslo=""
for i in range(len(haslo)):
    znak=haslo[i]
    zaszyfrowany_znak=chr(ord(znak)+kod)
    nowe_haslo+=zaszyfrowany_znak
print(f"Zaszyfrowane hasło: {nowe_haslo}")