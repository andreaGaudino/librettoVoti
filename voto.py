from dataclasses import dataclass


@dataclass
class Voto:  #altro modo per definire le classi, crea già in automatico alcuni metodi come init e repr
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str


    def str_punteggio(self):
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"

class Libretto:
    def __init__(self):
        self._voti  =[]

    def append(self, voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            self._voti.append(voto)
        else:
            raise ValueError("Voto già presente")


    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto, coglione")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

    def findByPunteggio(self, punteggio, lode):
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi

    def findByEsame(self, esame):
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame '{esame}' non presente nel libretto")
    def has_voto(self, voto):
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        else:
            return False
    def has_conflitto(self, voto):
        for v in self._voti:
            if v.esame == voto.esame and(v.punteggio != voto.punteggio and v.lode != voto.lode):
                return True
        return False



""""def _test_voto():   #modo per testare le classi
    print(__name__)
    v1 = Voto("Munfao", 8, 21, False, "2024-02-29")
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())

if __name__ == "__main__":
    _test_voto()
"""