import tkinter as tk
import os

window = tk.Tk()
window.title('MouseTrack')
window.geometry('200x100')

def mouseTrack():
    os.system('python mouseLogTest.pyw')

btn1 = tk.Button(window, text="Start", width=15, height=2, command=mouseTrack)
btn1.pack()

window.mainloop()