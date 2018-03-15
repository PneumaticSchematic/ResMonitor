import tkinter as tk
from tkinter import ttk

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

        self.cpu_labels = []
        self.cpu_bars = []
        for i in range(self.num_cpus):
            new_cpu = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=100,
                                      mode='determinate', style="blue.Horizontal.TProgressbar")
            self.cpu_bars.append(new_cpu)

            new_label = tk.Label(self)
            self.cpu_labels.append(new_label)

        self.pack()
        self.setup_widgets()

    def setup_widgets(self):
        cpu_percent = self.proc_info.cpu_percent(percpu=True)
        self.cpu_percent.pack(side="top")

        for i in range(self.num_cpus):
            self.cpu_bars[i].pack()
            self.cpu_labels[i].pack()
            self.cpu_labels[i]["text"] = cpu_percent[i]

        self.quit.pack(side="bottom")

    def update_cpu_usage(self):
        cpu_percent = self.proc_info.cpu_percent(percpu=True)
        self.cpu_percent["text"] = cpu_percent

        for i in range(self.num_cpus):
            self.cpu_bars[i]['value'] = cpu_percent[i]
            self.cpu_labels[i]["text"] = cpu_percent[i]

        self.master.after(self.CPU_USAGE_UPDATE_TIME_MS, self.update_cpu_usage)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(
        master=root,
        proc_info=psutil
    )

    root.attributes('-type', 'dialog')

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')

    app.update_cpu_usage()

    app.mainloop()
