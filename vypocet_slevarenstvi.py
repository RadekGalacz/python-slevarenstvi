from tkinter import *
from PIL import Image, ImageTk
from plocha_zarezu import F_zarezu
import math

root = Tk()
root.title('Výpočet vtokových soustav odlitků')
root.geometry('930x500')
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

def get_entry_int(e_item: Entry, label: Label = None) -> int | str:
    try:
        res = int(e_item.get())
    except ValueError as e:
        label_chyba.config(text=f"Zadej celé číslo do pole {label.cget('text') if label else ''}")
        return ""
    return res

def get_entry_float(e_item: Entry) -> float | str:
    try:
        res = float(e_item.get())
    except ValueError as e:
        return ""
    return res

def pomer_vtokovky():
    zarez = get_entry_float(entry_zarez)
    rozvod = get_entry_float(entry_rozvod)
    lici_kul = get_entry_float(entry_LK)

    if not zarez or not rozvod or not lici_kul:
        label_vysledek.config(text="Nejprve zadej poměr vtokové soustavy")
        return
    
    if lici_kul >= zarez and rozvod >= zarez:
        vt_soustava = "Přetlaková"

    else:
        vt_soustava = "Podtlaková"
    label_vysledek.config(text=f"{vt_soustava} vtoková sosutava")

# Tlačítko poměr
button = Button(root, text='Urči', command=pomer_vtokovky)
button.grid(row=1, column=4)

# Label - chyba
label_chyba = Label(root, text = '')
label_chyba.place(x=630, y=170)

# Label - vypsání poměru vtokové soustavy: podtlak/přetlak
label_vysledek = Label(root, text = '')
label_vysledek.place(x=630, y=40)

# Label - text, zadej hmotnot odlitku
label_hmotnost = Label(root, text='Zadej hmotnost odlitku (kg): ')
label_hmotnost.grid(row=2, column=0)

entry_hmotnost = Entry(root, width=8, justify=CENTER)
entry_hmotnost.grid(row=2, column=2)

# Tlačítko hmotnost - plocha zářezů
def urceni_plochy_z():
    hm = entry_hmotnost.get()
    zarez = get_entry_float(entry_zarez)
    rozvod = get_entry_float(entry_rozvod)
    lici_kul = get_entry_float(entry_LK)

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
label_plocha = Label(root, text = '')
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
label_pomer = Label(root, text='Dosaď hodnoty podle obrázku: ')
label_pomer.place(x=0, y=200)

# Label - text, zadej licí čas
label_cas = Label(root, text='t - licí čas (s): ', font=("Helvetica", 10, "italic"))
label_cas.place(x=148, y=250)

# Entry - licí čas
entry_t = Entry(root, width=6, justify=CENTER)
entry_t.place(x=233, y=252)

# Obrázek odlitku
open_image = Image.open('odlit.png')
image1 = open_image.resize((265, 139))
image1 = ImageTk.PhotoImage(image1)

image1_label = Label(root, image=image1)
image1_label.place(x=350, y=170)  

# Funkce aktualizuje proměnnou z MenuButton - faktor tření kovu
def vyber_treni(treni):
    selected_option_treni.set(treni)
    menubutton_treni.config(text=f"\u03BE = {treni}")

selected_option_treni = DoubleVar()

# Vytvoření MenuButton - faktor tření kovu
menubutton_treni = Menubutton(root, text="\u03BE - faktor tření kovu", relief=RAISED, font=("Helvetica", 10, "italic"))
menubutton_treni.place(x=145, y=225)

menu_treni = Menu(menubutton_treni, tearoff=0)
menubutton_treni.config(menu=menu_treni)

# Položky v MenuButton - faktor tření kovu
menu_treni.add_command(label="litina", command=lambda: vyber_treni(0.35))
menu_treni.add_command(label="ocel nad olitky", command=lambda: vyber_treni(0.4))


# Funkce aktualizuje proměnnou z MenuButton - hustota kovu
def vyber_hustota(hustota):
    selected_option_hustota.set(hustota)
    menubutton_hustota.config(text=f"\u03C1 = {hustota}")

selected_option_hustota = DoubleVar()

# Vytvoření MenuButton - hustota
menubutton_hustota = Menubutton(root, text="\u03C1 - hust. kovu (kg/dm3)", relief=RAISED, font=("Helvetica", 10, "italic"))
menubutton_hustota.place(x=145, y=273)

menu_hustota = Menu(menubutton_hustota, tearoff=0)
menubutton_hustota.config(menu=menu_hustota)

# Položky v MenuButton - hustota
menu_hustota.add_command(label="litina", command=lambda: vyber_hustota(7.2))
menu_hustota.add_command(label="ocel nad olitky", command=lambda: vyber_hustota(7.85))

# Výpočet tlakové výšky H (cm)
def tlak_vyska():
    m = get_entry_int(entry_hmotnost, label_hmotnost)
    t = get_entry_int(entry_t, label_cas)    
    c = get_entry_int(entry_c, label_c)
    a = get_entry_int(entry_a, label_a)
    h = get_entry_int(entry_h, label_h)

    if h and a and c:
        H = round((h - (a * a) / (2 * c)) / 10, 1)
        if H > 0:
            label_tlak_vyska.config(text=f"Efektivní licí výška H = {H} cm")
        else:
            label_tlak_vyska.config(text=f"Ověř, že jsi zadal hodnoty 'h' 'a' 'c' správně")
        
    elif h == "" or a == "" or c == "" or m == "" or t == "":
        label_tlak_vyska.config(text=f"")
        label_zarezy_vypocet.config(text=f"")
        return
    
    zarez = get_entry_float(entry_zarez)
    rozvod = get_entry_float(entry_rozvod)
    lici_kul = get_entry_float(entry_LK)
    hustota = get_entry_float(selected_option_hustota)
    treni = get_entry_float(selected_option_treni)

    if m and t and H:
        if hustota < 0.0000000000000001 or treni < 0.0000000000000001:
            label_chyba.config(text=f"Vyber z nabídky '\u03BE - tření' a '\u03C1 - hustota'")
        else:
            zarezy = round(22.6 * m / (hustota * treni * t * math.sqrt(H)), 1)
            rozvod_vypocet = round(zarezy / zarez * rozvod, 1)
            lici_kul_vypocet = round(zarezy / zarez * lici_kul, 1)
            label_zarezy_vypocet.config(text=f"Dle výpočtu ze vzorce je:\nSz = {zarezy} cm2\nSr = {rozvod_vypocet} cm2\nSk = {lici_kul_vypocet} cm2", justify='left')
            label_chyba.config(text=f"")
            
button = Button(root, text='Urči', command=tlak_vyska)
button.place(x=315, y=225)

# Obrázek vzorce pro výpočet plochy zářezů
open_image = Image.open('vzorec_plocha.png')
image2 = open_image.resize((139, 54))
image2 = ImageTk.PhotoImage(image2)

image_labe2 = Label(root, image=image2)
image_labe2.place(x=0, y=230)  

# Label - vypsání tlakové výšky
label_tlak_vyska = Label(root, text = '')
label_tlak_vyska.place(x=630, y=205)

# Label - vypsání plochy zářezů z výpočtu
label_zarezy_vypocet = Label(root, text = '')
label_zarezy_vypocet.place(x=630, y=225)

root.mainloop()