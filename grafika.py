from tkinter import *
from PIL import Image, ImageTk
from plocha_zarezu import F_zarezu
import math

root = Tk()
root.title('Výpočet vtokových soustav litinových odlitků')
root.geometry('920x500')
root.resizable(False, False)

# Zadání poměru zářezů
label_zarez = Label(root, text='zářezy  :\n(z)')
label_zarez.grid(row=0, column=1)

entry_zarez = Entry(root, width=4, justify=CENTER)
entry_zarez.grid(row=1, column=1)

# Zadání poměru rozvodu
label_rozvod = Label(root, text='rozvod  :\n(r)')
label_rozvod.grid(row=0, column=2)

entry_rozvod = Entry(root, width=4, justify=CENTER)
entry_rozvod.grid(row=1, column=2)

# Zadání poměru licího kůlu
label_LK = Label(root, text='licí kůl\n(k)')
label_LK.grid(row=0, column=3)

entry_LK = Entry(root, width=4, justify=CENTER)
entry_LK.grid(row=1, column=3)

# Label - text, zadej poměr
label_pomer = Label(root, text='Zadej poměr: ', anchor='w', width=22)
label_pomer.grid(row=1, column=0)

def pomer_vtokovky():
    zarez = entry_zarez.get()
    rozvod = entry_rozvod.get()
    lici_kul = entry_LK.get()

    if not entry_zarez.get() or not entry_rozvod.get() or not entry_LK.get():
        label_vysledek.config(text="Nejprve zadej poměry vtokové soustavy")
        return
    
    if lici_kul >= zarez and rozvod >= zarez:
        vt_soustava = "Přetlaková"

    else:
        vt_soustava = "Podtlaková"
    label_vysledek.config(text=f"{vt_soustava} vtoková sosutava")

# Tlačítko poměr
button = Button(root, text='Urči', command=pomer_vtokovky)
button.grid(row=1, column=4)

# Label - vypsání poměru vtokové soustavy: podtlak/přetlak
label_vysledek = Label(root, text = '')
label_vysledek.place(x=630, y=40)

# Label - text, zadej hmotnot odlitku
label_pomer = Label(root, text='Zadej hmotnost odlitku (kg): ')
label_pomer.grid(row=2, column=0)

entry_hmotnost = Entry(root, width=8, justify=CENTER)
entry_hmotnost.grid(row=2, column=2)

# Tlačítko hmotnost - plocha zářezů
def urceni_plochy_z():
    hm = entry_hmotnost.get()
    zarez = float(entry_zarez.get().replace(',', '.'))
    rozvod = float(entry_rozvod.get().replace(',', '.'))
    lici_kul = float(entry_LK.get().replace(',', '.'))

    if not entry_hmotnost.get():
        label_plocha.config(text="Nejprve zadej hmotnost odlitku")
        return
    
    if not zarez or not rozvod or not lici_kul:
        label_plocha.config(text=f"Nejprve zadej poměr vtokové soustavy")
        return

    for hmotnost, plocha in F_zarezu.items():
        if hmotnost[0] <= int(hm) <= hmotnost[1]:
            rozvod_vypocet = round(((plocha / zarez) * rozvod), 1)
            lici_kul_vypocet = round((((plocha / zarez) * lici_kul)), 1)
            label_plocha.config(text=f"Pro odlitek z tvárné/šedé litiny použij:\nSz = {plocha} cm2\nSr = {rozvod_vypocet} cm2\nSk = {lici_kul_vypocet} cm2", justify='left')
            return
        else:
            label_plocha.config(text=f"Uvedená hmotnost je mimo seznam hodnot")
        
button = Button(root, text='Urči', command=urceni_plochy_z)
button.grid(row=2, column=3)

# Obrázek vtokovky
open_image = Image.open('vtok.png')
image = open_image.resize((265, 139))
image = ImageTk.PhotoImage(image)

image_label = Label(root, image=image)
image_label.place(x=350, y=0)  

