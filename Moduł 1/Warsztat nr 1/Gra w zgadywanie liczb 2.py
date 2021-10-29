print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach.")



min = 0
max = 1000



    

while True:

    guess = int((max-min) / 2) + min

    print("Zgaduję: ", guess)

    answer = input("Czy zgadłem? (za dużo, za mało, zgadłeś)")

    if answer == "zgadłeś":

        print("Wygrałem!")
        
        break

    if answer == "za dużo":

        max = guess

        continue
    
    if answer == "za mało":

        min = guess

        continue

    else:

        print("Nie oszukuj!")

        continue
