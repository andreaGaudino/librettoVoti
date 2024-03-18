from voto import Libretto, Voto

lib = Libretto()

v1 = Voto("Analisi I", 10, 28, False, "2022-01-30")
lib.append(v1)

#lib.append(Voto("Fisica I", 10, 25, False, "2022-07-12"))
lib.append(Voto("Analisi II", 8, 30, True, "2022-02-15"))



voti25 = lib.findByPunteggio(25, False)
for v in voti25:
    print(v.esame)

try:
    votoAnalisiII = lib.findByEsame("Analisi III")
    print(f"Hai preso {votoAnalisiII.str_punteggio}")
except ValueError:
    print("Nessun voto trovato")


nuovo1 = Voto("Fisica I", 10, 25, False, "2022-07-12")
nuovo2 = Voto("Fisica II", 10, 21, False, "2022-07-12")
nuovo3 = Voto("Algebra e geometria lineare", 10, 20, False, "2022-06-12")
lib.append(nuovo1)
lib.append(nuovo2)
lib.append(nuovo3)

print("1)", lib.has_voto(nuovo1))
print("2)", lib.has_voto(nuovo2))
print("Libretto originario")
lib.stampa()
print("Libretto migliorato")
migliorato = lib.crea_migliorato()
migliorato.stampa()


