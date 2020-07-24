import time
from tkinter import CENTER

import pyautogui
import tkinter as tk


def screenshot():
    name = int(round(time.time() * 1000))
    name = 'Screenshots images\\{}.png'.format(name)

    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
root.geometry("400x200")
frame = tk.Frame(root)

frame.pack()
button = tk.Button(
    frame,
    text='Take Screenshot',
    command=lambda: [root.iconify(), time.sleep(0.5), screenshot(), root.deiconify()]
)

button.pack(side=tk.TOP)
button.place()
close = tk.Button(
    frame,
    text='Quit',
    command=quit
)
close.pack(side=tk.BOTTOM)
root.title = "ScreenShot"
root.iconphoto(False, tk.PhotoImage(file="C.png"))
root.mainloop()
