while True:
    tryb=input("Wybierz tryb - wpisz 'o' (odszyfrowanie) albo 's' (szyfrowanie): ")
    if tryb=='o' or tryb=='s':
        break
    else:
        print("Nieznany tryb! Wpisz 's' lub 'o'")

while True:
    kod_str=input("Podaj o ile chcesz przesunac znaki tekstu: ")
    if kod_str.isdigit():
        kod=int(kod_str)
        break
    else:
        print("Podaj cyfre!")


tekst=input("Podaj tekst: ")
wynik=""
for i in range(len(tekst)):
    znak=tekst[i]
    if tryb=='o':
        nowy_kod_ASCII=ord(znak)-kod
    else:
        nowy_kod_ASCII=ord(znak)+kod
    zaszyfrowany_znak=chr(nowy_kod_ASCII)
    wynik+=zaszyfrowany_znak
print(f"Wynik: {wynik}")