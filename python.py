# 1. Gör ett valfritt program som suddar skärmen med os.system(‘cls’) vid flera tillfällen. Du kan även uppdatera ett gammalt program
# from msvcrt import getwch, kbhit
# import os
# import time


# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def get_user_input():
#     start_time = time.time()

#     input_text = input("Skriv in något nedan ! Du har 5 sekunder på dig : ")
#     input_text = " "
    
#     while True:
#         if kbhit():
#             char = getwch()
#             if char == '\r':  # Enter-tangenten
#                 break
#             input_text += char

#         current_time = time.time()
#         elapsed_time = current_time - start_time

#         if elapsed_time >= 5:
#             break

#     return input_text

# def main():
#         while True:
#             print("Skriv in något nedan inom 5 sekunder:")
#             clear_screen()
#             GG = get_user_input()
#             if GG:
#                 print("Congrats! Du hann skriva in:", GG, "inom 5 sekunder")
#             else:
#                 print("Tyvärr, du hann inte att skriva in något inom 5 sekunder")

#             time.sleep(5)

# if __name__ == "__main__":
#     main()



# 2. Använd sleep()-kommandot i valfritt projekt och spara som nytt filnamn sleep() används när du vill att programmet väntar innan det fortsätter
# import time

# def main():
#     print("Programmet startar .")
#     IN = input("Skriv in något: ")
#     print("Tack!")

#     # Använd sleep() för att vänta i 5 sekunder
#     time.sleep(5)
    
#     print("Programmet har väntat i 5 sekunder och fortsätter nu.")
#     print("Tack för att du väntade")

# if __name__ == "__main__":
#     main()

# time.sleep(2 * 60)  # 2 minuter till sekunder 


# 3. Gör ett välkomstprogram som väntar på en knapptryckning (utan ENTER) innan det avslutas - getwch()
# import msvcrt

# def main():
#     print("Välkommen! Tryck på på vilken knapp som helst nedan (utan att trycka ENTER) för att avsluta.")
    
#     key = msvcrt.getwch()
    
#     print(f"Du tryckte på: {key}")
#     print("Programmet avslutas")

# if __name__ == "__main__":
#     main()


# 4. Gör en modul som ändrar färg (kolla flödet här på CR)
# from colors import bcolors
# print("Här kan du se alla fäger")

# print(bcolors.GREEN + "\n Green")

# print(bcolors.YELLOW + "\n Yellow")

# print(bcolors.BLUE + "\n Blue")

# print(bcolors.CYAN + "\n Cyan")

# print(bcolors.PURPLE + "\n Purple")


# 5. Skapa ett färgstarkt program som använder färg samt något mer du lärt dig
from colors import bcolors

# print(bcolors.BOLD + "Y-Yellow , G-Green , B-Blue , C-Cyan , P-Purple ")
# Color = input("Skriv in vilken färg du vill se (välj en av de 5 färgarna ovan): ")

# if Color == "G" :
#     print(bcolors.GREEN + "Green")
# if Color == "Y" :
#     print(bcolors.YELLOW + "Yellow")
# if Color == "C" :
#     print(bcolors.CYAN + "Cyan")
# if Color == "P" :
#     print(bcolors.PURPLE + "Purple")
# elif Color == "B" :
#     print(bcolors.BLUE + "Blue")

# else:
#     print("Man får bara skriva in Y , G , C , P och B. Var snäll och strata om programmet")

# 6. Uppdatera gärna något annat gammalt program med getwch() och färger!
import msvcrt


def main():
    print("Tryck på en tangent: ", end='')

key = msvcrt.getwch()
    
print( bcolors.GREEN + f"\nDu tryckte på tangenten: {key}  - Bra val!" )

if __name__ == "__main__":
    main()


