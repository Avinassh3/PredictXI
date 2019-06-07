from tkinter import *
master = Tk()

def var_states():
    partic={}


Label(master, text="Your Team:").grid(row=0, sticky=W)

england = IntVar()
Checkbutton(master, text="eng", variable=england).grid(row=1, sticky=W)
australia = IntVar()
Checkbutton(master, text="aus", variable=australia).grid(row=2, sticky=W)
india = IntVar()
Checkbutton(master, text="ind", variable=india).grid(row=3, sticky=W)
newzealand = IntVar()
Checkbutton(master, text="nz", variable=newzealand).grid(row=4, sticky=W)
southafrica = IntVar()
Checkbutton(master, text="Sa", variable=southafrica).grid(row=5, sticky=W)
pakistan = IntVar()
Checkbutton(master, text="Pak", variable=pakistan).grid(row=6, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=7, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=8, sticky=W, pady=4)

mainloop()