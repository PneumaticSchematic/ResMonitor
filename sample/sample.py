import tkinter as tk
import psutil

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Label(self)
        self.hi_there["text"] = psutil.cpu_percent(percpu=True)
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def update_cpu_usage(self):
        self.hi_there["text"] = psutil.cpu_percent(percpu=True)
        root.after(1000, app.update_cpu_usage)

root = tk.Tk()
app = Application(master=root)
app.update_cpu_usage()

app.mainloop()