# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 30 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 16 -> 5, 65 -> 44 , 78 -> 67, 72 -> 61
# -- sarkanas kāpnes ved uz augšu, 13 -> 22, 37 -> 46, 31 -> 50, 85 -> 94 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


round = 0
player1 = 1
player2 = 1
import random

while True:
    print("\nCirks:")
    print("1. Mest kauliņu.")
    print("2. Apstīties raundu.")
    print("3. Es negribu vairs spēlēt, iziet.")
    choice = input("Ivadiet jūsu izvēli (1-3): ")

    if choice == '1':
        round = round + 1# - Katru reizi kad kauliņš tiek mests, tiek skaitīts raunds

        print(" ")# - Print šeit ir domāts, lai teksts nebūtu "pilipis" cits pie cita
        dice = random.randint(1, 6)# - Izvēlās random skaitli no 1 līdz 6
        player1 = player1 + dice# - Pieskaita random skaitli pie spēlētāja 
        
        if player1 == 16:# - Zilās kāpnes, ja spēlētājs uzskāps uz vienu no šim kāpnēm, tad viņš ies uz leju
            player1 = 5
            print("Pirmais spēlētajs no 16 pozīcijas nojiet uz leju līdz 5")
        elif player1 == 65:
            player1 = 44
            print("Pirmais spēlētajs no 65 pozīcijas nojiet uz leju līdz 44")
        elif player1 == 78:
            player1 = 67
            print("Pirmais spēlētajs no 78 pozīcijas nojiet uz leju līdz 67")
        elif player1 == 72:
            player1 = 61
            print("Pirmais spēlētajs no 72 pozīcijas nojiet uz leju līdz 61")

        elif player1 == 13:# - Sarkanās kāpnes, ja spēlētajs uzskāps uz vienu no šīm kāpnēm tad viņš ies uz augšu
            player1 = 22
            print("Pirmais spēlētajs no 13 pozīcijas uziet uz augšu līdz 22")
        elif player1 == 37:
            player1 = 46
            print("Pirmais spēlētajs no 37 pozīcijas uziet uz augšu līdz 46")
        elif player1 == 31:
            player1 == 50
            print("Pirmais spēlētajs no 31 pozīcijas uziet uz augšu līdz 50")
        elif player1 == 85:
            player1 = 94
            print("Pirmais spēlētajs no 85 pozīcijas uziet uz augšu līdz 94")
        print("Pirmais spēlētājs pagāja uz priekšu pa", dice, ", spēlētājs 1 atrodas pozīcijā", player1)# - Tiek printēta spēlētāja gājiens un pozīcija
        print(" ")# - Print šeit ir domāts, lai teksts nebūtu "pilipis" cits pie cita
        if player1 >= 100:# - Ja spēlētājs tiek līdz 100 vai lielākam skaitlim tad tas automātiski uzvar
            print("Pirmais spēlētajs ir UZVARĒJIS!!!")
            break

        dice = random.randint(1, 6)
        player2 = player2 + dice
        if player2 == 16:# - Zilās kāpnes, ja spēlētājs uzskāps uz vienu no šim kāpnēm, tad viņš ies uz leju
            player2 = 5
            print("Otrais spēlētajs no 16 pozīcijas nojiet uz leju līdz 5")
        elif player2 == 65:
            player2 = 44
            print("Otrais spēlētajs no 65 pozīcijas nojiet uz leju līdz 44")
        elif player2 == 78:
            player2 = 67
            print("Otrais spēlētajs no 78 pozīcijas nojiet uz leju līdz 67")
        elif player2 == 72:
            player2 = 61
            print("Otrais spēlētajs no 72 pozīcijas nojiet uz leju līdz 61")

        elif player2 == 13:# - Sarkanās kāpnes, ja spēlētajs uzskāps uz vienu no šīm kāpnēm tad viņš ies uz augšu
            player2 = 22
            print("Otrais spēlētajs no 13 pozīcijas uziet uz augšu līdz 22")
        elif player2 == 37:
            player2 = 46
            print("Otrais spēlētajs no 37 pozīcijas uziet uz augšu līdz 46")
        elif player2 == 31:
            player2 == 50
            print("Otrais spēlētajs no 31 pozīcijas uziet uz augšu līdz 50")
        elif player2 == 85:
            player2 = 94
            print("Otrais spēlētajs no 85 pozīcijas uziet uz augšu līdz 94")
        print("Otrais spēlētājs pagāja uz priekšu pa", dice, ", spēlētājs 1 atrodas pozīcijā", player2)# - Tiek printēta spēlētāja gājiens un pozīcija
        if player2 >= 100:# - Ja spēlētājs tiek līdz 100 vai lielākam skaitlim tad tas automātiski uzvar
            print("Otrais spēlētajs ir UZVARĒJIS!!!")
            break
        
        if round == 30:# - Ja raunds ir vienāds 30 tad printē neizšķlirts
            print(" ")
            print("Jūs tikāt līdz 30 raundam, NEIZŠĶIRTS!!!")
            break

        pass
    elif choice == '2':
        print("Raunds ir", round)# - Printē kurš tagad raunds
        pass
    elif choice == '3':
        print(" ")
        print("Iziet no spēles, paldies ka esi spēlējis.")
        break
    else:
        print(" ")
        print("Nepareiza izvēle, lūdzu izvēlaties opciju no 1 līdz 3.")