# Label - vypsání hmotnosti - plochy zářezů
label_plocha= Label(root, text = '')
label_plocha.place(x=630, y=60)

# H - výška hladiny nad zářezem
label_h = Label(root, text='h (mm)')
label_h.place(x=170, y=180)

entry_h = Entry(root, width=6, justify=CENTER)
entry_h.place(x=172, y=200)

# A - výška odlitku nad zářezem
label_a = Label(root, text='a (mm)')
label_a.place(x=220, y=180)

entry_a = Entry(root, width=6, justify=CENTER)
entry_a.place(x=222, y=200)

# C - celková výška odlitku
label_c = Label(root, text='c (mm)')
label_c.place(x=270, y=180)

entry_c = Entry(root, width=6, justify=CENTER)
entry_c.place(x=272, y=200)

# Label - text, zadej hodnoty podle obrázku
label_pomer = Label(root, text='Zadej hodnoty podle obrázku: ')
label_pomer.place(x=0, y=200)

# Label - text, zadej licí čas
label_pomer = Label(root, text='Zadej licí čas (s): ')
label_pomer.place(x=0, y=225)

# Entry - licí čas
entry_t = Entry(root, width=6, justify=CENTER)
entry_t.place(x=172, y=225)

# Obrázek odlitku
open_image = Image.open('odlit.png')
image1 = open_image.resize((265, 139))
image1 = ImageTk.PhotoImage(image1)

image1_label = Label(root, image=image1)
image1_label.place(x=350, y=150)  

# Výpočet tlakové výšky H (cm)
def tlak_vyska():
    h = entry_h.get()
    a = entry_a.get()
    c = entry_c.get()
    m = entry_hmotnost.get()
    t = entry_t.get()

    if not h or not a or not c or not m or not t:
        label_tlak_vyska.config(text="Nejprve zadej hodnoty podle obrázku a ověř,\n že jsi zadal hm. odlitku (kg) a čas lití (s)", justify='left')
        return
    
    h = int(entry_h.get())
    a = int(entry_a.get())
    c = int(entry_c.get())
    m = int(entry_hmotnost.get())
    t = int(entry_t.get())
    
    zarez = float(entry_zarez.get().replace(',', '.'))
    rozvod = float(entry_rozvod.get().replace(',', '.'))
    lici_kul = float(entry_LK.get().replace(',', '.'))

    H = round((h - (a * a) / (2 * c)) / 10, 1)

    zarezy = round(22.6 * m / (7 * 0.35 * t * math.sqrt(H)), 1)
    rozvod_vypocet = round((zarezy / zarez * rozvod), 1)
    lici_kul_vypocet = round(zarezy / zarez * lici_kul, 1)

    label_tlak_vyska.config(text=f"Efektivní licí výška H = {H} cm")
    label_zarezy_vypocet.config(text=f"Dle výpočtu je:\nSz = {zarezy} cm2\nSr = {rozvod_vypocet} cm2\nSk = {lici_kul_vypocet} cm2", justify='left')

button = Button(root, text='Urči', command=tlak_vyska)
button.place(x=315, y=220)

# Obrázek vzorce pro výpočet plochy zářezů
open_image = Image.open('vzorec_plocha.png')
image2 = open_image.resize((139, 48))
image2 = ImageTk.PhotoImage(image2)

image_label2 = Label(root, image=image2)
image_label2.place(x=630, y=150)  

# Label - vypsání tlakové výšky
label_tlak_vyska= Label(root, text = '')
label_tlak_vyska.place(x=630, y=200)

# Label - popisek symbolů ke vzorci
label_vzorec_popis= Label(root, text = '\u03BE - faktor tření kovu 0,35\nt - čas lití (s),\n\u03C1 - hustota (kg/m3)', justify='left')
label_vzorec_popis.place(x=775, y=150)

# Label - vypsání plochy zářezů z výpočtu
label_zarezy_vypocet= Label(root, text = '')
label_zarezy_vypocet.place(x=630, y=225)

root.mainloop()