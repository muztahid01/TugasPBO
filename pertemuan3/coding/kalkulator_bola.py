import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas ():
    jari_jari= float (txtjari_jari.get())
    
    Luas = 4*3.14*jari_jari**2

    txtLuas.delete(0,END)
    txtLuas.insert(END,Luas)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())
    
    Volume = 4/3*3.14*jari_jari**3

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Balok")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label jari jari
panjang= Label (frame, text="jari jari: ")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtjari_jari = Entry (frame)
txtjari_jari.grid(row=0, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ") 
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame) 
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()