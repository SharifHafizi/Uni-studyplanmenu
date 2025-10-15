from emne import emnekoder,semester, studiepoeng , studieplan
def lagre_til_fil():
    with open("data.txt", "w") as f:
        f.write(";".join(emnekoder) + "\n")
        f.write(";".join(semester) + "\n")
        f.write(";".join(str(sp) for sp in studiepoeng) + "\n")
        for sem in studieplan:
            f.write(";".join(sem) + "\n")
    print("Data lagret til data.txt!")


def les_fra_fil():
    global emnekoder, semester, studiepoeng, studieplan
    try:
        with open("data.txt", "r") as f:
            lines = f.read().splitlines()
            emnekoder = lines[0].split(";") if lines[0] else []
            semester = lines[1].split(";") if lines[1] else []
            studiepoeng = [int(x) for x in lines[2].split(";")] if lines[2] else []
            studieplan = [line.split(";") if line else [] for line in lines[3:9]]
        print("Data lest fra data.txt!")
    except FileNotFoundError:
        print("Filen finnes ikke!")
