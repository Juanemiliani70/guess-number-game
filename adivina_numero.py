import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class GuessNumber(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title("Juego Adivina el Número")
        self.geometry("400x300")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Imagen
        self.image = Image.open("img/imagen_juego.jpg")
        self.image = self.image.resize((150, 150), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.label_image = tk.Label(self, image=self.photo)
        self.label_image.pack(pady=10)

        # Widgets
        self.label = tk.Label(self, text="Ingresa un número (1 - 100):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.button = tk.Button(self, text="Adivinar", command=self.check_guess)
        self.button.pack(pady=10)

        self.entry.bind("<Return>", self.check_guess_event)

    def check_guess_event(self, event):
        self.check_guess()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                message = "Muy bajo"
            elif guess > self.secret_number:
                message = "Muy alto"
            else: 
                message = f"¡Correcto! Adivinaste el número en {self.attempts} intentos.\nSe ha generado un nuevo número secreto."
                self.secret_number = random.randint(1, 100)
                self.attempts = 0 

            messagebox.showinfo("Resultado", message)
            self.entry.delete(0, tk.END)  
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

if __name__ == "__main__":
    app = GuessNumber()
    app.mainloop()
