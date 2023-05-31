import tkinter as tk
import time
from tkinter import messagebox

def set_alarm():
    alarm_time = entry.get()
    try:
        time.strptime(alarm_time, '%H:%M')
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
        return
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Wake up!")
            break

def create_gui():
    global entry
    window = tk.Tk()
    window.title("Alarm Clock")

    label = tk.Label(window, text="Set alarm time (HH:MM):")
    label.pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=5)

    button = tk.Button(window, text="Set Alarm", command=set_alarm)
    button.pack(pady=5)

    window.mainloop()

create_gui()