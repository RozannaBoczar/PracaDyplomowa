import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hi Rozia",
                    foreground='black',
                    background='white',
                    width="50",
                    height="25")
button_detect = tk.Button(text="Detect!")
greeting.pack()
button_detect.pack()
window.mainloop()