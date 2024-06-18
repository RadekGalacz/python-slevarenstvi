from tkinter import *
from plocha_zarezu import F_zarezu

root = Tk()
root.title('Výpočet vtokových soustav')
root.geometry('900x500')
root.resizable(False, False)

# Zadání poměru zářezů
label_zarez = Label(root, text='zářezy  :')
label_zarez.grid(row=0, column=1)

entry_zarez = Entry(root, width=4, justify=CENTER)
entry_zarez.grid(row=1, column=1)

# Zadání poměru rozvodu
label_rozvod = Label(root, text='rozvod  :')
label_rozvod.grid(row=0, column=2)

entry_rozvod = Entry(root, width=4, justify=CENTER)
entry_rozvod.grid(row=1, column=2)

# Zadání poměru licího kůlu
label_LK = Label(root, text='licí kůl')
label_LK.grid(row=0, column=3)

entry_LK = Entry(root, width=4, justify=CENTER)
entry_LK.grid(row=1, column=3)

# Label - text, zadej poměr
label_pomer = Label(root, text='Zadej poměr: ')
label_pomer.grid(row=1, column=0)

def pomer_vtokovky():
    zarez = int(entry_zarez.get())
    rozvod = int(entry_rozvod.get())
    lici_kul = int(entry_LK.get())
    if lici_kul >= zarez and rozvod >= zarez:
        vt_soustava = "přetlaková"
    else:
        vt_soustava = "podtlaková"
    label_vysledek.config(text=f"{vt_soustava} vtoková sosutava")

# Tlačítko poměr
button = Button(root, text='Urči', command=pomer_vtokovky)
button.grid(row=1, column=4)

# Label - vypsání poměru vtokové soustavy: podtlak/přetlak
label_vysledek = Label(root, text = '')
label_vysledek.grid(row=1, column=5)

# Label - text, zadej hmotnot odlitku
label_pomer = Label(root, text='Zadej hmotnost odlitku (kg): ')
label_pomer.grid(row=2, column=0)

entry_hmotnost = Entry(root, width=8, justify=CENTER)
entry_hmotnost.grid(row=2, column=2)

# Tlačítko hmotnost - plocha zářezů
def urcenit_plochy_z():
    hodnota = int(entry_hmotnost.get())
    for hmotnost, plocha in F_zarezu.items():
        if hmotnost[0] <= hodnota <= hmotnost[1]:
            label_plocha.config(text=f"Pro odlitek z tvárné/šedé litiny použij plochu zářezů {plocha} cm2")
        
button = Button(root, text='Urči', command=urcenit_plochy_z)
button.grid(row=2, column=3)

# Label - vypsání hmotnosti - plochy zářezů
label_plocha= Label(root, text = '')
label_plocha.grid(row=2, column=5)




root.mainloop()