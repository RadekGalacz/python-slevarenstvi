from tkinter import *
from main import *


root = Tk()
root.title('Výpočet vtokových soustav')
root.geometry('900x500')
root.resizable(False, False)

label_zarez = Label(root, text='zářez  :')
label_zarez.grid(row=0, column=1)

entry_zarez = Entry(root, width=4, justify=CENTER)
entry_zarez.grid(row=1, column=1)

label_rozvod = Label(root, text='rozvod  :')
label_rozvod.grid(row=0, column=2)

entry_rozvod = Entry(root, width=4, justify=CENTER)
entry_rozvod.grid(row=1, column=2)

label_LK = Label(root, text='licí kůl')
label_LK.grid(row=0, column=3)

entry_LK = Entry(root, width=4, justify=CENTER)
entry_LK.grid(row=1, column=3)

label_pomer = Label(root, text='Zadej poměr: ')
label_pomer.grid(row=1, column=0)





root.mainloop()