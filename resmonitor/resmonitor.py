import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL

import psutil


class Application(tk.Frame):
    CPU_USAGE_UPDATE_TIME_MS = 1000
    NUM_CPUS = psutil.cpu_count()

    def __init__(self, master: tk.Tk = None):
        super().__init__(master)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=master.destroy)
        self.cpu_percent = tk.Label(self)

        self.cpu_list = []
        for i in range(self.NUM_CPUS):
            new_cpu = Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate')
            self.cpu_list.append(new_cpu)

        self.pack()
        self.setup_widgets()

    def setup_widgets(self):
        self.cpu_percent["text"] = psutil.cpu_percent(percpu=True)
        self.cpu_percent.pack(side="top")

        for i in range(self.NUM_CPUS):
            self.cpu_list[i].pack()

        self.quit.pack(side="bottom")

    def update_cpu_usage(self):
        cpu_percent = psutil.cpu_percent(percpu=True)
        self.cpu_percent["text"] = cpu_percent

        for i in range(self.NUM_CPUS):
            self.cpu_list[i]['value'] = cpu_percent[i]

        self.master.after(self.CPU_USAGE_UPDATE_TIME_MS, self.update_cpu_usage)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.update_cpu_usage()

    app.mainloop()
