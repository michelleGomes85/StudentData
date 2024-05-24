import tkinter as tk
from tkinter import scrolledtext


class TextDialog:

    def __init__(self, title, font=None):
        
        self.root = tk.Tk()
        self.root.title(title)

        if font:
            self.font = font
        else:
            self.font = ('Courier', 10)

    def show_text(self, text):
        
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=10, font=self.font)
        self.text_area.pack(expand=True, fill='both')
        self.text_area.insert(tk.INSERT, text)
        self.text_area.configure(state='disabled') 

        self.ok_button = tk.Button(self.root, text="OK", command=self.close)
        self.ok_button.pack()

        self.root.mainloop()

    def show_error(self, error_message):
        
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=10, font=self.font)
        self.text_area.pack(expand=True, fill='both')
        self.text_area.insert(tk.INSERT, "Erro: " + error_message)
        self.text_area.configure(state='disabled') 

        self.ok_button = tk.Button(self.root, text="OK", command=self.close)
        self.ok_button.pack()

        self.root.mainloop()

    def close(self):
        self.root.destroy()