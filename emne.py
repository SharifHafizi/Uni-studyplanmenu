emnekoder = []
semester = []      # "Høst" or "Vår"
studiepoeng = []

# Study plan: 6 semesters, each is a list of course codes
studieplan = [[], [], [], [], [], []]


def lag_nytt_emne():
    kode = input("Skriv emnekode (f.eks. INF100): ").strip().upper()
    if kode in emnekoder:
        print("Emnet finnes allerede!")
        return
    sem = input("Skriv semester (Høst/Vår): ").strip().capitalize()
    if sem not in ["Høst", "Vår"]:
        print("Ugyldig semester!")
        return
    try:
        poeng = int(input("Skriv antall studiepoeng: "))
    except ValueError:
        print("Må være et tall!")
        return

    emnekoder.append(kode)
    semester.append(sem)
    studiepoeng.append(poeng)
    print(f"Emnet {kode} lagt til!")


def legg_til_emne_i_studieplan():
    if not emnekoder:
        print("Ingen emner registrert!")
        return
    kode = input("Hvilket emne vil du legge til? ").strip().upper()
    if kode not in emnekoder:
        print("Emnet finnes ikke!")
        return

    # Sjekk om emnet allerede er lagt til
    for sem in studieplan:
        if kode in sem:
            print("Emnet er allerede i studieplanen!")
            return

    try:
        semnr = int(input("Hvilket semester (1-6)? "))
    except ValueError:
        print("Ugyldig semester!")
        return
    if semnr < 1 or semnr > 6:
        print("Semester må være mellom 1 og 6.")
        return

    # Sjekk semester type
    idx = emnekoder.index(kode)
    emne_sem = semester[idx]
    if (emne_sem == "Høst" and semnr not in [1, 3, 5]) or \
       (emne_sem == "Vår" and semnr not in [2, 4, 6]):
        print(f"Feil semester! {kode} kan kun legges i {emne_sem}-semester.")
        return

    # Sjekk studiepoeng i semesteret
    total = sum(studiepoeng[emnekoder.index(k)] for k in studieplan[semnr-1])
    if total + studiepoeng[idx] > 30:
        print("Ikke plass i semesteret (maks 30 sp).")
        return

    studieplan[semnr-1].append(kode)
    print(f"{kode} lagt til i semester {semnr}!")