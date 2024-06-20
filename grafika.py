from tkinter import *
from PIL import Image, ImageTk
from plocha_zarezu import F_zarezu

root = Tk()
root.title('Výpočet vtokových soustav litinových odlitků')
root.geometry('900x500')
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
    zarez = int(entry_zarez.get())
    rozvod = int(entry_rozvod.get())
    lici_kul = int(entry_LK.get())
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

    if not entry_hmotnost.get():
        label_plocha.config(text="Nejprve zadej hmotnost odlitku")
        return
    
    if not entry_zarez.get() or not entry_rozvod.get() or not entry_LK.get():
        label_plocha.config(text=f"Nejprve zadej poměr vtokové soustavy")
        return

    for hmotnost, plocha in F_zarezu.items():
        if hmotnost[0] <= int(hm) <= hmotnost[1]:
            rozvod_vypocet = round((plocha / int(entry_zarez.get()) * int(entry_rozvod.get())), 1)
            lici_kul_vypocet = round((plocha / int(entry_zarez.get()) * int(entry_LK.get())), 1)
            label_plocha.config(text=f"Pro odlitek z tvárné/šedé litiny použij:\n Sz = {plocha} cm2, Sr = {rozvod_vypocet} cm2, Sk = {lici_kul_vypocet} cm2")
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

# Obrázek odlitku
open_image = Image.open('odlit.png')
image1 = open_image.resize((265, 139))
image1 = ImageTk.PhotoImage(image1)

image1_label = Label(root, image=image1)
image1_label.place(x=350, y=150)  


root.mainloop()