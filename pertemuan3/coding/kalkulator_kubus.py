import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    rusuk = float( txttrusuk .get())
    
    Luas = round (6 * rusuk **2)

    txtLuas.delete(0,END)
    txtLuas.insert(END,Luas)

def hitung_volume():
    rusuk = float(txttrusuk.get())
    
    Volume = round (rusuk **3)

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume kubus")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label panjang
panjang= Label (frame, text="rusuk: ")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox rusuk
txttrusuk = Entry (frame)
txttrusuk.grid(row=0, column=1)

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