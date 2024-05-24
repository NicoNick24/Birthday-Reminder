import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class BirthdayReminderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Birthday Reminder")
        self.master.geometry("300x200")
        self.master.configure(bg="#FF6B6B")
        
        self.birthdays = {
            "Arriane": "2024-05-06",
            "Nico": "2024-05-31",
            "Justin": "2024-03-10",
            "Jiro": "2024-04-20",
            "John": "2024-05-05",
            "Kyla": "2024-06-30",
            "Geric": "2024-07-12",
            "Tyron": "2024-08-25",
            "Christian": "2024-09-08",
            "Karl": "2024-10-18",
            "George": "2024-11-27",
            "Catay": "2024-12-05"
        }

        self.name_label = tk.Label(master, text="Enter Name:", bg="#FF6B6B", fg="white", font=("Arial", 12))
        self.name_label.pack()

        self.name_entry = tk.Entry(master, bg="white", font=("Arial", 12))
        self.name_entry.pack()

        self.timer_button = tk.Button(master, text="Start Timer", command=self.start_timer, bg="#FFD166", fg="#444444", font=("Arial", 12))
        self.timer_button.pack()

        self.celebrants_frame = tk.Frame(master, bg="#FF6B6B")
        self.celebrants_frame.pack()

        self.celebrants_label = tk.Label(self.celebrants_frame, text="Birthday Celebrants:", bg="#FF6B6B", fg="#FFD166", font=("Arial", 12))
        self.celebrants_label.pack()

        self.celebrants_listbox = tk.Listbox(self.celebrants_frame, bg="white", font=("Arial", 12))
        self.celebrants_listbox.pack()

        self.list_celebrants()

    def start_timer(self):
        name = self.name_entry.get().strip()
        if name:
            if name in self.birthdays:
                birthday_date = datetime.strptime(self.birthdays[name], "%Y-%m-%d")
                today_date = datetime.now()
                if birthday_date > today_date:
                    time_difference = birthday_date - today_date
                    seconds = time_difference.total_seconds()
                    self.master.after(int(seconds * 1000), lambda: self.show_birthday(name))
                else:
                    messagebox.showinfo("Birthday Reminder", f"{name}'s birthday has already passed.")
            else:
                messagebox.showinfo("Birthday Reminder", f"No birthday found for {name}.")
        else:
            messagebox.showwarning("Warning", "Please enter a name.")

    def show_birthday(self, name):
        birthday_window = tk.Toplevel(self.master)
        birthday_window.title("Happy Birthday!")
        birthday_window.geometry("200x100")
        birthday_window.configure(bg="#FF6B6B")

        birthday_label = tk.Label(birthday_window, text=f"Happy Birthday, {name}!", bg="#FF6B6B", fg="#FFD166", font=("Arial", 16))
        birthday_label.pack(pady=20)

    def list_celebrants(self):
        self.celebrants_listbox.delete(0, tk.END)
        for name, birthday in self.birthdays.items():
            birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
            today_date = datetime.now()
            if birthday_date > today_date:
                time_difference = birthday_date - today_date
                days_left = time_difference.days
                self.celebrants_listbox.insert(tk.END, f"{name}: {birthday} (Days left: {days_left})")

def main():
    root = tk.Tk()
    app = BirthdayReminderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
