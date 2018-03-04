import tkinter as tk
import unittest

import psutil

from resmonitor import resmonitor


class TkinterTest(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.app = resmonitor.Application(self.master)
        self.master.withdraw()

    def tearDown(self):
        self.master.destroy()

    def process_events(self):
        self.master.update()


class TestMainPage(TkinterTest):
    def test_cpu_percent(self):
        psutil.cpu_percent = lambda percpu: [1, 1, 1, 1]
        self.app.update_cpu_usage()
        self.assertEqual('1 1 1 1', self.app.cpu_percent['text'])


if __name__ == '__main__':
    unittest.main()
