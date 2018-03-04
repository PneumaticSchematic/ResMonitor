import tkinter as tk
from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar

import psutil


class Application(tk.Frame):
    CPU_USAGE_UPDATE_TIME_MS = 1000

    def __init__(self, master: tk.Tk, proc_info: psutil):
        super().__init__(master)

        self.num_cpus = proc_info.cpu_count()
        self.proc_info = proc_info

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=master.destroy)
        self.cpu_percent = tk.Label(self)

        self.cpu_list = []
        for i in range(self.num_cpus):
            new_cpu = Progressbar(self, orient=HORIZONTAL, length=100,
                                  mode='determinate')
            self.cpu_list.append(new_cpu)

        self.pack()
        self.setup_widgets()

    def setup_widgets(self):
        self.cpu_percent["text"] = self.proc_info.cpu_percent(percpu=True)
        self.cpu_percent.pack(side="top")

        for i in range(self.num_cpus):
            self.cpu_list[i].pack()

        self.quit.pack(side="bottom")

    def update_cpu_usage(self):
        cpu_percent = self.proc_info.cpu_percent(percpu=True)
        self.cpu_percent["text"] = cpu_percent

        for i in range(self.num_cpus):
            self.cpu_list[i]['value'] = cpu_percent[i]

        self.master.after(self.CPU_USAGE_UPDATE_TIME_MS, self.update_cpu_usage)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(
        master=root,
        proc_info=psutil
    )

    app.update_cpu_usage()

    app.mainloop()
