
from plocha_zarezu import F_zarezu
import math

class Vypocet:
    def __init__(self, zarez_prurez):
        self.zarez = zarez_prurez

    def pomer_vtokovky(self, zarez, rozvod, lici_kul):
        rozvod_vypocet = round((self.zarez / zarez * rozvod ), 1)
        lici_kul_vypocet = round((self.zarez / zarez * lici_kul), 1)

# Podmínka definuje, o jaký typ vtokové soustavy se jedná:
        if lici_kul / zarez >= 1:
            vt_soustava = "přetlakovou"
        else:
            vt_soustava = "podtlakovou"
        return (f"Zadal jsi poměr vtokovky:\n(zářez : rozvod : licí kůl)\n"
                f"({zarez} : {rozvod} : {lici_kul}) - jedná se o {vt_soustava} vtokovou sosutavu\n"
                f"Zadaná plocha zářezů je {float(self.zarez)} cm2, to odpovídá rozvodu o průřezu {rozvod_vypocet} cm2 a licímu kůlu o průžezu {lici_kul_vypocet} cm2.")

# Metoda přiřadí hmotnsot odlitku k zadané ploše zářezu:        
    def vyber_ze_slovniku(self):  
        for hmotnost, plocha in F_zarezu.items():
            if plocha >= self.zarez:
                return (f"Počítáš vtokovou soustavu pro odlitek o surové hmotnosti cca: {hmotnost} kg")
        return ("Hmotnost odlitku je nad 32 t")

        
# POUŽITÍ:
# _________________________________________________________________________________________
# Zobrazí dict pro surovou hmotnost odlitku (kg): F zarezu (cm2)
for hmotnost, plocha in F_zarezu.items():
    print(hmotnost , ":", plocha)

# Zadej plochu zářezů dle výpočtu nebo vyber hodnotu ze slovníku podle hmotnosti odlitku:
pomer = Vypocet(2)

# Uveď poměr vtokové soustavy - zářez : rozvod : licí kůl
vtokovka = pomer.pomer_vtokovky(3, 5, 4)
print(vtokovka)

# Zobrazí odpovídající hmotnost odlitku podle celkové plochy zářezů
odpovidajici_m = pomer.vyber_ze_slovniku()
print(odpovidajici_m)




