from tkinter import *
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import pyperclip

class QRCodeGenerator(Tk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Generator")
        self.geometry("400x400")
        self.resizable(0, 0)

        self.input_text = StringVar(self)

        self.create_widgets()

        self.mainloop()

    def generate_qr_code(self):
        text = self.input_text.get()
        if not text:
            messagebox.showerror("Error", "Input text cannot be empty!")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img_path = "qr_code.png"
        img.save(img_path)

        self.display_qr_code(img_path)

        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Your text was copied to the clipboard!")

    def display_qr_code(self, img_path):
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.LANCZOS)  # Используем Image.LANCZOS вместо Image.ANTIALIAS
        img = ImageTk.PhotoImage(img)

        self.qr_label.config(image=img)
        self.qr_label.image = img

    def create_widgets(self):
        Label(self, text="Enter text to generate QR code:").pack(pady=10)

        Entry(self, textvariable=self.input_text, width=50).pack(pady=10)

        Button(self, text="Generate QR Code", command=self.generate_qr_code).pack(pady=10)

        self.qr_label = Label(self)
        self.qr_label.pack(pady=10)

if __name__ == "__main__":
    QRCodeGenerator()
