import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator App")

        self.translator = Translator()

        # Label dan Entry untuk input teks
        tk.Label(self.master, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10)
        self.input_entry = tk.Entry(self.master, width=40)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button untuk menerjemahkan teks
        translate_button = tk.Button(self.master, text="Translate", command=self.translate_text)
        translate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Label untuk menampilkan hasil terjemahan
        tk.Label(self.master, text="Translation:").grid(row=2, column=0, padx=10, pady=10)
        self.translation_label = tk.Label(self.master, text="")
        self.translation_label.grid(row=2, column=1, padx=10, pady=10)

    def translate_text(self):
        input_text = self.input_entry.get()
        if input_text:
            try:
                translation = self.translator.translate(input_text, dest='en')
                self.translation_label.config(text=translation.text)
            except Exception as e:
                self.translation_label.config(text=f"Error: {str(e)}")
        else:
            self.translation_label.config(text="Error: Enter text to translate.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
