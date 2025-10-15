
from emne import emnekoder ,semester ,studiepoeng , studieplan

def skriv_ut_alle_emner():
    if not emnekoder:
        print("Ingen emner registrert.")
        return
    print("\nAlle registrerte emner:")
    for i in range(len(emnekoder)):
        print(f"{emnekoder[i]} - {semester[i]} - {studiepoeng[i]} sp")


def skriv_ut_studieplan():
    print("\nStudieplan:")
    for i in range(6):
        sem_type = "Høst" if i+1 in [1,3,5] else "Vår"
        print(f"Semester {i+1} ({sem_type}): {studieplan[i]} - total sp: {sum(studiepoeng[emnekoder.index(k)] for k in studieplan[i])}")


def sjekk_studieplan_gyldighet():
    gyldig = True
    for i in range(6):
        total = sum(studiepoeng[emnekoder.index(k)] for k in studieplan[i])
        if total != 30:
            gyldig = False
            print(f"Semester {i+1} har {total} sp - ikke gyldig!")
    if gyldig:
        print("Studieplanen er gyldig!")
