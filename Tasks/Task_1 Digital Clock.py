import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

root.configure(bg='black')

def time():
    current_time = strftime('%I : %M : %S %p') 
    current_day = strftime('%A, %d %B %Y')  
    time_label.config(text=current_time)
    day_label.config(text=current_day, font=('ds-digital', 15), background='black', foreground='white')
    root.after(1000, time)

time_label = tk.Label(root, font=('ds-digital italic', 35), background='black', foreground='white')

day_label = tk.Label(root, font=('ds-digital', 15), background='black', foreground='white')

time_label.pack(anchor='center')
day_label.pack(anchor='center')

time()

root.mainloop()
