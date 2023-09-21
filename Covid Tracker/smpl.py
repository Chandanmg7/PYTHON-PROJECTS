import tkinter as tk
import os

coro = tk.Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+100')
coro.configure(bg='#046173')

icon_path = 'corona.ico'

if os.path.exists(icon_path):
    coro.iconbitmap(icon_path)
else:
    print(f"Icon file '{icon_path}' not found. Make sure the icon file is in the same directory as your Python script.")

# Add your app code here

coro.mainloop()
