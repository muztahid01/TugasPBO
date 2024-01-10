import tkinter as tk
from tkinter import Frame,Label,Entry,Button,W

def konversi_suhu():
    try:
        # Dapatkan nilai dari input pengguna
        suhu_celsius = float(entry_celsius.get())
        
        # Lakukan konversi suhu
        suhu_fahrenheit = (suhu_celsius * 9/5) + 32
        
        # Tampilkan hasil konversi
        label_hasil["text"] = f"Hasil Konversi: {suhu_fahrenheit:.2f} Fahrenheit"
    except ValueError:
        label_hasil["text"] = "Masukkan suhu dalam format angka."

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Konversi Suhu")

# Membuat widget-label
label_celsius = tk.Label(root, text="Masukkan Suhu Celsius:")
label_celsius.pack(pady=10)

# Membuat widget-entry untuk pengguna memasukkan suhu
entry_celsius = tk.Entry(root)
entry_celsius.pack(pady=10)

# Membuat tombol untuk memicu konversi
tombol_konversi = tk.Button(root, text="Konversi", command=konversi_suhu)
tombol_konversi.pack(pady=10)

# Membuat widget-label untuk menampilkan hasil konversi
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
