import operator
from dataclasses import dataclass
import copy


@dataclass
class Voto:  #altro modo per definire le classi, crea già in automatico alcuni metodi come init e repr
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str


    def str_punteggio(self):
        if self.punteggio == 30 and self.lode:
            return f"{self.esame} con voto 30 e lode"
        else:
            return f"{self.esame} ({self.cfu} cfu): {self.punteggio}"


def estrai_campo_esame(voto):
    return voto.esame

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
        somma = 0
        somma_crediti = 0
        for v in self._voti:
            somma += v.punteggio*v.cfu
            somma_crediti += v.cfu
        #punteggi = [v.punteggio for v in self._voti]
        return round(somma/somma_crediti, 2)

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
    def crea_migliorato(self):
        #migliora i voti presenti
        nuovo = Libretto()
        nuovo._voti = copy.deepcopy(self._voti)
        #nuovo._voti = []
        """for v in self._voti:
            nuovo._voti.append(Voto(v.esame, v.cfu, v.punteggio, v.lode, v.data))
        """

        for v in nuovo._voti:
            if 18<=v.punteggio<=23:
                v.punteggio+=1
            elif 24<=v.punteggio<=28:
                v.punteggio +=2
            elif v.punteggio==29:
                v.punteggio = 30
        return nuovo


    def stampa(self):
        print(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            print(v.str_punteggio())
        print(f"La media vale {self.media()}")
    def crea_ordinato_per_esame(self):
        nuovo = copy.deepcopy(self)
        return nuovo

    def ordina_per_esame(self):
        #self._voti.sort(key=estrai_campo_esame())

        self._voti.sort(key=operator.attrgetter("esame"))

    def crea_ordinato_per_punteggio(self):
        nuovo = copy.deepcopy(self)
        self._voti.sort(key=lambda v:(v.punteggio, v.lode), reverse=True)
        return nuovo

    def cancella_inferiori(self, punteggio):
        voti_nuovi = []
        for v in self._voti:
            if v.punteggio>=punteggio:
                voti_nuovi.append(v)
        self._voti = voti_nuovi

""""def _test_voto():   #modo per testare le classi
    print(__name__)
    v1 = Voto("Munfao", 8, 21, False, "2024-02-29")
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())

if __name__ == "__main__":
    _test_voto()
"""