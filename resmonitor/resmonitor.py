import tkinter as tk

import psutil


class Application(tk.Frame):
    CPU_USAGE_UPDATE_TIME_MS = 1000

    def __init__(self, master: tk.Tk = None):
        super().__init__(master)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=master.destroy)
        self.cpu_percent = tk.Label(self)

        self.pack()
        self.setup_widgets()

    def setup_widgets(self):
        self.cpu_percent["text"] = psutil.cpu_percent(percpu=True)
        self.cpu_percent.pack(side="top")

        self.quit.pack(side="bottom")

    def update_cpu_usage(self):
        self.cpu_percent["text"] = psutil.cpu_percent(percpu=True)
        self.master.after(self.CPU_USAGE_UPDATE_TIME_MS, self.update_cpu_usage)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.update_cpu_usage()

    app.mainloop()
