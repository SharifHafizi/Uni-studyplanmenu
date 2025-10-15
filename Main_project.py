# Simple Study Plan Program

# Lists to store course info
#from emne import lag_nytt_emne, legg_til_emne_i_studieplan
import emne
from emnelist import skriv_ut_alle_emner, skriv_ut_studieplan, sjekk_studieplan_gyldighet
from filehandling import lagre_til_fil, les_fra_fil



def hovedmeny():
    while True:
        print("\n--- MENY ---")
        print("1. Lag et nytt emne")
        print("2. Legg til et emne i studieplanen")
        print("3. Skriv ut alle registrerte emner")
        print("4. Skriv ut studieplanen")
        print("5. Sjekk om studieplanen er gyldig")
        print("6. Lagre til fil")
        print("7. Les fra fil")
        print("8. Avslutt")
        valg = input("Velg et tall (1-8): ")
        if valg == "1":
            emne.lag_nytt_emne()
        elif valg == "2":
            emne.legg_til_emne_i_studieplan()
        elif valg == "3":
            skriv_ut_alle_emner()
        elif valg == "4":
            skriv_ut_studieplan()
        elif valg == "5":
            sjekk_studieplan_gyldighet()
        elif valg == "6":
            lagre_til_fil()
        elif valg == "7":
            les_fra_fil()
        elif valg == "8":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg!")


if __name__ == "__main__":
    hovedmeny()
